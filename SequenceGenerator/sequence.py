import argparse
import subprocess
import os, sys, platform

import SequenceGenerator.basecall as bc 
import SequenceGenerator.qtoa as qa
import SequenceGenerator.align as al

'''
#include download directory
sys.path.insert(1, "../downloads/")

#from minimap import download_map as dmap
#download required tools/files
#check if minmap is installed
minstall = True
squiggleInstall = True
minmapDir = os.getcwd() + "minimap2"
print("mindir ", minmapDir)
for dirname, subdir, files in os.walk(os.getcwd()):    
    if "minimap2" in subdir:
        print("already installed minmap2")
        minstall = False

    if "SquiggleKit" in subdir:
        print("already installed SquiggleKit")
        squiggleInstall = False

#if not installed then install
if minstall:
    os.system("git clone https://github.com/lh3/minimap2")
    os.system("cd minimap2 && make")

if squiggleInstall:
    #check for squiggle Kit download
    if platform.system() == "Windows":
        print("Squiggle kit currently doesn't work with windows")

    #os.system("cd download_directory")
    os.system("git clone https://github.com/Psy-Fer/SquiggleKit.git")
    os.system("pip install numpy h5py sklearn matplotlib")
    os.system("pip install scrappie")

#check for all files
parser = argparse.ArgumentParser(description="Start of Getting Nanopore Signals")

#input folder of fast5 files
parser.add_argument('-i', action='store', dest='path_input', help='Provide Fast5 folder path')
#bed file argument
parser.add_argument('-b', action='store', dest='bed_input', help='Provide Bed file')
#reference genome to align
parser.add_argument('-ref', action='store', dest='ref_input', help='Provide reference genome file')


#get arguments
results = parser.parse_args()
#directory argument
directory = results.path_input
'''


#prepare all files needed for signal extraction
def prep_required_files(bedfile, fast5Path=None, referenceFile=None, samFile=None):
    #basecall the fast5 files and return directory
    prompt = input("basecall?(y/n)")
    if prompt == "y":
        bc.basecall_files(fast5Path)
        print("after basecall")
        #convert fastq to fasta
        #newDirectory = fast5Path + "basecall/"
        newDirectory = os.getcwd() + "/Data/basecall/"
        qa.convertFastq(newDirectory)

    #align fastq and get sam file
    #bwa-mem
    if samFile == None:
        if referenceFile != None:
            for file in os.listdir(newDirectory):
                if file.endswith(".fastq"):
                    #input minmap directory
                    minmapDir = os.getcwd() + "minimap2"
                    samFile = al.minimapAligner(file, referenceFile, minDir=minmapDir)

        else:
            print("Input Reference File")

    #get default bedfile if empty
    if bedfile == None:
        pass

    return bedfile, fast5Path, referenceFile, samFile








