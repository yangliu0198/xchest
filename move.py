import random
import os
from shutil import copyfile

rootDir = '../../../../media/data/yangliu/xrays/images/'
trainDir = '../../../../media/data/yangliu/xrays/train_images/'
valDir = '../../../../media/data/yangliu/xrays/val_images/'
for fname in os.listdir(rootDir):
	if fname.endswith('.png'):
		rnd_idx = random.random()

		if rnd_idx < 0.1:
			copyfile(rootDir + fname, valDir + fname)
		else:
			copyfile(rootDir + fname, trainDir + fname)
