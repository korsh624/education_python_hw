# -*- coding: utf-8 -*-
import cv2
import time
from user_task import fingsqer
draw=False

im=[]
## TODO: Допишите импорт библиотек, которые собираетесь использовать
img=cv2.imread('C:/git/education_python_hw/user_task/images/4e9d2e0c-f4b0-42b6-8077-4a07f27d8170.jpg')
while True:
    cv2.imshow('img',img)
    im=fingsqer.findimages(img)

    if not draw:
        for i in range(len(im)):
            cv2.imshow(str(i),im[i])
        draw=True
    time.sleep(1)
    print('findet')




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
