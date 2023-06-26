#!/bin/bash
# conda init bash
# conda activate orchid
python3 ./tools/build_df.py /home/chs.gpu/Documents/rintu/researchxoscc/project-1/train
python3 ./training/test_data_loader.py /home/chs.gpu/Documents/rintu/researchxoscc/project-1/train DenseNet121