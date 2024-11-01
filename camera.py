import cv2
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('camera', frame)
    cv2.waitKey(1)
    print(list(frame))
    print(ret)
    for el in frame:
        for i in el:
            print(i, end='')
    break