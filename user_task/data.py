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
            rect_fr=10
            im = frame[images_y[item]+rect_fr:images_y[item] + images_h[item]-rect_fr, images_x[item]+rect_fr:images_x[item] + images_w[item]-rect_fr]
            images.append(im)
    return images
img=cv2.imread('C:/git/education_python_hw/user_task/images/4e9d2e0c-f4b0-42b6-8077-4a07f27d8170.jpg')
pictur=findxywh(img,mask_min,mask_max)
# for i in range(len(pictur)):
#     cv2.imshow(str(i),pictur[i])
item_pictur=[]
# cv2.imshow('w',pictur[0])
mask_min_item=[(118,158,162),(52,182,204),(189,250,223)]
mask_max_item=[(101,87,94),(36,109,153),(170,184,180)]
hsv_item = cv2.cvtColor(pictur[0], cv2.COLOR_BGR2HSV)
hsv_item=cv2.GaussianBlur(hsv_item, (15, 15), 2)
thresh_item = cv2.inRange(hsv_item, mask_min_item[1], mask_max_item[1])
contours0_item, hierarchy = cv2.findContours(thresh_item.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow('filter', thresh_item)
for cnt in contours0_item:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    # print(box)
    print(len(box))
    box = np.int0(box)
    cv2.drawContours(img, [box], -1, (255, 0, 0), 0)
def getcontours(img):
    imgContour=img.copy()
    contours,mierchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if contours:
        for cnt in contours:
            area=cv2.contourArea(cnt)
            print(area)
            if area>500:
                cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
                per1=cv2.arcLength(cnt,True)
                approx=cv2.applyColorMap(cnt,0.02*per1,True)
                print(len(approx))
                objCor=len(approx)
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.imshow('cont',imgContour)
                if objCor==4:
                    print(objCor)
                    return


cv2.imshow("frame",img)
cv2.imshow('contours', pictur[0])
img_gray=cv2.cvtColor(pictur[0],cv2.COLOR_BGR2GRAY)
img_gray=cv2.resize(img_gray,(640, 480))
img_blur=cv2.GaussianBlur(img_gray,(3,3),1)
imgCanny=cv2.Canny(img_blur,10,10)
cv2.imshow("cany",imgCanny)
angle_4=getcontours(imgCanny)
print(angle_4)

cv2.waitKey(0)
