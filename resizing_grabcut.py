from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# Opens a image in RGB mode
#im1 = cv2.imread(r'C:\Users\ayush\Downloads\New folder\25.jpg')
im1 = Image.open(r"C:\Users\ayush\Downloads\download_test.jpg")
 
# Cropped image of above dimension
# (It will not change original image)
#im1 = im.crop((left, top, right, bottom))
newshape=(192,256)
im2=im1.resize(newshape)
#im1 = cv2.resize(im1,(192,256),interpolation = cv2.INTER_NEAREST)
# Shows the image in image viewer
#im2 = Image.fromarray(im1)
im2.save(r"test_cloth25.jpg")

im1 = cv2.imread(r'C:\Users\ayush\Downloads\download_test.jpg')

#OLD_IMG = im1.copy()
#print(im1.shape[1])
mask = np.zeros(im1.shape[:2], np.uint8)
SIZE = (1, 65)
bgdModle = np.zeros(SIZE, np.float64)

fgdModle = np.zeros(SIZE, np.float64)
rect = (1, 1, im1.shape[1], im1.shape[0])
cv2.grabCut(im1, mask, rect, bgdModle, fgdModle, 10, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
im_new = im1*mask2[:, :, np.newaxis]

bgd= im1 - im_new
bgd[np.where((bgd > [0,0,0]).all(axis = 2))] =[1,1,1]
bgd[np.where((bgd < [1,1,1]).all(axis = 2))] =[255,255,255] 

#for i in range(len(im1)):
    #for j in range(len(im1[0])):
        #if np.all(im1[i, j] != 0):
            #im1[i,j]=(255,255,255)


#print(bgd[37,125])
im3 = Image.fromarray(bgd)
im3.save(r"test_edge26.jpg")
