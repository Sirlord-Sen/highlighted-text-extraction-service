import os
import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
from .utils import *

# Loading Pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def text_detect(img_title):
    img_path = os.path.abspath('app\static\images')
    path = f'{img_path}/{img_title}'

    img = cv2.imread(path)

    # HSV value for Yellow Highlight
    hsv = [0, 179, 49, 255, 183, 255]

    #### Detect Color ####
    imgResult = detectColor(img, hsv)

    #### Get Contours ####
    imgContours, contours = getContours(imgResult, img, showCanny=False, minArea=1000, filter=4, cThr=[250, 250], draw=True)

    #### Get Roi ####
    roiList = getRoi(imgContours, contours)
    roiDisplay(roiList)

    #### Recognize Text with Tesseract ####
    highlightedText = []
    for x, roi in enumerate(roiList):
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        highlight = (pytesseract.image_to_string(roi, lang='eng', config='--psm 6'))
        highlightedText.append(highlight)
    saveText(highlightedText)
    return highlightedText
    # cv2.waitKey(0)