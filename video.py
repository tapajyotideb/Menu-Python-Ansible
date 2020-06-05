import cv2
import subprocess as sp

x = sp.getoutput('ls /dev/ | grep video')
dev = int(x[-1])
cap = cv2.VideoCapture(dev)

while True:
    ret, photo = cap.read()
    fphoto = photo[150:250, 250:350]
    photo[0:100, 0:100] = fphoto
    cv2.imshow("frame", photo)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
cap.release()
