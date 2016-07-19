import tkinter
from random import choice,randint

ball_num=30
ball_min=15
ball_max=40
ball_colors=['green','blue','red','yellow','#FF00FF']
x_center=200
y_center=200
r=30

def click_ball(event):
    obj=canvas.find_closest(event.x,event.y)#номер объекта кортеж (23,)
    #print(canvas.coord(obj))
    x1,y1,x2,y2= canvas.coords(obj)
    #canvas.coords(line,0,0,event.x,event.y)
    if x1<=event.x<=x2 and y1<=event.y<=y2:
           canvas.delete(obj)
           create_rand_ball()
           
def move_ball(event):
    global x_center,y_center
    dx=event.x-x_center
    dy=event.y-y_center
    x_center=event.x
    y_center=event.y                  
    for obj in canvas.find_all():
           canvas.move(obj,dx+randint(-1,1),dy+randint(-1,1))

def create_ball(xc,yc):
    #r=randint(ball_min,ball_max)
    x=randint(xc-30,xc+30)
    y=randint(yc-15,yc+15)
    canvas.create_oval(x,y,x+2*r,y+2*r,fill="grey",outline="grey",tag="gr_ball")

def init_ball_game():
    for i in range(ball_num):
        create_ball(x_center,y_center)
        
def draw_front(begin_x,y):
    for j in range(20):
        for i in range(10):
            canvas.create_line(begin_x+10*i,y+10*j,begin_x+10*i,y+10*j+5,tag="gr_line")

def rain(event):
    rain_width=50
    draw_front(x_center-25,y_center+30)

def end_rain():
    canvas.delete("gr_line")

def init_main():
    global root, canvas,x_center,y_center
    root=tkinter.Tk()
    x_center=200
    y_center=200

    lab = tkinter.Label(root, text="Управляйте тучей с помощью мыши \n Для полива нажимайте левую кнопку мыши \n Для остановки дождя - пробел.", font="Arial 15")
    lab.pack()

    canvas=tkinter.Canvas(root,background='white',width=400,height=400)
    canvas.bind("<Motion>",move_ball)
    canvas.tag_bind("gr_ball","<Button-1>",rain)
    canvas.pack()

    button_rain=tkinter.Button(root,text="End of rain",command=end_rain)
    button_rain.pack()
    button_rain.focus_set()


if __name__=="__main__":
    init_main()
    init_ball_game()

"""def outgo(event):
     root.destroy()
 
from tkinter import *
root = Tk()
 
fra = Frame(root,width=100,height=100)
but = Button(root,text="Выход")
"""
