import tkinter
from random import choice,randint


ball_num=30
is_rain=False
x_center=200
y_center=200
r=30
win_width=600
win_height=400
timer_delay = 400


class Mushrooms:
    up_colors=['black','brown','red']
    height=30
    x_mush=randint(10,win_width-10)
    y_mush=win_height-height-10
    _dh=2

    def __init__(self):
        fillcolor = choice(Mushrooms.up_colors)
        _dh=1

        #ножка
        self._avatar2=canvas.create_oval(Mushrooms.x_mush-3*Mushrooms.height//8,Mushrooms.y_mush+Mushrooms.height//4,
                                      Mushrooms.x_mush+3*Mushrooms.height//8,win_height-7,
                                      fill="white",outline="white")   
        #шляпка
        self._avatar1=canvas.create_arc(Mushrooms.x_mush-Mushrooms.height//2,Mushrooms.y_mush,
                                      Mushrooms.x_mush+Mushrooms.height//2,Mushrooms.y_mush+2*Mushrooms.height//3,
                                      start=0,extent=180,fill=fillcolor,outline=fillcolor)
    def grow(self):
        if Mushrooms.height<59:
            Mushrooms.height += self._dh
            Mushrooms.y_mush-=self._dh
            #ножка
            canvas.coords(self._avatar2,Mushrooms.x_mush-3*Mushrooms.height//8,Mushrooms.y_mush+Mushrooms.height//4,
                                          Mushrooms.x_mush+3*Mushrooms.height//8,win_height-3)
            #шляпка
            canvas.coords(self._avatar1,Mushrooms.x_mush-Mushrooms.height//2,Mushrooms.y_mush,
                                          Mushrooms.x_mush+Mushrooms.height//2,Mushrooms.y_mush+2*Mushrooms.height//3)
        else:
            self.mush_destroy()

    def mush_destroy(self):
        canvas.delete(self._avatar1)
        canvas.delete(self._avatar2)
        
def move_ball(event):
    global x_center,y_center
    dx=event.x-x_center
    dy=event.y-y_center
    x_center=event.x
    y_center=event.y                  
    
    for obj in canvas.find_withtag( "gr_ball"):#движение тучи
        canvas.move(obj,dx+randint(-1,1),dy+randint(-1,1))
    for obj in canvas.find_withtag( "gr_line"):# движение капель
        canvas.move(obj,dx+randint(-1,1),dy+randint(-1,1))

def create_ball(xc,yc):
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
    global is_rain
    is_rain=True
    draw_front(x_center-25,y_center+35)

def end_rain():
    global is_rain
    canvas.delete("gr_line")
    is_rain=False

def init_main():
    global root, canvas,x_center,y_center,m1
    root=tkinter.Tk()
    x_center=200
    y_center=100

    lab = tkinter.Label(root, text="Управляйте тучей с помощью мыши \n Для полива нажимайте левую кнопку мыши \n Для остановки дождя - пробел,\n Гриб растет под дождем, переросший - пропадает",
                        font="Arial 15")
    lab.pack()

    
    canvas=tkinter.Canvas(root,background='lightblue',width=win_width,height=win_height)
    canvas.bind("<Motion>",move_ball)
    canvas.tag_bind("gr_ball","<Button-1>",rain)
    canvas.pack()

    canvas.create_rectangle(0,win_height-60,win_width,win_height,fill='darkgreen', outline="darkgreen")
    canvas.pack()
    
    m1=Mushrooms()
    
    button_rain=tkinter.Button(root,text="End of rain",command=end_rain)
    button_rain.pack()
    button_rain.focus_set()

def timer_event():
    # все периодические рассчёты, которые я хочу, делаю здесь

    if is_rain==True and x_center-25<m1.x_mush and x_center+25>m1.x_mush:
        m1.grow()
    
    canvas.after(timer_delay, timer_event)

if __name__=="__main__":
    init_main()
    init_ball_game()
    timer_event()

"""def outgo(event):
     root.destroy()
 
from tkinter import *
root = Tk()
 
fra = Frame(root,width=100,height=100)
but = Button(root,text="Выход")
"""
