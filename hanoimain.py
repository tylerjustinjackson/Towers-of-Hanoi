from turtle import Screen, Turtle, textinput
import time
from random import shuffle

"""To play, you press the key corresponding to the tower to move
disk over by one tower (to the right)."""


#GLOBAL VARIABLES 

newgame= True
positions=[(-200, -180), (0, -180), (200, -180)]
alldisks=[]
rowa=[]
rowb=[]
rowc=[]
colorlist=['yellow', 'gold', 'orange', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
shuffle(colorlist)
shuffle(colorlist)
colorlist=colorlist*1000
pins = {1:[], 2:[], 3:[], 4:[], 5:[]}

#CLASSES

class Poles:

    def __init__(self, towers=3):
        
        self.createtower(towers)
               
    def createtower(self,towers):
        for tower in range(0,towers):
            pole= Turtle('square')
            
            pole.color("white")
            pole.shapesize(15,.2)
            pole.penup()
            pole.speed('fastest')
            pole.goto(positions[tower-1])
            

class Disks():
    
    def __init__(self, numberofdisk=3, r=False):
        self.time=0
        self.disktext=disktext
        for i in range(numberofdisk, 0, -1):
            self.alllist=self.createdisks(i)
            self.time+=1
            
        
        if r==True:  
            self.movedisk()
        if r==False:
            self.hanoi(disktext, 'A','B', 'C')


    def gameover(self, disktext, text=True):
        if len(rowc)==disktext:
            self.game = Turtle()
            align = "center"
            self.game.hideturtle()
            self.game.penup()
            self.game.speed('fastest')
            FONT = ("Verdana", 50, "bold")
            self.game.color('white')
            self.game.goto(0,0)
            if text==True:
                self.game.write(f'YOU WON!', align=align, font=FONT)
            elif text==False:
                self.game.write(f'HANOI SOLVED!', align=align, font=FONT)

    def createdisks(self,i):
        disk=Turtle()
        disk.color(colorlist[i])
        disk.shape('square')
        disk.shapesize(0.5,(1+(i)))
        disk.penup()
        disk.speed('fastest')
        self.yposition, self.xposition = self.newdiskpositions(i)
        disk.goto(self.xposition, self.yposition)
        rowa.insert(0, [disk, self.yposition, i])

    def newdiskpositions(self,i):
        self.yposition= -280+(self.time*(20))
        self.xposition= -200
        return self.yposition, self.xposition



    def movedisk(self):
        screen.listen()
        screen.onkey(self.MoveA, 'a')
        screen.onkey(self.MoveB, 'b')
        screen.onkey(self.MoveC, 'c')
        screen.onkey(self.space, 'space')
    
    def error(self):
        self.errors = Turtle()
        align = "center"
        self.errors.hideturtle()
        self.errors.penup()
        self.errors.speed('fastest')
        FONT = ("Verdana", 20, "bold")
        self.errors.color('white')
        self.errors.goto(0,0)
        self.errors.write('Invalid Move!', align=align, font=FONT)
        time.sleep(1.7)
        self.errors.clear()

    def MoveA(self):
        try:
            disk= rowa[0][0]
            pos=rowa[0][-1]

            if not len(rowb):
                disk.goto(0, -280)
                rowb.insert(0,[disk, -280, pos])
                del rowa[0]
            elif pos< rowb[0][-1]:
                d=rowb[0][1]
                disk.goto(0, 20+d)
                rowb.insert(0,[disk, 20+d, pos])
                del rowa[0]

            elif not len(rowc):
                disk.goto(200, -280)
                rowc.insert(0,[disk, -280, pos])
                del rowa[0]
            elif pos< rowc[0][-1]:
                d=rowc[0][1]
                disk.goto(200, 20+d)
                rowc.insert(0,[disk, 20+d, pos])
                del rowa[0]

            else:
                self.error()

            self.gameover(self.disktext)
        except IndexError:
            self.error()


    def MoveB(self):
        try:

            disk= rowb[0][0]
            pos=rowb[0][-1]

            if not len(rowc):
                disk.goto(200, -280)
                rowc.insert(0,[disk, -280, pos])
                del rowb[0]
            elif pos< rowc[0][-1]:
                d=rowc[0][1]
                disk.goto(200, 20+d)
                rowc.insert(0,[disk, 20+d, pos])
                del rowb[0]

            elif not len(rowa):
                disk.goto(-200, -280)
                rowa.insert(0,[disk, -280, pos])
                del rowb[0]
            elif pos< rowa[0][-1]:
                d=rowa[0][1]
                disk.goto(-200, 20+d)
                rowa.insert(0,[disk, 20+d, pos])
                del rowb[0]

            else:
                self.errors()
            self.gameover(self.disktext)
        except IndexError:
            self.error()


    def MoveC(self):
        try:
            disk= rowc[0][0]
            pos=rowc[0][-1]

            if not len(rowa):
                disk.goto(-200, -280)
                rowa.insert(0,[disk, -280, pos])
                del rowc[0]
            elif pos< rowa[0][-1]:
                d=rowa[0][1]
                disk.goto(-200, 20+d)
                rowa.insert(0,[disk, 20+d, pos])
                del rowc[0]

            elif not len(rowb):
                disk.goto(0, -280)
                rowb.insert(0,[disk, -280, pos])
                del rowc[0]
            elif pos< rowb[0][-1]:
                d=rowb[0][1]
                disk.goto(0, 20+d)
                rowb.insert(0,[disk, 20+d, pos])
                del rowc[0]

            else:
                self.errors()
            
            self.gameover(self.disktext)
        except IndexError:
            self.error()


    def hanoi(self,num,f,h,t):

        if num == 0:  # Prevent from moving 0 or negative discs
            self.gameover(self.disktext, text=False)
            pass

        else:
            self.hanoi(num-1,f,t,h) # move all but bottom to helper (A to B using C)
            time.sleep(0.2)
            self.move(f,t) # move bottom disc to target (from A to C)
            self.hanoi(num-1,h,f,t) # move rest from helper to target via from (from B to C using A)



    def move(self,f,t):
        #Move disc from F to T

        if f=='A':
            disk=rowa[0][0]
            pos=rowa[0][-1]

            if t=='C':

                if not len(rowc):
                    disk.goto(200, -280)
                    rowc.insert(0,[disk, -280, pos])
                    del rowa[0]
                elif pos< rowc[0][-1]:
                    d=rowc[0][1]
                    disk.goto(200, 20+d)
                    rowc.insert(0,[disk, 20+d, pos])
                    del rowa[0]
            
            elif t=='B':
                if not len(rowb):
                    disk.goto(0, -280)
                    rowb.insert(0,[disk, -280, pos])
                    del rowa[0]
                elif pos< rowb[0][-1]:
                    d=rowb[0][1]
                    disk.goto(0, 20+d)
                    rowb.insert(0,[disk, 20+d, pos])
                    del rowa[0]


        elif f=='B':
            disk=rowb[0][0]
            pos=rowb[0][-1]
            if t=='C':

                if not len(rowc):
                    disk.goto(200, -280)
                    rowc.insert(0,[disk, -280, pos])
                    del rowb[0]
                elif pos< rowc[0][-1]:
                    d=rowc[0][1]
                    disk.goto(200, 20+d)
                    rowc.insert(0,[disk, 20+d, pos])
                    del rowb[0]
            
            elif t=='A':
                if not len(rowa):
                    disk.goto(-200, -280)
                    rowa.insert(0,[disk, -280, pos])
                    del rowb[0]
                elif pos< rowa[0][-1]:
                    d=rowa[0][1]
                    disk.goto(-200, 20+d)
                    rowa.insert(0,[disk, 20+d, pos])
                    del rowb[0]

            
        elif f=='C':
            disk=rowc[0][0]
            pos=rowc[0][-1]
            if t=='B':

                if not len(rowb):
                    disk.goto(0, -280)
                    rowb.insert(0,[disk, -280, pos])
                    del rowc[0]
                elif pos< rowb[0][-1]:
                    d=rowb[0][1]
                    disk.goto(0, 20+d)
                    rowb.insert(0,[disk, 20+d, pos])
                    del rowc[0]
            
            elif t=='A':

                if not len(rowa):
                    disk.goto(-200, -280)
                    rowa.insert(0,[disk, -280, pos])
                    del rowc[0]
                elif pos< rowa[0][-1]:
                    d=rowa[0][1]
                    disk.goto(-200, 20+d)
                    rowa.insert(0,[disk, 20+d, pos])
                    del rowc[0]
    


    def space(self):
        self.enter = Turtle()
        align = "center"
        self.enter.hideturtle()
        self.enter.penup()
        self.enter.speed('fastest')
        FONT = ("Verdana", 20, "bold")
        self.enter.color('white')
        self.enter.goto(-200,0)
        self.enter.write('A', align=align, font=FONT)
        self.enter.goto(0,0)
        self.enter.write('B', align=align, font=FONT)
        self.enter.goto(200,0)
        self.enter.write('C', align=align, font=FONT)
        time.sleep(1.7)
        self.enter.clear()



# FUNCTIONS

def intro():
    t=Turtle()
    global screen
    screen = Screen()
    t.hideturtle()
    screen.setup(width=800, height=600)
    screen.title('Towers of Hanoi - Tyler Jackson')
    screen.bgcolor("maroon")

    align = "center"
    FONT = ("Verdana", 50, "bold")
    color = 'white'
    text=Turtle()
    text.color(color)
    text.hideturtle()
    text.penup()
    text.speed('fastest')
    text.goto(0,230)
    text.write('Towers of Hanoi', align=align, font= FONT)

def orders(i):
    orders = Turtle()
    align = "center"
    orders.hideturtle()
    orders.penup()
    orders.speed('fastest')
    FONT = ("Verdana", 12, "bold")
    color = colorlist[i]
    orders.color(color)
    orders.goto(-200,200-(i*15))
    orders.write(f'{colorlist[i]} corresponds to disk {i}', align=align, font=FONT)


if __name__ == '__main__':

    try: 
        intro() 
        algorplay= textinput('Play or Watch??', 'Would you like to watch or play?').lower().strip()
        disktext = int(textinput('How many disks?', 'How many disks would you like?'))
        textinput('Game Rules', '\nYou cannot place a bigger disk over a smaller disk.\nThe objective is to get all the disk to tower C.\nHowever, you can only move one disk at a time.\n')

        Poles(3)

        for i in range (disktext,0,-1): orders(i)
        
        if algorplay=='watch':
            
            Disks(numberofdisk= disktext)
            while True:
                time.sleep(0.01)
                screen.update()
                screen.exitonclick()

        elif algorplay=='play':
            textinput('GamePlay Disclaimer', '\nWith turtle, multiple key inputs are limited\ntherefore, press the corresponding tower\nkey to move the top disk from the tower.\nto the top fo the tower to the right if\nyou forget which tower corresponds to\nwhich key, press the space key!\n')
            Disks(numberofdisk= disktext, r=True)
            while True:
                time.sleep(0.01)
                screen.update()
                screen.exitonclick()

    except:
        pass