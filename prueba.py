import cv2 
import numpy as np
import sys


video_capture = cv2.VideoCapture(0)
#video_capture.set(cv2.CAP_PROP_FPS, 15)


while True:
    # Capture frame-by-frame
    ret, image = video_capture.read()

    if not ret:
        print("no ret")
    else:
        #filtro imagen
        kernel =  np.array([[1,1,1],[1,-8,1],[1,1,1]])
        #print(kernel)
        image=cv2.GaussianBlur(image,(5,5),0)
        image = cv2.filter2D(image,-10,kernel)

        #////////
        fast = cv2.FastFeatureDetector_create() #FastFeatureDetector()
        
        fast.setThreshold(20)

        kp = fast.detect(image)
        cv2.drawKeypoints(image, kp, image, color=(255,0,0))
        image[1:100,1:10]=[0,0,0]
        cv2.imshow("video", image)
    print(image[10, 10])
   
    cv2.waitKey(1)