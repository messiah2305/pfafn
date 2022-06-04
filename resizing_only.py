from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# Opens a image in RGB mode
#im1 = cv2.imread(r'C:\Users\ayush\Downloads\New folder\25.jpg')
im1 = Image.open(r"C:\Users\ayush\Downloads\New folder\seed0000.png")
 
# Cropped image of above dimension
# (It will not change original image)
#im1 = im.crop((left, top, right, bottom))
newshape=(750,1101)
im2=im1.resize(newshape)
#im1 = cv2.resize(im1,(192,256),interpolation = cv2.INTER_NEAREST)
# Shows the image in image viewer
#im2 = Image.fromarray(im1)
im2.save(r"0new.jpg")