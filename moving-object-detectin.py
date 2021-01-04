import cv2
from playsound import playsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    _,frame1 = cam.read()
    _,frame2 = cam.read()
    abs = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(abs,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    _,thres = cv2.threshold(blur,50,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thres,None,iterations=3)
    contor,hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in contor:
        area = cv2.contourArea(c)
        if(area>5000):
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x,y),(x+w,y+h), (0,0,255),5)
            playsound("/home/siva/mpw/objecttraking/beep.mp3")
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("video",frame1)
