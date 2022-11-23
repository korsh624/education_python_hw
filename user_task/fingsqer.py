import cv2

def findimages(frame):
    images = []
    images_x = []
    images_y = []
    images_w = []
    images_h = []
    drow_rect=False
    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (0, 101, 35), (182, 255, 196))
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
        im = frame[images_y[item]:images_y[item] + images_h[item], images_x[item]:images_x[item] + images_w[item]]
        images.append(im)
    if not drow_rect:
        for i in range(len(images)):
            cv2.imshow(str(i), images[i])
            drow_rect = True
    return images



