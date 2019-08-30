import cv2
import os

path0 = './img'
imglist = os.listdir('./img')
for path in imglist:
    path = os.path.join(path0, path)
    img = cv2.imread(path)
    img = cv2.resize(img, (1024, 512))
    cv2.imwrite(path, img)
