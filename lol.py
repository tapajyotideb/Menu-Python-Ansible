import cv2
import subprocess as sp

x = sp.getoutput('ls /dev/ | grep video')
dev = int(x[-1])
cap = cv2.VideoCapture(dev)
ret, photo = cap.read()
#x = sp.getoutput("date +%s")
cv2.imwrite('/root/Desktop/photo.png', photo)
cap.release()
