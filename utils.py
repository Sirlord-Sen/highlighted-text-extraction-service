import cv2
import numpy as np


def detectColor(img, hsv):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow("imgResult", imgHSV)
    lower = np.array([hsv[0], hsv[2], hsv[4]])
    upper = np.array([hsv[1], hsv[3], hsv[5]])
    mask = cv2.inRange(imgHSV, lower, upper)
    # cv2.imshow("imgResult", mask)
    imgMask = cv2.bitwise_and(img, img, mask=mask)
    # cv2.imshow("imgResult", imgMask)
    imgResult = cv2.bitwise_and(imgMask, imgMask, mask=mask)
    # cv2.imshow("imgResult", imgResult)
    return imgResult

def getContours(img, imgDraw, cThr=[100, 100], showCanny=False, minArea=1000, filter=0, draw=False):
    imgDraw = imgDraw.copy()
    imgCopy = img.copy()
    imgGray = cv2.cvtColor(imgCopy, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (15, 15), 1)
    imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])
    kernel = np.array((10, 10))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=1)
    imgClose = cv2.morphologyEx(imgDial, cv2.MORPH_CLOSE, kernel)

    if showCanny: cv2.imshow('Canny', imgClose)
    contours, hiearchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print('length of contours', len(contours))
    # cnt = contours[0]
    # img = cv2.drawContours(img, contours, [cnt], (0,255,0), 3)
    # cv2.imshow("contours", cv2.resize(img, (800 ,500)))
    finalContours = []
    for i in contours:
        img = cv2.drawContours(img, i, -1, (0, 255, 0), 3)
        area = cv2.contourArea(i)
        if area > minArea:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.0002 * peri, True)
            bbox = cv2.boundingRect(approx)
            if filter > 0 :
                if len(approx) == filter:
                    finalContours.append([len(approx), area, approx, bbox, i])

                else:
                    finalContours.append([len(approx), area, approx, bbox, i])

    finalContours = sorted(finalContours, key=lambda x: x[1], reverse=True)
    if draw:
        for con in finalContours:
            # print('con', con[3])
            x, y, w, h = con[3]
            # cv2.imshow('copy', imgCopy)
            cv2.rectangle(imgCopy, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.drawContours(imgDraw, con[4], -1,(0,0,255), 2)
        # cv2.imshow("Things" ,imgDraw)
    return imgCopy, finalContours

def getRoi(img, contours):
    roiList = []
    for con in contours:
        x, y, w, h = con[3]
        roiList.append(img[y:y + h, x:x +w])
    return roiList

def roiDisplay(roiList):
    for x, roi in enumerate(roiList):
        roi = cv2.resize(roi, (0,0), None, 2, 2)
        # cv2.imshow(str(x),roi)
        
def saveText(highlightedText):
    with open('highlightedText.csv', 'w') as f:
        for text in highlightedText:
            f.writelines(f'\n{text}')

