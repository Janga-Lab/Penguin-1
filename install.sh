#!/bin/bash
#build tools
sudo apt-get install build-essential
sudo apt-get install libz-dev
sudo apt-get install libbz2-dev
sudo apt-get install libncurses5-dev
sudo apt-get install -y liblzma-dev
sudo apt-get install libcurl4-openssl-dev

#build tools for scrappy

sudo apt-get install libcunit1
sudo apt-get install libcunit1-dev
sudo apt-get install libhdf5
sudo apt-get install libhdf5-dev
sudo apt-get install libopenblas-base
sudo apt-get install libopenblas-dev
sudo apt-get install cmake

#install scrappy
git clone https://github.com/nanoporetech/scrappie
cd scrappie
mkdir build && cd build && cmake .. && make
cd ..


#install minimap2
git clone https://github.com/lh3/minimap2
cd minimap2 && make
cd ../..

#install squiggleKit & scrappie
#git clone https://github.com/Psy-Fer/SquiggleKit.git
pip install numpy h5py sklearn matplotlib
#pip install scrappie
pip3 install tensorflow==2.1.0
pip install keras
#create empty directory for data
mkdir Data/basecall/

#change permissions for folder
cd ..
chmod -R 777 Penguin
cd Penguin

#installing nanopolish
sudo apt-get install nanopolish
#git clone --recursive https://github.com/jts/nanopolish.git
#cd nanopolish
#make
#cd ..

#install prerequisites for samtools
git clone https://github.com/samtools/htslib
cd htslib
autoheader
autoconf
./configure
make
make install
cd ..

#install samtools (bug requires permissions)
git clone https://github.com/samtools/samtools
cd samtools
autoconf -Wno-syntax
./configure --without-curses
make
make install
cd ..
