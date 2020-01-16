import cv2

import PIL import image 
import sys

imagePath=sys.argv[1]
cascPath=""
maskPath=""

faceCascade= cv2.CascadeClassifier(cascPath)

image=cv2.imread(imagePath)
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(gray,1.15)

for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),2)
    cv2.waitKey(0)