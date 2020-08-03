"""
ARE YOU FAN OF HARRY POTTER...?
Project By..Akshay7802.
Enjoy..!!

"""

import cv2
import numpy as np
import time



## Reading the webcam
cap = cv2.VideoCapture(0)
##  Allowing System to sleep for 5 sec before webcam starts :
time.sleep(3)
count = 0
background = 0
## Capturing the background in range :
for i in range(60):
    ret,background = cap.read()
background = np.flip(background,axis=1)

## Reading the images from the webcam
while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    count+=1
    img = np.flip(img,axis=1)

    ## Converting the color space from BGR(BLUE,GREEEN,RED) to HSV(HUE,SATURATION,VALUE)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## Generating mask to detect red color
    lowerRed = np.array([110,50,50])
    upperRed = np.array([120,255,255])
    masked1 = cv2.inRange(hsv,lowerRed,upperRed)

    lowerRed = np.array([120,50,50])
    upperRed = np.array([130,255,255])
    masked2 = cv2.inRange(hsv,lowerRed,upperRed)

    masked1 = masked1+masked2

    # Refining the mask corresponding to the detected red color
    masked1 = cv2.morphologyEx(masked1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
    masked1 = cv2.dilate(masked1,np.ones((3,3),np.uint8),iterations = 1)
    masked2 = cv2.bitwise_not(masked1)

    # Generating the final output
    res1 = cv2.bitwise_and(background,background,mask=masked1)
    res2 = cv2.bitwise_and(img,img,mask=masked2)
    finalOutput = cv2.addWeighted(res1,1,res2,1,0)

    cv2.imshow("Harry Potter's invisible secret revealed",finalOutput)
    ##key = cv2.waitKey(10)
    if(cv2.waitKey(1)==ord("q")):#press q to stop.
        break
