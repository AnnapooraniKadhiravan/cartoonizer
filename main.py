import cv2 #computer vision to read images 
import numpy as np   #to perform mathematical operations on arrays
from tkinter.filedialog import *   #code causes several widgets like button,frame,label

photo = askopenfilename() #opens internal file to select image
img = cv2.imread(photo)  #loads an image from the specified file

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #used to convert an image from one color space to another
grey = cv2.medianBlur(grey, 5)  #central pixel is replace with median value,computes median value
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9 ,9) #separate desirable foreground image objects from background based on the difference in pixel intensities of each region

#cartoonize
color = cv2.bilateralFilter(img,9,250,250)  #edge preserving and noise-reducing smoothing filter for images
cartoon = cv2.bitwise_and(color,color,mask = edges) #calculates the conjunction of pixel in both images

cv2.imshow("Image", img) #used to display an image in a window
cv2.imshow("Cartoon",cartoon)

#save
cv2.imwrite("cartoon.jpg",cartoon) #used to save an image to any storage device
cv2.waitKey(0) #it only accepts time in milliseconds as an argument.
cv2.destroyAllWindows() #simply destroys all the windows we created
