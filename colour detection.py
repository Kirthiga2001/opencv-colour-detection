import cv2
import  numpy as np
def empty(a):
    pass
p="car.jpg"
cv2.namedWindow("Tracer")
cv2.resizeWindow("Tracer",640,240)
cv2.createTrackbar("Hue Min","Tracer",0,179,empty)
cv2.createTrackbar("Hue Max","Tracer",179,179,empty)
cv2.createTrackbar("Sat Min","Tracer",137,255,empty)
cv2.createTrackbar("Sat Max","Tracer",255,255,empty)
cv2.createTrackbar("Val Min","Tracer",154,255,empty)
cv2.createTrackbar("Val Max","Tracer",255,255,empty)

while 1:
        i=cv2.imread(p)
        ihsv=cv2.cvtColor(i,cv2.COLOR_BGR2HSV)
        hmin=cv2.getTrackbarPos("Hue Min","Tracer")
        hmax = cv2.getTrackbarPos("Hue Max", "Tracer")
        smin = cv2.getTrackbarPos("Sat Min", "Tracer")
        smax = cv2.getTrackbarPos("Sat Max", "Tracer")
        vmin = cv2.getTrackbarPos("Val Min", "Tracer")
        vmax = cv2.getTrackbarPos("Val Max", "Tracer")
        print(hmin,hmax,smax,smin,vmax,vmin)
        l=np.array([hmin,smin,vmin])
        u=np.array([hmax,smax,vmax])
        mask=cv2.inRange(ihsv,l,u)

        ir=cv2.bitwise_and(i,i,mask=mask)

        i=cv2.resize(i,(150,150))
        i = cv2.resize(i, (150, 150))
        ihsv = cv2.resize(ihsv, (150, 150))
        mask = cv2.resize(mask, (150, 150))
        ir = cv2.resize(ir, (150, 150))


        #.imshow("full",h)
        cv2.imshow("ori",i)
        cv2.imshow("hsv", ihsv)
        cv2.imshow("mask", mask)
        cv2.imshow("result", ir)
        cv2.waitKey(1)