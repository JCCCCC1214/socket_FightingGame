import pygame
import socket
import tkinter as tk
import threading
from tkinter import ttk
from socket import*
# from PIL import Image, ImageTk
from tkinter import *
window = tk.Tk()
ID = ""
password = ""
def complete_login():
    global ID,password,window
    ID = e1.get()
    window.destroy()


window.title('設定ID和密碼')
window.geometry('300x180')
window.configure(background='white')
l1 = tk.Label(window, text = "ID",font=('Arial', 10),bg = "gray", width = 12, height = 2 )
l1.place(x=10,y=20)
e1 = tk.Entry(window, show=None,width = 20)   
e1.place(x=130,y=30)
b1 = tk.Button(window, text='完成', font=('Arial', 12), width=10, height=1,command = complete_login)
b1.place(x=100,y=130)
window.mainloop()

 

pygame.init()
win = pygame.display.set_mode((1100,600))
pygame.display.set_caption("First Game")
bg = pygame.image.load('gg.PNG')
bg1 = pygame.image.load('login.PNG')
wait1 = pygame.image.load('wait1.PNG')
wait2 = pygame.image.load('wait2.PNG')
wait3 = pygame.image.load('wait3.PNG')
wait4 = pygame.image.load('wait4.PNG')
clock = pygame.time.Clock()



clientSocket = socket(AF_INET,SOCK_STREAM)  
clientSocket.connect(('140.115.213.23',12000))
reponse = clientSocket.recv(1024)
threadnumber = reponse.decode()

my_font = pygame.font.SysFont("mnjzbh.ttf", 100)
name_font = pygame.font.SysFont("mnjzbh.ttf", 30)
text_login = my_font.render("start", 1,"white")
rec_login = text_login.get_rect()
rec_login.center = (550,300)







if(threadnumber == "1"):
    x = 0
    y = 500
    ex = 1000
    ey = 500
    temp_direction1 = "Right"
    temp_direction2 = "Left"
 
elif(threadnumber == "0"):
    x=1000
    y = 500
    ex = 0
    ey = 500
    temp_direction1 = "Left"
    temp_direction2 = "Right"

stayRight =[pygame.image.load('8.png'),pygame.image.load('9.png'),pygame.image.load('10.png'),pygame.image.load('12.png'),pygame.image.load('13.png'),pygame.image.load('14.png'),pygame.image.load('15.png')]
stayLeft =[pygame.image.load('a.png'),pygame.image.load('b.png'),pygame.image.load('c.png'),pygame.image.load('e.png'),pygame.image.load('f.png'),pygame.image.load('g.png'),pygame.image.load('h.png')]
walkLeft= [pygame.image.load('bhl1.png'),pygame.image.load('bhl2.png'),pygame.image.load('bhl3.png'),pygame.image.load('bhl4.png'),pygame.image.load('bhl5.png'),pygame.image.load('bhl6.png')]
walkRight = [pygame.image.load('bhr1.png'),pygame.image.load('bhr2.png'),pygame.image.load('bhr3.png'),pygame.image.load('bhr4.png'),pygame.image.load('bhr5.png'),pygame.image.load('bhr6.png')]
jumpRight = [pygame.image.load('j1.png'),pygame.image.load('j2.png'),pygame.image.load('j3.png'),pygame.image.load('j4.png'),pygame.image.load('j5.png'),pygame.image.load('j6.png')]
atk_one_Right = [pygame.image.load('atk1r.png'),pygame.image.load('atk2r.png'),pygame.image.load('atk3r.png'),pygame.image.load('atk4r.png'),pygame.image.load('atk5r.png'),pygame.image.load('atk6r.png'),pygame.image.load('atk7r.png'),pygame.image.load('atk8r.png'),pygame.image.load('atk9r.png'),pygame.image.load('atk10r.png'),pygame.image.load('atk11r.png'),pygame.image.load('atk12r.png'),pygame.image.load('atk13r.png')]
atk_one_Left = [pygame.image.load('atk1l.png'),pygame.image.load('atk2l.png'),pygame.image.load('atk3l.png'),pygame.image.load('atk4l.png'),pygame.image.load('atk5l.png'),pygame.image.load('atk6l.png'),pygame.image.load('atk7l.png'),pygame.image.load('atk8l.png'),pygame.image.load('atk9l.png'),pygame.image.load('atk10l.png'),pygame.image.load('atk11l.png'),pygame.image.load('atk12l.png'),pygame.image.load('atk13l.png')]
atk_two_Right = [pygame.image.load('qr1.png'),pygame.image.load('qr2.png'),pygame.image.load('qr3.png'),pygame.image.load('qr4.png'),pygame.image.load('qr5.png'),pygame.image.load('qr6.png'),pygame.image.load('qr7.png')]
atk_two_Left = [pygame.image.load('ql1.png'),pygame.image.load('ql2.png'),pygame.image.load('ql3.png'),pygame.image.load('ql4.png'),pygame.image.load('ql5.png'),pygame.image.load('ql6.png'),pygame.image.load('ql7.png')]
atk_w_Right = [pygame.image.load('w1.png'),pygame.image.load('w2.png'),pygame.image.load('w3.png'),pygame.image.load('w4.png'),pygame.image.load('w5.png'),pygame.image.load('w6.png'),pygame.image.load('w7.png'),pygame.image.load('w8.png'),pygame.image.load('w9.png'),pygame.image.load('f1.png'),pygame.image.load('f2.png'),pygame.image.load('f3.png'),pygame.image.load('f4.png'),pygame.image.load('f5.png'),pygame.image.load('w10.png'),pygame.image.load('w11.png'),pygame.image.load('w12.png'),pygame.image.load('w13.png'),pygame.image.load('w14.png'),pygame.image.load('w15.png'),pygame.image.load('w16.png')]
atk_w_Left = [pygame.image.load('w1.png'),pygame.image.load('w2.png'),pygame.image.load('w3.png'),pygame.image.load('w4.png'),pygame.image.load('w5.png'),pygame.image.load('w6.png'),pygame.image.load('w7.png'),pygame.image.load('w8.png'),pygame.image.load('w9.png'),pygame.image.load('f1.png'),pygame.image.load('f2.png'),pygame.image.load('f3.png'),pygame.image.load('f4.png'),pygame.image.load('f5.png'),pygame.image.load('w10l.png'),pygame.image.load('w11l.png'),pygame.image.load('w12l.png'),pygame.image.load('w13l.png'),pygame.image.load('w14l.png'),pygame.image.load('w15l.png'),pygame.image.load('w16l.png')]
atk_e_Left = [pygame.image.load('w10l.png'),pygame.image.load('w11l.png'),pygame.image.load('w12l.png'),pygame.image.load('w13l.png'),pygame.image.load('w14l.png'),pygame.image.load('w15l.png'),pygame.image.load('w16l.png')]
atk_e_Right = [pygame.image.load('w10.png'),pygame.image.load('w11.png'),pygame.image.load('w12.png'),pygame.image.load('w13.png'),pygame.image.load('w14.png'),pygame.image.load('w15.png'),pygame.image.load('w16.png')]
atk_efly_Right = [pygame.image.load('er1.png'),pygame.image.load('er2.png'),pygame.image.load('er3.png'),pygame.image.load('er4.png'),pygame.image.load('er5.png')]
atk_efly_Left = [pygame.image.load('el1.png'),pygame.image.load('el2.png'),pygame.image.load('el3.png'),pygame.image.load('el4.png'),pygame.image.load('el5.png')]
hit = [pygame.image.load('hit1.png'),pygame.image.load('hit2.png'),pygame.image.load('hit3.png'),pygame.image.load('hit4.png'),pygame.image.load('hit5.png')]
wrstay = [pygame.image.load('atk2r.png')]
wlstay = [pygame.image.load('atk2l.png')]
defenser = pygame.image.load('defenser.png')
defensel = pygame.image.load('defensel.png')
shield = pygame.image.load('shield.png')

width = 64
height = 64
vel = 10
isJump = False
jumpCount = 8
left = False
right = False
walkCount = 0
stayCount = 0
image_XY = []
stayCounte = 0
jrate = 0
enmey_anim = []
fly_anim = []
allready = False
state = ""
waitcount = 0
name12 = []
skills = False
Q_skill = False
Q_count = 0
Q_count2 = 0
Q_atk = 0
p1_blood = 200
p2_blood = 200
winname = ""
W_skill = False
W_count = 0
wflag = False
w_locate = 0
wf_locate = 0
E_skill = False
E_count = 0
E_flag = False
Eatkx = 0
Eatky = 0
E_direction = ""
E_flycount = 0
enemy_hit_flag = False 
enemy_hit_count = 0
self_hit_flag = False
self_hit_count = 0
self_defense_flag = False
enemy_defense_flag = False
bye_flag = False

def handle():
    global ex,ey,image_XY,state,threadnumber,p1_blood,p2_blood,self_hit_flag,self_defense_flag
    while True: 
        try:
            temp = clientSocket.recv(1024).decode()
            print(temp)
            image_XY = temp.split()
            if(temp[0]!="l" and temp[0]!="r" and temp[0]!="j" and temp[0]!='q' and temp[0]!="b" and temp[0]!='w' and temp[0]!='e' and image_XY[0]!="eflyr" and image_XY[0]!="eflyl" and temp[0]!='Q' and temp[0]!='d'):
                state = temp
            elif(temp[0]=="b"):
                self_hit_flag = True
                image_XY = temp.split()
                if(threadnumber=="1"):
                    if(self_defense_flag == False):
                        p1_blood -= float(image_XY[1])
                    else:
                        p1_blood -= float(image_XY[1])/2
                elif(threadnumber=="0"):
                    if(self_defense_flag == False):
                        p2_blood -= float(image_XY[1])
                    else:
                        p2_blood -= float(image_XY[1])/2
            elif(image_XY[0] == "eflyr" or image_XY[0] == "eflyl"):
                image_XY = temp.split()
                fly_anim.append(image_XY)
            else:
                image_XY = temp.split()
                enmey_anim.append(image_XY)

        except:
            pass       
thread1=threading.Thread(target=handle)
thread1.start()






def redrawGameWindow(temp_direction1):
    global walkCount,ex,ey,enmey_anim,char,stayCount,stayCounte,jrate,temp_direction2,name12,p1_blood,p2_blood,W_count,wflag,x,y,w_locate,wf_locate,E_flycount,E_flag,Eatkx,Eatky,enemy_hit_flag,enemy_hit_count,self_hit_count,self_hit_flag,Q_atk,enemy_defense_flag
    win.blit(bg, (0,0))
    if walkCount + 1 >= 12:
        walkCount = 0
    if stayCount + 1 >= 21:
        stayCount = 0
    if stayCounte +1 >=21:
        stayCounte = 0
    if E_flycount + 1 >= 15:
        E_flycount = 0

    if(len(enmey_anim)==0):
        enemy_defense_flag = False
        if(temp_direction2 == "Left"):
            win.blit(stayLeft[stayCounte//3], (ex,ey))
        elif(temp_direction2 == "Right"):
            win.blit(stayRight[stayCounte//3], (ex,ey))
        stayCounte +=1
    else:
        new_anim = enmey_anim[0]
        #敵人人物
        if(new_anim[0]=='d'):
            enemy_defense_flag = True
            if(temp_direction2 == "Left"):
                win.blit(shield, (float(new_anim[1])-35,float(new_anim[2])-30))
                win.blit(defensel, (float(new_anim[1]),float(new_anim[2])+10))
            elif(temp_direction2 == "Right"):
                win.blit(shield, (float(new_anim[1])-40,float(new_anim[2])-30))
                win.blit(defenser, (float(new_anim[1])-20,float(new_anim[2])+10))
                
        elif(new_anim[0]=='e'):
            enemy_defense_flag = False
            if(temp_direction2 == "Left"):
                win.blit(atk_e_Left[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
            elif(temp_direction2 == "Right"):
                win.blit(atk_e_Right[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
        elif(new_anim[0]=='w'):
            enemy_defense_flag = False
            if(temp_direction2 == "Left"):
                if(int(new_anim[3])<=8):
                    win.blit(wlstay[0], (float(new_anim[1])+30,float(new_anim[2])-30))
                if(int(new_anim[3])>=14):
                    ex = float(new_anim[1])
                    ey = float(new_anim[2])
                win.blit(atk_w_Left[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
            elif(temp_direction2 == "Right"):
                if(int(new_anim[3])<=8):
                    win.blit(wrstay[0], (float(new_anim[1])+30,float(new_anim[2])-30))
                if(int(new_anim[3])>=14):
                    ex = float(new_anim[1])
                    ey = float(new_anim[2])
                win.blit(atk_w_Right[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
        elif(new_anim[0]=='Q'):
            enemy_defense_flag = False
            if(temp_direction2 == "Left"):
                win.blit(atk_two_Left[int(new_anim[3])], (float(new_anim[1])-int(atk_two_Left[int(new_anim[3])].get_width())+75,float(new_anim[2])))
            elif(temp_direction2 == "Right"):
                win.blit(atk_two_Right[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
        elif(new_anim[0]=='q'):
            enemy_defense_flag = False
            if(temp_direction2 == "Left"):
                win.blit(atk_one_Left[int(new_anim[3])], (float(new_anim[1])-int(atk_one_Left[int(new_anim[3])].get_width())+75,float(new_anim[2])))
            elif(temp_direction2 == "Right"):
                win.blit(atk_one_Right[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
        elif(new_anim[0]=='j'):
            enemy_defense_flag = False
            win.blit(jumpRight[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
            ex = float(new_anim[1])
            ey = float(new_anim[2])
        elif(new_anim[0]=='l'):
            enemy_defense_flag = False
            win.blit(walkLeft[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
            ex = float(new_anim[1])
            ey = float(new_anim[2])
            temp_direction2 = "Left"
        elif(new_anim[0]=='r'):
            enemy_defense_flag = False
            win.blit(walkRight[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
            ex = float(new_anim[1])
            ey = float(new_anim[2])
            temp_direction2 = "Right"
        enmey_anim[0:0+1] = []




    

    

    if Q_skill:
        if(Q_atk == 0):                   
            if(temp_direction1 == "Left"):
                win.blit(atk_one_Left[Q_count], (x-int(atk_one_Left[Q_count].get_width())+75,y))
                sword_left = x-int(atk_one_Left[Q_count].get_width())+75
                sword_right = x
                if((ex<=sword_right and ex>=sword_left) or (ex+75<=sword_right and ex+75>=sword_left) or(ex+75>=sword_right and ex<=sword_left)):
                    if(ey>=450 and Q_count==2):
                        enemy_hit_flag = True
                        if(threadnumber == "1"):
                            if(enemy_defense_flag == True):
                                p2_blood -= 5.0
                            else:
                                p2_blood -= 10.0
                        else:
                            if(enemy_defense_flag == True):
                                p1_blood -= 5.0
                            else:
                                p1_blood -= 10.0
                        text = "b"+" "+"10"+" "+"1"+" "+"1"+" "
                        clientSocket.send(str.encode(text))
            elif(temp_direction1 == "Right"):
                win.blit(atk_one_Right[Q_count], (x,y))
                sword_left = x+75
                sword_right = x+int(atk_one_Left[Q_count].get_width())
                if((ex<=sword_right and ex>=sword_left) or (ex+75<=sword_right and ex+75>=sword_left)or(ex+75>=sword_right and ex<=sword_left)):
                    if(ey>=450 and Q_count==2):
                        enemy_hit_flag = True
                        if(threadnumber == "1"):
                            if(enemy_defense_flag == True):
                                p2_blood -= 5.0
                            else:
                                p2_blood -= 10.0
                        else:
                            if(enemy_defense_flag == True):
                                p1_blood -= 5.0
                            else:
                                p1_blood -= 10.0
                        text = "b"+" "+"10"+" "+"1"+" "+"1"+" "
                        clientSocket.send(str.encode(text))
            text = "q"+" "+str(x)+" "+str(y)+" "+str(Q_count)+" "
            clientSocket.send(str.encode(text))

        
        elif(Q_atk == 1):   
            if(temp_direction1 == "Left"):
                win.blit(atk_two_Left[Q_count2//2], (x-int(atk_two_Left[Q_count2//2].get_width())+75,y))
                sword_left = x-int(atk_two_Left[Q_count2//2].get_width())+75
                sword_right = x
                if((ex<=sword_right and ex>=sword_left) or (ex+75<=sword_right and ex+75>=sword_left) or(ex+75>=sword_right and ex<=sword_left)):
                    if(ey>=450 and Q_count2//2==2):
                        enemy_hit_flag = True
                        if(threadnumber == "1"):
                            if(enemy_defense_flag == True):
                                p2_blood -= 5.0
                            else:
                                p2_blood -= 10.0
                        else:
                            if(enemy_defense_flag == True):
                                p1_blood -= 5.0
                            else:
                                p1_blood -= 10.0
                        text = "b"+" "+"10"+" "+"1"+" "+"1"+" "
                        clientSocket.send(str.encode(text))
            elif(temp_direction1 == "Right"):
                win.blit(atk_two_Right[Q_count2//2], (x,y))
                sword_left = x+75
                sword_right = x+int(atk_two_Left[Q_count2//2].get_width())
                if((ex<=sword_right and ex>=sword_left) or (ex+75<=sword_right and ex+75>=sword_left)or(ex+75>=sword_right and ex<=sword_left)):
                    if(ey>=450 and Q_count2//2==2):
                        enemy_hit_flag = True
                        if(threadnumber == "1"):
                            if(enemy_defense_flag == True):
                                p2_blood -= 5.0
                            else:
                                p2_blood -= 10.0
                        else:
                            if(enemy_defense_flag == True):
                                p2_blood -= 5.0
                            else:
                                p2_blood -= 5.0
                        text = "b"+" "+"10"+" "+"1"+" "+"1"+" "
                        clientSocket.send(str.encode(text))
            text = "Q"+" "+str(x)+" "+str(y)+" "+str(Q_count2//2)+" "
            clientSocket.send(str.encode(text))







        
    elif W_skill:
        if(temp_direction1 == "Left"):
            if(wflag == False):
                wflag = True
                w_locate = x - 500
                wf_locate = x - 500
                if(w_locate<0):
                    w_locate = 0
            if(W_count//2<=8):
                win.blit(wlstay[0], (x,y))
                win.blit(atk_w_Left[W_count//2], (x-30,y+30))
                text = "w"+" "+str(x-30)+" "+str(y+30)+" "+str(W_count//2)+" "
                clientSocket.send(str.encode(text))
            elif(W_count//2<=13):
                win.blit(atk_w_Left[W_count//2], (wf_locate,y))
                if((ex<=x and ex>=x-500) or (ex+75<=x and ex+75>=x-500)):
                    if(ey>=450):
                        enemy_hit_flag = True
                        if(threadnumber == "1"):
                            if(enemy_defense_flag == True):
                                p2_blood -= 1.0
                            else:
                                p2_blood -= 2.0
                        else:
                            if(enemy_defense_flag == True):
                                p1_blood -= 1.0
                            else:
                                p1_blood -= 2.0
                        text = "b"+" "+"2"+" "+"1"+" "+"1"+" "
                        clientSocket.send(str.encode(text))
                text = "w"+" "+str(wf_locate)+" "+str(y)+" "+str(W_count//2)+" "
                clientSocket.send(str.encode(text))
            else:
                x = w_locate
                win.blit(atk_w_Left[W_count//2], (x,y))
                text = "w"+" "+str(x)+" "+str(y)+" "+str(W_count//2)+" "
                clientSocket.send(str.encode(text))
        elif(temp_direction1 == "Right"):
            if(wflag == False):
                wflag = True
                w_locate = x + 500 - 70
                if(w_locate>1000):
                    w_locate = 1000
            if(W_count//2<=8):
                win.blit(wrstay[0], (x,y))
                win.blit(atk_w_Right[W_count//2], (x-30,y+30))
                text = "w"+" "+str(x-30)+" "+str(y+30)+" "+str(W_count//2)+" "
                clientSocket.send(str.encode(text))
            elif(W_count//2<=13):
                win.blit(atk_w_Right[W_count//2], (x,y))
                if((ex<=x+500-70 and ex>=x) or (ex+75<=x+500-70 and ex+75>=x)):
                    if(ey>=450):
                        enemy_hit_flag = True
                        if(threadnumber == "1"):
                            if(enemy_defense_flag == True):
                                p2_blood -= 1.0
                            else:
                                p2_blood -= 2.0
                        else:
                            if(enemy_defense_flag == True):
                                p1_blood -= 1.0
                            else:
                                p1_blood -= 2.0
                        text = "b"+" "+"2"+" "+"1"+" "+"1"+" "
                        clientSocket.send(str.encode(text))
                text = "w"+" "+str(x)+" "+str(y)+" "+str(W_count//2)+" "
                clientSocket.send(str.encode(text))
            else:
                x = w_locate
                win.blit(atk_w_Right[W_count//2], (x,y))
                text = "w"+" "+str(x)+" "+str(y)+" "+str(W_count//2)+" "
                clientSocket.send(str.encode(text))
    elif E_skill:
        if(temp_direction1 == "Left"):
            win.blit(atk_e_Left[E_count//2], (x,y))           
        elif(temp_direction1 == "Right"):
            win.blit(atk_e_Right[E_count//2], (x,y))
        text = "e"+" "+str(x)+" "+str(y)+" "+str(E_count//2)+" "
        clientSocket.send(str.encode(text))    



    elif isJump:
        win.blit(jumpRight[jrate//3], (x,y))
        text = "j"+" "+str(x)+" "+str(y)+" "+str(jrate//3)+" "
        clientSocket.send(str.encode(text))
        jrate += 1
        if(jrate == 18):
            jrate = 0
    elif self_defense_flag:      
        if(temp_direction1 == "Left"):
            win.blit(shield, (x-35,y-30))
            win.blit(defensel, (x,y+10))
        elif(temp_direction1 == "Right"):
            win.blit(shield, (x-40,y-30))
            win.blit(defenser, (x-20,y+10))
        text = "d"+" "+str(x)+" "+str(y)+" "+"1"+" "
        clientSocket.send(str.encode(text))
    elif left:
        win.blit(walkLeft[walkCount//2], (x,y))
        text = "l"+" "+str(x)+" "+str(y)+" "+str(walkCount//3)+" "
        clientSocket.send(str.encode(text))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//2], (x,y))
        text = "r"+" "+str(x)+" "+str(y)+" "+str(walkCount//3)+" "
        clientSocket.send(str.encode(text))
        walkCount +=1
    
    else:
        if(temp_direction1 == "Left"):
            win.blit(stayLeft[stayCount//3], (x,y))
        elif(temp_direction1 == "Right"):
            win.blit(stayRight[stayCount//3], (x,y))
        stayCount += 1


    #衝擊波
    if(len(fly_anim)!=0):
        new_anim = fly_anim[0]
        if(new_anim[0]== 'eflyr'):
            win.blit(atk_efly_Right[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
        elif(new_anim[0]== 'eflyl'):
            win.blit(atk_efly_Left[int(new_anim[3])], (float(new_anim[1]),float(new_anim[2])))
        fly_anim[0:0+1] = []

    if(E_flag == True):
        if(E_direction == "Right"):
            if(Eatkx>=1100):
                E_flag = False
            win.blit(atk_efly_Right[E_flycount//3], (Eatkx,Eatky))
            sword_left = Eatkx
            sword_right = Eatkx+70
            if(sword_right<=ex+75 and sword_right>=ex):
                if(ey>=450):
                    enemy_hit_flag = True
                    E_flag = False
                    if(threadnumber == "1"):
                        if(enemy_defense_flag == True):
                            p2_blood -= 15.0
                        else:
                            p2_blood -= 30.0
                    else:
                        if(enemy_defense_flag == True):
                            p1_blood -= 15.0
                        else:
                            p1_blood -= 30.0
                    text = "b"+" "+"30"+" "+"1"+" "+"1"+" "
                    clientSocket.send(str.encode(text))
            text = "eflyr"+" "+str(Eatkx)+" "+str(Eatky)+" "+str(E_flycount//3)+" "
            clientSocket.send(str.encode(text))
            E_flycount += 1
            Eatkx += 15
        elif(E_direction == "Left"):
            if(Eatkx<=-50):
                E_flag = False
            win.blit(atk_efly_Left[E_flycount//3], (Eatkx,Eatky))
            sword_left = Eatkx
            sword_right = Eatkx+70
            if(sword_left<=ex+75 and sword_left>=ex):
                if(ey>=450):
                    enemy_hit_flag = True
                    E_flag = False
                    if(threadnumber == "1"):
                        if(enemy_defense_flag == True):
                            p2_blood -= 15.0
                        else:
                            p2_blood -= 30.0
                    else:
                        if(enemy_defense_flag == True):
                            p1_blood -= 15.0
                        else:
                            p1_blood -= 30.0
                    text = "b"+" "+"30"+" "+"1"+" "+"1"+" "
                    clientSocket.send(str.encode(text))
            text = "eflyl"+" "+str(Eatkx)+" "+str(Eatky)+" "+str(E_flycount//3)+" "
            clientSocket.send(str.encode(text))
            E_flycount += 1
            Eatkx -= 15
    
    #擊打動畫
    if(enemy_hit_flag == True):
        win.blit(hit[enemy_hit_count//2], (ex,ey))
        enemy_hit_count += 1
        if(enemy_hit_count + 1 >= 10):
            enemy_hit_flag = False
            enemy_hit_count = 0
    if(self_hit_flag == True):
        win.blit(hit[self_hit_count//2], (x,y))
        self_hit_count += 1
        if(self_hit_count + 1 >= 10):
            self_hit_flag = False
            self_hit_count = 0
    #name
    if(threadnumber == "1"):
        text_p1 = name_font.render(name12[0], 1,"blue")
        rec_p1 = text_p1.get_rect()
        rec_p1.center = (x+30,y-50)    
        win.blit(text_p1, rec_p1)

        text_p2 = name_font.render(name12[1], 1,"green")
        rec_p2 = text_p2.get_rect()
        rec_p2.center = (ex+30,ey-50)    
        win.blit(text_p2, rec_p2)
    elif(threadnumber == "0"):
        text_p1 = name_font.render(name12[0], 1,"blue")
        rec_p1 = text_p1.get_rect()
        rec_p1.center = (ex+30,ey-50)    
        win.blit(text_p1, rec_p1)

        text_p2 = name_font.render(name12[1], 1,"green")
        rec_p2 = text_p2.get_rect()
        rec_p2.center = (x+30,y-50)    
        win.blit(text_p2, rec_p2)

    #blood
    text_p1_blood = my_font.render(str(p1_blood), 1,"blue")
    rec_p1_blood = text_p1_blood.get_rect()
    rec_p1_blood.center = (100,100)
    win.blit(text_p1_blood, rec_p1_blood)

    text_p2_blood = my_font.render(str(p2_blood), 1,"green")
    rec_p2_blood = text_p2_blood.get_rect()
    rec_p2_blood.center = (900,100)
    win.blit(text_p2_blood, rec_p2_blood)

    pygame.display.update()


def draw_gameover():
    win.blit(bg1, (0,0))
    if(p1_blood<=0):
        winname = name12[1]
    else:
        winname = name12[0]
    winname +=" win"
    text_gameover = my_font.render(winname, 1,"white")
    rec_gameover= text_gameover.get_rect()
    rec_gameover.center = (550,300)
    win.blit(text_gameover, rec_gameover)
    pygame.display.update() 



def draw_login():  
    win.blit(bg1, (0,0))
    win.blit(text_login, rec_login)
    pygame.display.update() 


def draw_wait():
    global waitcount
    if(waitcount == 32):
        waitcount = 0
    if(waitcount//4 == 0 or waitcount//4 == 7):
        win.blit(wait1, (0,0))
    elif(waitcount//4 == 1 or waitcount//4 == 6):
        win.blit(wait2, (0,0))
    elif(waitcount//4 == 2 or waitcount//4 == 5):
        win.blit(wait3, (0,0))
    elif(waitcount//4 == 3 or waitcount//4 == 4):
        win.blit(wait4, (0,0))
    waitcount += 1
    pygame.display.update() 


#mainloop
click = True
ifready = True
run = True
nameset = False
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
            clientSocket.send(str.encode("bye"))

    #login 介面
    if(click):
        buttons = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if(buttons[0]):
            if(pos[0]>=rec_login.left and pos[0]<=rec_login.right and pos[1]>=rec_login.top and pos[1]<=rec_login.bottom):
                click = False
        if(click):
            draw_login()
            continue
    #login 介面

    #等待畫面
    if(ifready):
        clientSocket.send(str.encode("ready"+" "+ID+" "+"1"+" "+"1"+" "))
        ifready = False
    if(state==""):
        draw_wait()
        continue
    #等待畫面
    if(not nameset):
        name12 = state.split()
        nameset = True
    #打鬥畫面
    if(p1_blood<=0 or p2_blood<=0):
        if(bye_flag == False):
            bye_flag = True
            clientSocket.send(str.encode("bye"))
        draw_gameover()
        continue
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and not isJump:
        self_defense_flag = True
        skills = True
    else:
        self_defense_flag = False
        skills = False

    if(not Q_skill):
        if(not isJump and not skills and not self_hit_flag):
            if keys[pygame.K_q]:
                skills = True
                Q_skill = True
                walkCount = 0
    else:
        if(Q_atk == 0):
            if Q_count <= 11:
                skills = True
                Q_count += 1
            else:
                Q_count = 0
                skills = False
                Q_skill = False
                Q_atk = 1
                print(Q_atk)
        elif(Q_atk == 1):
            if Q_count2 <= 12:
                skills = True
                Q_count2 += 1
            else:
                Q_count2 = 0
                skills = False
                Q_skill = False
                Q_atk = 0
    
    if(not W_skill):
        if(not isJump and not skills and not self_hit_flag):
            if keys[pygame.K_w]:
                skills = True
                W_skill = True
                walkCount = 0
    else:
        if W_count <= 40:
            skills = True
            W_count += 1
        else:
            W_count = 0
            skills = False
            W_skill = False
            wflag = False

    if(not E_skill):
        if(not isJump and not skills and E_flag==False and not self_hit_flag):
            if keys[pygame.K_e]:
                skills = True
                E_skill = True
                walkCount = 0
    else:
        if E_count <= 12:
            skills = True
            E_count += 1
        else:
            E_count = 0
            skills = False
            E_skill = False
            E_flag = True
            E_direction = temp_direction1
            if(E_direction == "Right"):
                Eatkx = x
                Eatky = y
            elif(E_direction == "Left"):
                Eatkx = x-75
                Eatky = y
    
    

    if(not skills and not self_hit_flag):
        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
            temp_direction1 = "Left"
        elif keys[pygame.K_RIGHT] and x < 1070 - width - vel:
            x += vel
            right = True
            left = False
            temp_direction1 = "Right"
        else:
            right = False
            left = False
            self_defense_flag = False
            walkCount = 0
        
        if not(isJump):
            if keys[pygame.K_UP]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -8:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 8
            
    redrawGameWindow(temp_direction1)


clientSocket.close()
pygame.quit()
