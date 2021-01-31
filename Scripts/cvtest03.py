import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'images\kouichiTV.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cascade = cv.CascadeClassifier(r'haarcascades\haarcascade_frontalface_default.xml')
face = cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

# 顔領域を赤色の矩形で囲む
for (x, y, w, h) in face:
    cv.rectangle(img, (x, y), (x + w, y+h), (0, 0, 200), 3)

print(face)
cv.imshow("test",img)
cv.waitKey(0)
cv.destroyAllWindows()


