#!/usr/bin/env python3
import os
import numpy as np

dataroot = '/data/datasets/blurred_sharp/blurred_sharp'
subdirs = os.listdir(dataroot)
filenames = None

splits = None

np.random.seed(0)

for subdir in subdirs: # blurred or sharp
    if filenames is None:
        folder = os.path.join(dataroot, subdir)
        filenames = np.array(os.listdir(folder))
    else:
        filenames = [filename for filename in os.listdir(folder) if filename in filenames]

np.random.shuffle(filenames)
for subdir in subdirs: # blurred or sharp
    print(subdir)
    folder = os.path.join(dataroot, subdir)
    if splits is None:
        N = len(filenames)
        N_train = N * 85 // 100
        splits = {'train': filenames[:N_train], 'val': filenames[N_train:]}

    for k, v in splits.items():
        for img in v:
            if 'png' not in img:
                continue
            os.rename(os.path.join(folder, img), os.path.join(folder, k, img))
# vim: ts=4 sw=4 sts=4 expandtab
