# -*- coding: utf-8 -*-
import cv2
images=[]
images_x=[]
images_y=[]
images_w=[]
images_h=[]
count_item=[]
counts_conts=[]
count_conts=0
count=True
drow_rect=False
## TODO: Допишите импорт библиотек, которые собираетесь использовать
img=cv2.imread('C:/git/education_python_hw/user_task/images/4e9d2e0c-f4b0-42b6-8077-4a07f27d8170.jpg')
while count==True:
    cv2.imshow("frame",img)
    frame = cv2.resize(img, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (0,101,35),(182,255,196))
    thresh = cv2.GaussianBlur(thresh, (15, 15), 2)
    conts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    conts = conts[0]
    print(len(conts))
    if conts:
        cv2.drawContours(frame, conts, -1, (0, 255, 0), 2)
        for i in range(len(conts)):
            (x, y, w, h) = cv2.boundingRect(conts[i])
            images_x.append(x)
            images_y.append(y)
            images_w.append(w)
            images_h.append(h)
    cv2.imshow("Frame", frame)
    for item in range(len(images_x)):
        # print(images_x[item])
        # print(images_y[item])
        # print(images_w[item])
        # print(images_h[item])
        im = frame[images_y[item]:images_y[item] + images_h[item], images_x[item]:images_x[item] + images_w[item]]
        images.append(im)
    if not drow_rect:
        for i in range(len(images)):
            cv2.imshow(str(i),images[i])
            drow_rect=True

    for i in range(len(images)):
        im_item = images[i]
        im_item = cv2.cvtColor(im_item, cv2.COLOR_BGR2HSV)
        im_item = cv2.inRange(im_item, (106,95,108,),(179,255,198))
        im_item = cv2.GaussianBlur(im_item, (15, 15), 2)
        conts_items = cv2.findContours(im_item.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        conts_items = conts_items[0]
        print(len(conts_items))
        if conts_items:
            cv2.drawContours(im_item, conts_items, -1, (255, 0, 0), 2)
            for i in range(len(conts_items)):
                (x, y, w, h) = cv2.boundingRect(conts_items[i])
                count_item.append(x)
    counts_conts.append(len(count_item))
    print(counts_conts)
    count=False
    if cv2.waitKey(1) == ord('q'):
        break

