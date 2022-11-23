# -*- coding: utf-8 -*-
import cv2
images=[]
images_x=[]
images_y=[]
images_w=[]
images_h=[]
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
        print(images_x[item])
        print(images_y[item])
        print(images_w[item])
        print(images_h[item])
        im=frame[y:y+h,x:x+w]
        images.append(im)
    if not drow_rect:
        for i in range(len(images)):
            cv2.imshow(str(i),images[i])
            drow_rect=True
    # count=False
    if cv2.waitKey(1) == ord('q'):
        break



def find_markers(image) -> list:
    """
        Функция для поиска маркировок грузов на изображении и подсчета количества цветных полос на них.

        Входные данные: изображение (bgr), прочитано cv2.imread
        Выходные данные: список из количества цветных полос на маркировках в порядке возрастания
                         на одной маркировке от 0 до 3 полос

        Примеры вывода:
            [1, 3, 3] - 3 маркировки, на одном из них 1 цветная полоса, на двух других по 3 полосы

            [2] - 1 маркировки, на нем 2 цветные полоски

            [] - маркеры не найдены или отсутствуют цветные полосы

    """
    # Алгоритм проверки будет вызывать функцию find_markers,
    # остальные функции должны вызываться из неё.

    ## TODO: Отредактируйте эту функцию по своему усмотрению.
    result = []

    return result
