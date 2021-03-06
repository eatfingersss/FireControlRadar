import numpy as np
import cv2
from ServoCtl import ServoCtl
import ReadConfig

WIDTH = 800
HEIGHT = 600

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
            
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.line(img, (x, y), (x+w, y+h), ( 0, 0,255), 2)
            cv2.line(img, (x+w, y), (x, y+h), ( 0, 0,255), 2)
	 #flag |= True

        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #cv2.line(img, (x, y), (x+w, y+h), ( 0, 0), 2)
            #cv2.line(img, (x+w, y), (x, y+h), ( 0, 0), 2)
        flag |= True
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.line(img, (0, int(HEIGHT/2.0)), (WIDTH, int(HEIGHT/2.0)), (255, 0, 0), 2)
    cv2.line(img, (int(WIDTH/2), 0), (int(WIDTH/2.0), HEIGHT), (255, 0, 0), 2)   

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
