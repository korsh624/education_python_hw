from tkinter import *
root=Tk()
root.title('Флаг России')
canvas=Canvas(root,width=240,height=160,bg='white')
canvas.pack()
# -------- параметры ---------
(xs,ys)=(30,20); d=60; w=2*d
# ----------------------------
canvas.create_rectangle(xs,ys,xs+d,ys+w,fill='#007a33')
xs=xs+d
canvas.create_rectangle(xs,ys,xs+d,ys+w,fill='#ffffff')
xs=xs+d
canvas.create_rectangle(xs,ys,xs+d,ys+w,fill='#cb333b')


