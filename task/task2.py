from tkinter import *
root=Tk()
root.title('Флаг России')
l_sq=800
h_sq=800
color_flag='#da291c'
color_polos='#ffffff'
canvas=Canvas(root,width=l_sq,height=h_sq,bg=color_flag)
canvas.pack()
l_polos=5*l_sq//8
h_polos=3*h_sq//16
print(l_polos)
print(h_polos)
x0_gorizont_polos=3*l_sq//16
y0_gorizont_polos=13*h_sq//32
print(x0_gorizont_polos)
print(y0_gorizont_polos)
canvas.create_rectangle(x0_gorizont_polos,y0_gorizont_polos,x0_gorizont_polos+l_polos,y0_gorizont_polos+h_polos,fill=color_polos)
x0_vertical=13*l_sq//32
y0_vertical=3*h_sq//16
canvas.create_rectangle(x0_vertical,y0_vertical,x0_vertical+h_polos,y0_vertical+l_polos,fill=color_polos)

