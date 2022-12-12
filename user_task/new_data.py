# -*- coding: utf-8 -*-
import cv2
import numpy as np
images=[]
images_x=[]
images_y=[]
images_w=[]
images_h=[]
mask_min=0,101,35
mask_max=182,255,196
# (106,95,108,),(179,255,198)
def findxywh(img,mask_min,mask_max):
    frame = cv2.resize(img, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (mask_min),(mask_max))
    thresh = cv2.GaussianBlur(thresh, (15, 15), 2)
    conts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    conts = conts[0]
    print(len(conts))
    if conts:
        cv2.drawContours(frame, conts, -1, (255,0, 0), 2)
        for i in range(len(conts)):
            (x, y, w, h) = cv2.boundingRect(conts[i])
            print((x,' ', y,' ', w,' ', h))
            images_x.append(x)
            images_y.append(y)
            images_w.append(w)
            images_h.append(h)
        for item in range(len(images_x)):
            # print(images_x[item])
            # print(images_y[item])
            # print(images_w[item])
            # print(images_h[item])
            rect_px=20
            im = frame[images_y[item]+rect_px:images_y[item] + images_h[item]-rect_px, images_x[item]+rect_px:images_x[item] + images_w[item]-rect_px]
            images.append(im)
    return images
img=cv2.imread('C:/git/education_python_hw/user_task/images/4e9d2e0c-f4b0-42b6-8077-4a07f27d8170.jpg')
pictur=findxywh(img,mask_min,mask_max)
# green=48,160,129
# red=23,8,179
# blue=138,91,70
print(len(pictur))
for i in range(len(pictur)):
    hsv=cv2.cvtColor(pictur[i],cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (15, 15), 2)
    thresh = cv2.inRange(hsv, (47,159,128),(49,161,130))
    contours=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    if contours:
        print('green')
        contours=contours[0]
        sorted(contours, key=cv2.contourArea,reverse=True)
        cv2.drawContours(pictur[i],contours,-1,(255,0,0),3)    
        # (x,y,w,h)=cv2.boundingRect(contours[0])
        # cv2.rectangle(pictur[i],(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow(str(i),pictur[i])


cv2.waitKey(0)
