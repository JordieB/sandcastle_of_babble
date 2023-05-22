#!/bin/bash
# For CUDA
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb

sudo apt update
sudo apt install -y python3-pyaudio espeak ffmpeg cuda