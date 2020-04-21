from statistics import mean, median
#from keras.models import model_from_json
from tensorflow.keras.models import model_from_json
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from enum import Enum
import pickle
import numpy as np


def createInstance(kmer, raw_signal, type=None):
    #requirements for NN model
    #kmer/median/mean/max/min
    inst = []

    inst.append(mean(raw_signal))
    inst.append(median(raw_signal))
    inst.append(max(raw_signal))
    inst.append(min(raw_signal))
    inst.append(len(raw_signal))

    for k in kmer:
        inst.append(k)
        
    inst = np.array(inst)
    inst = np.transpose(inst)
    return inst


def prepareNNModel():
    #load model
    json_file = open("./Models/NNmodel.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)
    #load weights
    loaded_model.load_weights("./Models/model.h5")
    print("loaded model")
    loaded_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
    return loaded_model


def createEncoder(X):
    #A G C T
    '''
    le = LabelEncoder()          
    le.fit(X)
    X = le.transform(X)
    X = X.reshape(-1, 1)

    #onehot encode
    _, n_features = np.shape(X)
    enc = OneHotEncoder(handle_unknown='ignore', categories='auto')
    enc.fit(X)
    '''
    #load encoder
    le = LabelEncoder()          
    le.fit(X)
    X = le.transform(X)
    X = X.reshape(-1, 1)
    enc = None
    with open("./Models/encoder", 'rb') as e:
        enc = pickle.load(e)

    if enc != None:
        onehots = enc.transform(X).toarray()
    else:
        raise Exception

    return onehots
    

def to_onehot(encoder, kmer):
    onehot = encoder.transform(kmer).toarray()
    return onehot
    


    
