# Python script used to resieze the wbc images to 128*128

import os 
import pandas as pd
from pathlib import Path
import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
import cv2
from PIL import Image
import numpy as np
# Ignore warnings
import warnings

# dataset_path = '/Users/KyleWang/Desktop/Blood_cell_classification_kaggle/kaggle/blood_cell'
dataset_path = Path('./wbc_reorg/')
images_path = list(dataset_path.glob(r"**/*.jpg"))
print(len(images_path))


for path in images_path:
    im = Image.open(path).resize((128,128))
    im.save(path) 

print("DONE!")


