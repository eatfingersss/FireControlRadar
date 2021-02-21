import numpy as np
import cv2
from ServoCtl import ServoCtl
import ReadConfig

WIDTH = 640
HEIGHT = 480

files = ReadConfig.get_cascade_files()
for it in files:
    faceCascade = cv2.CascadeClassifier('Cascades/' + it)

cap = cv2.VideoCapture(0)
cap.set(3, WIDTH)  # set Width
cap.set(4, HEIGHT)  # set Height
sc = ServoCtl(WIDTH,HEIGHT)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    flag = False
    for (x, y, w, h) in faces:
        if not flag:
            sc.ctl((x + w) / 2, (y + h) / 2)
        flag |= True

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
