import os

try:

   from opencv import Fore,init
   init()
except ImportError:
    os.system("pip3 install opencv-python")


import cv2
import time
import datetime

camera = cv2.VideoCapture(0)

while camera.is0pened():
  r, frame = camera.read()
  
  if cv2.waitKey(10) == ord('q'):
    break
  cv2.imshow("gx7gaming camera python", frame)