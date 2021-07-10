import numpy as np
import cv2

cap=cv2.VideoCapture(0)
ret1,bg=cap.read()
kernel=np.ones((5,5),np.uint8)
while True:        
        ret2,bg1=cap.read()
        #cv2.imshow("bb",bg1)
        hsv=cv2.cvtColor(bg1,cv2.COLOR_BGR2HSV)
        #cv2.imshow("INA",hsv)
        lower=(20,105,22)
        higher=(105,255,157)
        mask=cv2.inRange(hsv,lower,higher)
        #cv2.imshow("Mask",mask)
        Dilate=cv2.dilate(mask,kernel,iterations=1)
        #cv2.imshow("Dilate",Dilate)
        erode=cv2.erode(Dilate,kernel,iterations=2)
        #cv2.imshow("ERODE",erode)
        final=cv2.dilate(erode,kernel,iterations=4)
        #cv2.imshow("FInal",final)
        #To obtain the inverted image
        ret,thresh=cv2.threshold(final,90,255,cv2.THRESH_BINARY_INV)
        #cv2.imshow("Thresh",thresh)

        image=cv2.bitwise_and(bg,bg,mask=final)
        #cv2.imshow("Thresh1",image)
        image2=cv2.bitwise_and(bg1,bg1,mask=thresh)
        #cv2.imshow("Thresh2",image2)
        image3=image2+image
        cv2.imshow("Final_View",image3)
        cv2.waitKey(1)
        
        #closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
        #cv2.imshow("CLosing",closing)




