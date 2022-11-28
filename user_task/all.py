import cv2
import time
mask_min=0,101,35
mask_max=182,255,196
mask_min_item=106,95,108
mask_max_item=179,255,198
points=[]
draw=False
images=[]

while True:
    img=cv2.imread('C:/git/education_python_hw/user_task/images/4e9d2e0c-f4b0-42b6-8077-4a07f27d8170.jpg')
    frame=findxywh.findxywh(img,mask_min,mask_max)
    print('Количество квадратиков',len(frame))
    for i in range(len(frame)):
        if not draw:
            cv2.imshow(str(i),frame[i])
        point=findxywh(frame[i], mask_min_item, mask_max_item)
        points.append(len(point))
    draw=True
    print(points)


def findxywh(img,mask_min,mask_max):
    images = []
    images_x = []
    images_y = []
    images_w = []
    images_h = []

    cv2.imshow("frame",img)
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
            im = frame[images_y[item]:images_y[item] + images_h[item], images_x[item]:images_x[item] + images_w[item]]
            images.append(im)
    return images






