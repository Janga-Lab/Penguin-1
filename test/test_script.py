import h5py

#test to check if required files are created
def file_test(bed_file, ref_file, sam_file):
    if bed_file == None:
        raise FileNotFoundError

    elif ref_file == None:
        raise FileNotFoundError

    elif sam_file == None:
        raise FileNotFoundError

    return


def id_file_test():
    pass


def event_check(filename):
    hdf = h5py.File(filename, 'r')
    print(hdf.keys())


def sequence_check():
    pass