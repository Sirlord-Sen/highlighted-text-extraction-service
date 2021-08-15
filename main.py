# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Import Libraries
# %% [markdown]
# ## Main code

# %%
import sys
import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
from utils import *

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = 'c:/Users/Sir-Lord/Documents/GitHub/highlight-service-v1/public/uploads\\'+ str(sys.argv[1])
# fullpath = path + str(sys.argv[1])

img = cv2.imread(path)
# cv2.imshow('image', img)
# print(img)


##### TRACKBARS ######
# def empty(x):
#     pass

# cv2.namedWindow('TrackBars')
# cv2.resizeWindow('TrackBars', 640, 240)
# cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 51, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 183, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


# while True:
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(imgHSV, lower, upper)
     
#     imgResult = cv2.bitwise_and(img, img, mask=mask)

# #     # cv2.imshow("original", img)
# #     # cv2.imshow("HSV", imgHSV)
#     # cv2.imshow("mask", cv2.resize(mask, (700, 450)))
#     print(pytesseract.image_to_string(imgResult))
#     # cv2.imshow('imgResult', imgResult)
#     cv2.waitKey(1)

# # hsv = [0, 109, 159, 255, 176, 255]
hsv = [0, 179, 49, 255, 183, 255]

# # # # # #### Step 2 ####
imgResult = detectColor(img, hsv)



# # # # # #### Step 3 & 4 ####
imgContours, contours = getContours(imgResult, img, showCanny=False, minArea=1000, filter=4, cThr=[250, 250], draw=True)

# # # # cv2.imshow('imgContours', imgContours)
# print('No. of Highlights:', len(contours))

# # # # # #### Step 5 ####
roiList = getRoi(imgContours, contours)
roiDisplay(roiList)

# # # # # # #### Step 6 ####
highlightedText = []
for x, roi in enumerate(roiList):
    highlightedText.append(pytesseract.image_to_string(roi, lang='eng', config='--psm 6'))
print(highlightedText)
# saveText(highlightedText)



cv2.waitKey(0)


# %%



