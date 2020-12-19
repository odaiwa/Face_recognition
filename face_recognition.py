import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath= "haarcascade_frontalface_default.xml"

faceCascade=cv2.CascadeClassifier(cascadePath)

font=cv2.FONT_HERSHEY_TRIPLEX

id=0

names = [0, 1, 2, 3, 4, 5]

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW=0.1*cam.get(3)
minW=0.1*cam.get(4)

while True:

