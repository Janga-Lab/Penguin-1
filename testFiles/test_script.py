import h5py
import SequenceGenerator.align as align
import SignalExtractor.Nanopolish as events
import os

#test to check if required files are created
def file_test(bed_file, ref_file, sam_file):
    if bed_file == None:
        print("bed file test failed****")
        raise FileNotFoundError

    #create aligned sam
    elif ref_file != None and sam_file == None:
        #fasta input
        fastfile = os.getcwd() + "/Data/basecall/"
        for ffile in os.listdir(fastfile):
            if ffile.endswith(".fastq") or ffile.endswith(".fasta"):
                #check if fast files exist in directory
                fastfile = os.getcwd() + "/Data/basecall/" + ffile

        if fastfile.endswith(".fastq") != True and fastfile.endswith(".fasta") != True:
            print("basecall test failed****")
            raise FileNotFoundError

        sam_file = align.minimapAligner(fastfile, ref_file)


    elif ref_file == None and sam_file == None:
        #use default ref files
        refFlag = False
        #defaultReferenceFile = "Homo_sapiens.GRCh38.dna.alt.fa"
        defaultReferenceFile = "refgenome"
        downloadedFlag = False
        #check if default reference file exists
        for f in os.listdir(os.getcwd()):
            if f == defaultReferenceFile:
                print("reference downloaded already****")
                downloadedFlag = True

        if downloadedFlag != True:
            print("RECOMMENDED to download first")
            print("WARNING: default reference file is 18gb in size, ..downloading")
            #os.system("wget -O refgenome.tar.gz ftp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Homo_sapiens/Ensembl/GRCh37/Homo_sapiens_Ensembl_GRCh37.tar.gz")
            os.system("wget -O refgenome.gz ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh37_latest/refseq_identifiers/GRCh37_latest_genomic.fna.gz")
            #os.system("wget -O ftp://ftp.ensembl.org/pub/release-100/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.alt.fa.gz")
            os.system("tar -xzf refgenome.tar.gz")
            os.system("gunzip refgenome.gz")
            print("gunzipping reference genome****")
            #os.system("gunzip -v Homo_sapiens.GRCh38.dna.alt.fa.gz")
            for f in os.listdir(os.getcwd()):
                print(f)
                if f == "Homo_sapiens" or f == defaultReferenceFile or f == "refgenome":
                    refFlag = True
                    break

        ref_file = defaultReferenceFile

        if refFlag == False and downloadedFlag != True:
            print("ref file test failed****")
            raise FileNotFoundError

        #get basecalled file
        fastfile = os.getcwd() + "/Data/basecall/"
        for ffile in os.listdir(fastfile):
            if ffile.endswith(".fastq") or ffile.endswith(".fasta"):
                #check if fast files exist in directory
                fastfile = os.getcwd() + "/Data/basecall/" + ffile
                break

        #ref file exists so align here
        sam_file = align.minimapAligner(fastfile, ref_file)

    elif sam_file == None:
        print("sam file test failed****")
        raise FileNotFoundError

    if bed_file != None:
        print("\nbed file test passed****")
    if sam_file != None:
        print("sam file test passed****")

    return bed_file, ref_file, sam_file


def id_file_test():
    for f in os.listdir("./Data/"):
        if f == "Fast5_ids.txt":
            print("id test passed****")
            return


def event_check(fpath=None, filename=None, ref=None, NanopolishOnly=True):
    #single file
    if fpath == None:
        hdf = h5py.File(filename, 'r')
        #check if event file exists
        if "reads-ref.eventalign.txt" in os.listdir("Data"):
            return "Data/reads-ref.eventalign.txt"

    #multiple files
    else:
        hdf = h5py.File(fpath + filename, 'r')

    fast_keys = hdf.keys()
    if "/Analyses/Basecall_1D_001/BaseCalled_template/Events/" in fast_keys and not NanopolishOnly:
        print("events test passed**** \n")
        show_penguin()
        return None
    #no events
    else:
        if ref != None:
            if event_align_check() == None:
                print("Creating Event Align file****")
                #create events(nanopolish code goes here)
                event_file = events.nanopolish_events(fpath, "Data/basecall/", ref)
                print("event file ", event_file)
                show_penguin()
                return event_file
            else:
                show_penguin()
                return "Data/reads-ref.eventalign.txt"

        else:
            print("reference file test failed")
            raise FileNotFoundError



def show_penguin():
    penguin = """
    =============================================================

      **-..L```|
       \        |
        *        \        |```| |```` |\  | |```| |   | ``|`` |\  |
        |     |    \      |___| |___  | \ | |___  |   |   |   | \ |
       /*\    |     \     |     |     |  \| |   | | | |   |   |  \|
      |***\   |      |    |     |____ |   | |___|  \|/   _|_  |   |
      \****\   \     |                              |
       \***/    \   /                               |
        \*/        /
         /___/_____\

    =============================================================

    """
    print(penguin)


def sequence_check():
    pass


def event_align_check():
    for file in os.listdir("Data"):
        if file == "reads-ref.eventalign.txt":
            return "Data/reads-ref.eventalign.txt"

    print("Event Align Test Failed****")
    return None
