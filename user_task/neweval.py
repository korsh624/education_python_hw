import cv2
import time
import findxywh
mask_min=0,101,35
mask_max=182,255,196
mask_min_item=106,95,108
mask_max_item=179,255,198
points=[]
draw=False
img=cv2.imread('C:/git/education_python_hw/user_task/images/4e9d2e0c-f4b0-42b6-8077-4a07f27d8170.jpg')
images=findxywh.findxywh(img,mask_min,mask_max)
print('Количество квадратиков',len(images))
for i in range(len(images)):
    cv2.imshow(str(i),images[i])
    point=findxywh.findxywh(images[i], mask_min_item, mask_max_item)
    points.append(len(point))
    time.sleep(1)
print(points)
input()






