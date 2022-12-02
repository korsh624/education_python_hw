import cv2
cap=cv2.VideoCapture(0)
noDrive=cv2.imread("C:\Python\povorot2.png")
pedistrian=cv2.imread("C:\Python\povorot1.png")
noDrive=cv2.resize(noDrive,(64,64))
pedistrian=cv2.resize(pedistrian,(64,64))
noDrive=cv2.inRange(noDrive,(0,163,60),(255,255,255))
pedistrian=cv2.inRange(pedistrian,(0,163,60),(255,255,255))
cv2.imshow("noDrive",noDrive)
cv2.imshow("pedistrian",pedistrian)

while (True):
    ret,frame=cap.read()
    cv2.imshow("Frame",frame)
    frameCopy=frame.copy()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv=cv2.blur(hsv,(5,5))
    mask=cv2.inRange(hsv,(0,163,60),(255,255,255))
    cv2.imshow("Mask",mask)

    contours=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours=contours[0]
    if contours:
        contours=sorted(contours,key=cv2.contourArea,reverse=True)
        cv2.drawContours(frame,contours,0,(255,0,255),3)
        cv2.imshow("Contours",frame)

        (x,y,w,h)=cv2.boundingRect(contours[0])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Rect",frame)

        roLmg=frameCopy[y:y+h,x:x+w]
        cv2.imshow("Detect",roLmg)
        roLmg=cv2.resize(roLmg,(64,64))
        roLmg=cv2.inRange(roLmg,(89,124,73),(255,255,255))
        cv2.imshow("ResizedRoi",roLmg)

        noDrive_val=0
        pedistrian_val=0

        for i in range(64):
            for j in range(64):
                if roLmg[i][j]==noDrive[i][j]:
                    noDrive_val+=1
                if roLmg[i][j]==pedistrian[i][j]:
                    pedistrian_val+=1

        print(noDrive_val," ^  ",pedistrian_val)

        if pedistrian_val>2900:
            print("движение прямо или право")
        elif noDrive_val>2550:
            print("движение прямо или на лево")
        else:
            print("знак не обноружен")
                                
            
        
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyALLWindows()
        
