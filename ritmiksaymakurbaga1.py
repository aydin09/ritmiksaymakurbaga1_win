from tkinter import *
from tkinter import font
import pygame
from PIL import Image
import time
import random
import os

pygame.mixer.init()

pencere=Tk()
pencere.attributes("-fullscreen", 1)
pencere.tk_setPalette("white")
canvas = Canvas(pencere, height=800, width=1333)
canvas.pack()

bg_img0 = PhotoImage(file="gol.png")
bg_label0 = canvas.create_image((140,20), image=bg_img0, anchor=N+W)

bg_img2 = PhotoImage(file="gol.png")
bg_label2 = canvas.create_image((650,20), image=bg_img2, anchor=N+W)

bg_img3 = PhotoImage(file="nilufer.png")
bg_label3 = canvas.create_image((150,430), image=bg_img3, anchor=N+W)

bg_img4 = PhotoImage(file="nilufer.png")
bg_label4 = canvas.create_image((250,350), image=bg_img3, anchor=N+W)

bg_img4 = PhotoImage(file="nilufer.png")
bg_label4 = canvas.create_image((350,270), image=bg_img4, anchor=N+W)

bg_img5 = PhotoImage(file="nilufer.png")
bg_label5 = canvas.create_image((450,350), image=bg_img5, anchor=N+W)

bg_img6 = PhotoImage(file="nilufer.png")
bg_label6 = canvas.create_image((550,430), image=bg_img6, anchor=N+W)

bg_img7 = PhotoImage(file="nilufer.png")
bg_label7 = canvas.create_image((650,350), image=bg_img7, anchor=N+W)

bg_img8 = PhotoImage(file="nilufer.png")
bg_label8 = canvas.create_image((750,270), image=bg_img8, anchor=N+W)

bg_img9 = PhotoImage(file="nilufer.png")
bg_label9 = canvas.create_image((850,350), image=bg_img9, anchor=N+W)

bg_img10 = PhotoImage(file="nilufer.png")
bg_label10 = canvas.create_image((950,430), image=bg_img10, anchor=N+W)

bg_img = PhotoImage(file="kurbaga.png")
bg_label = canvas.create_image((50,350), image=bg_img, anchor=N+W)

bg_img1 = PhotoImage(file="kurbaga1.png")
bg_label1 = canvas.create_image((1170,350), image=bg_img1, anchor=N+W)

appHighlightFont = font.Font(family='TTKB Dik Temel Abece', size=12, weight='bold')
appHighlightFont1 = font.Font(family='TTKB Dik Temel Abece', size=20, weight='bold')
appHighlightFont2 = font.Font(family='TTKB Dik Temel Abece', size=60 ,weight='bold')
       
label2=Label(text="1'den 10'a kadar ritmik birer şekilde butonlara basarak tamamlayınız.",font=appHighlightFont)
label2.place(relx = 0.01, rely = 0.95)

labelkr=Label(text="Geçen süre: 0:00:00",fg="black",font=appHighlightFont1)
labelkr.place(relx = 0.70, rely = 0.73)

label=Label(text="www.egitimhane.com",font=appHighlightFont)
label.place(relx = 0.88, rely = 0.95)

xy=[["0.08","0.78"],["0.16","0.78"],["0.24","0.78"],["0.32","0.78"],["0.40","0.78"],["0.48","0.78"],["0.56","0.78"],["0.64","0.78"],["0.72","0.78"],["0.80","0.78"]]

e=[]

q=0

while q<10:
    for d in random.sample((xy),1):
        e.append(d)
        xy.remove(d)
        q+=1

        break

h=e[0][0]
t=e[0][1]

h1=e[1][0]
t1=e[1][1]

h2=e[2][0]
t2=e[2][1]

h3=e[3][0]
t3=e[3][1]

h4=e[4][0]
t4=e[4][1]

h5=e[5][0]
t5=e[5][1]

h6=e[6][0]
t6=e[6][1]

h7=e[7][0]
t7=e[7][1]

h8=e[8][0]
t8=e[8][1]

h9=e[9][0]
t9=e[9][1]

    

def aşama10():
    labelkr.destroy()
    labelkr1=Label(pencere,text="",fg="black",font=appHighlightFont1)
    labelkr1.place(relx = 0.70, rely = 0.73)
    labelkr1.config(text="Geçen süre: %d:%d%d:%d%d"%(e1,d1,c1,b1,a1),font=appHighlightFont1)
    
    canvas.move(bg_label, 185, 10)
    
    pygame.mixer.music.load("alkis.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(state="disabled",borderwidth=0)
    bes.config(state="disabled",borderwidth=0)
    alti.config(state="disabled",borderwidth=0)
    yedi.config(state="disabled",borderwidth=0)
    sekiz.config(state="disabled",borderwidth=0)
    dokuz.config(state="disabled",borderwidth=0)
    on.config(state="disabled",borderwidth=0)

def aşama9():
    canvas.move(bg_label, 100, 80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(state="disabled",borderwidth=0)
    bes.config(state="disabled",borderwidth=0)
    alti.config(state="disabled",borderwidth=0)
    yedi.config(state="disabled",borderwidth=0)
    sekiz.config(state="disabled",borderwidth=0)
    dokuz.config(state="disabled",borderwidth=0)
    on.config(command=aşama10,borderwidth=0)

def aşama8():
    canvas.move(bg_label, 100, 80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(state="disabled",borderwidth=0)
    bes.config(state="disabled",borderwidth=0)
    alti.config(state="disabled",borderwidth=0)
    yedi.config(state="disabled",borderwidth=0)
    sekiz.config(state="disabled",borderwidth=0)
    dokuz.config(command=aşama9,borderwidth=0)

def aşama7():
    canvas.move(bg_label, 100, -80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(state="disabled",borderwidth=0)
    bes.config(state="disabled",borderwidth=0)
    alti.config(state="disabled",borderwidth=0)
    yedi.config(state="disabled",borderwidth=0)
    sekiz.config(command=aşama8,borderwidth=0)

def aşama6():
    canvas.move(bg_label, 100, -80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(state="disabled",borderwidth=0)
    bes.config(state="disabled",borderwidth=0)
    alti.config(state="disabled",borderwidth=0)
    yedi.config(command=aşama7,borderwidth=0)

def aşama5():
    canvas.move(bg_label, 100, 80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(state="disabled",borderwidth=0)
    bes.config(state="disabled",borderwidth=0)
    alti.config(command=aşama6,borderwidth=0)
    
def aşama4():
    canvas.move(bg_label, 105, 80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(state="disabled",borderwidth=0)
    bes.config(command=aşama5,borderwidth=0)
   
def aşama3():
    canvas.move(bg_label, 100, -80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(state="disabled",borderwidth=0)
    dort.config(command=aşama4,borderwidth=0)

def aşama2():    
    canvas.move(bg_label, 110, -80)
    
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(state="disabled",borderwidth=0)
    uc.config(command=aşama3,borderwidth=0)
   
def aşama1():
    canvas.move(bg_label, 128, 60)
   
    pygame.mixer.music.load("kurbaga.ogg")
    pygame.mixer.music.play()
    
    bir.config(state="disabled",borderwidth=0)
    iki.config(command=aşama2,borderwidth=0)

    try:
        global a1,b1,c1,d1,e1
    
        b1=0
        a1=0
        c1=0
        d1=0
        e1=0
        
        while True:
            labelkr.config(text="Geçen süre: %d:%d%d:%d%d"%(e1,d1,c1,b1,a1),font=appHighlightFont1)
            a1+=1
            time.sleep(0.01)
            bir.update()    
            if a1==9:
                b1+=1
                a1=0
                if b1>5:
                    c1+=1
                    b1=0
                    if c1>9:
                        d1+=1
                        c1=0
                        if d1>5:
                            e1+=1
                            d1=0
                            if e1>59:
                                b1=0
                                a1=0
                                c1=0
                                d1=0
                                e1=0
                                
                                
            
    except:
        None

def yenile():
    pencere.destroy()
    os.startfile("ritmiksaymakurbaga1.exe")

bir_buton = PhotoImage(file = "bir.png")
iki_buton = PhotoImage(file = "iki.png")
uc_buton = PhotoImage(file = "uc.png")
dort_buton = PhotoImage(file = "dort.png")
bes_buton = PhotoImage(file = "bes.png")
alti_buton = PhotoImage(file = "alti.png")
yedi_buton = PhotoImage(file = "yedi.png")
sekiz_buton = PhotoImage(file = "sekiz.png")
dokuz_buton = PhotoImage(file = "dokuz.png")
on_buton = PhotoImage(file = "on.png")

bir = Button()
bir.config(image=bir_buton, command=aşama1,borderwidth=0)
bir.place(relx = h , rely = t)

iki = Button()
iki.config(image=iki_buton,borderwidth=0)
iki.place(relx = h1, rely = t1)

uc = Button()
uc.config(image=uc_buton,borderwidth=0)
uc.place(relx = h2 , rely = t2)

dort = Button()
dort.config(image=dort_buton,borderwidth=0)
dort.place(relx = h3, rely = t3)

bes = Button()
bes.config(image=bes_buton,borderwidth=0)
bes.place(relx = h4 , rely = t4)

alti = Button()
alti.config(image=alti_buton,borderwidth=0)
alti.place(relx = h5, rely = t5)

yedi = Button()
yedi.config(image=yedi_buton,borderwidth=0)
yedi.place(relx = h6 , rely = t6)

sekiz = Button()
sekiz.config(image=sekiz_buton,borderwidth=0)
sekiz.place(relx = h7, rely = t7)

dokuz = Button()
dokuz.config(image=dokuz_buton,borderwidth=0)
dokuz.place(relx = h8 , rely = t8)

on = Button()
on.config(image=on_buton,borderwidth=0)
on.place(relx = h9, rely = t9)

yeni = PhotoImage(file="yenile.png")

buton=Button()
buton.config(text="YENİLE",image=yeni,compound="top",command=yenile,width='40',fg="white",bg="green",font=appHighlightFont)
buton.place(relx = 0.78, rely = 0.90)

cikis = PhotoImage(file="cikis.png")

buton=Button()
buton.config(text="ÇIKIŞ",image=cikis,compound="top",command=pencere.destroy,width='40',fg="white",bg="red",font=appHighlightFont)
buton.place(relx = 0.83, rely = 0.90)
      
pencere.mainloop()
