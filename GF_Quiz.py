
import matplotlib.pyplot as plt
import matplotlib.image as mpl_img
import math
import random
from PIL import Image, ImageTk
from tkinter import *
from matplotlib.widgets import Button as matButton
from functools import partial
from numpy import *

myfont = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
myfont2 = {'family': 'serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 16,
        }
myfont3 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 32,
        }
def gf_add(x1,x2,GFrep):
    x1_poly = GFrep[x1]
    x2_poly = GFrep[x2]
    add_x1_x2_poly = [x1_poly[k]^x2_poly[k] for k in range(len(x1_poly)) ]
    add_x1_x2_expo = [k for k, v in GFrep.items() if v == add_x1_x2_poly][0]
    return add_x1_x2_expo   

def gf_mul(x1,x2,GFrep):
    if x1!=-1 and x2!=-1:
        mul_x1_x2 = (x1 + x2)%(len(GFrep)-1)
        return(mul_x1_x2)
    else:
        return(-1)
def createGFrepresentation(primitivePoly):
        Degree = len(primitivePoly)-1
        GFsize = 2**Degree
        print(Degree)

        GFrep = {}
        tempPoly = [0]*Degree
        for expo in range(-1,GFsize-1):
            if expo == -1:
                GFrep[expo] = tempPoly.copy()
            elif expo == 0:
                tempPoly[0] = 1
                GFrep[expo] = tempPoly.copy()
            else:
                msb = tempPoly[-1]
                tempPoly[1:] = tempPoly[0:-1]
                tempPoly[0] = 0
                if msb == 1:     
                    tempPoly = [(tempPoly[k]+primitivePoly[k])%2 for k in range(Degree)]
                GFrep[expo] = tempPoly.copy()
            print(expo,GFrep[expo])
        return(GFrep)
#---------------- + gf ------------------
def GFquiz1():
######################################
############### Quiz
    def gf2str(val):
        if val == -1:
            mytext = r'$0$'
        elif val==0:
            mytext = r'$1$'
        elif val==1:
            mytext = r'$\alpha$'
        else:
            mytext = r'$\alpha^' + str(val) + '$'
        return mytext
###########################################
    def show_answer(event,operation,k):
        if operation == '+':
            ans2_text.set_text(gf2str(k-1))
            global your_ans 
            your_ans = k
    def check_ans(a,b):
        if your_ans-1 == correct_ans:
            check2_text.set_text('Correct')
        else :
            check2_text.set_text('Incorrect')

# main of GFQUIZ

    fig4 = plt.figure()
    fig4.canvas.set_window_title('Add GF Quiz')
    plt.axis('off')
    plt.title('A simple test for GF(8)')
    myaxes = plt.axes([0,0,1,1])  
    # โจทย์2 x
    myaxes.text(0.41,0.84,'Quiz',fontdict=myfont3)
    a = random.randint(-1,6)
    b = random.randint(-1,6)
    
    prob2 = gf2str(a) + ' + ' + gf2str(b) + ' = '
    myaxes.text(0.1,0.45,prob2,fontdict=myfont)
    myaxes.text(0.28,0.43,'............',fontdict=myfont)
    ans2_text = myaxes.text(0.33,0.45,'  ',fontdict=myfont2, color = '#6510C4')
    check2_text = myaxes.text(0.41,0.12,'  ',fontdict=myfont2, color = 'green')
    correct_ans = gf_add(a,b,GFrep)
    bn_prob2 = [0]*8
    for k in range(4):
        bn_prob2[k] = matButton(plt.axes([0.5+0.1*k,0.45,0.09,0.09]),gf2str(k-1),color='pink', hovercolor='#D179E7')
        bn_prob2[k].label.set_fontsize(16)
        bn_prob2[k].on_clicked(lambda e,k=k :show_answer(e,'+',k)) 
        bn_prob2[4+k] = matButton(plt.axes([0.5+0.1*k,0.35,0.09,0.09]),gf2str(4+k-1),color='pink', hovercolor='#D179E7')
        bn_prob2[4+k].label.set_fontsize(16)
        bn_prob2[4+k].on_clicked(lambda e,k=k :show_answer(e,'+',4+k)) 

    bn_send = matButton(plt.axes([0.66, 0.1, 0.15, 0.075]),'check',color='#F0F181', hovercolor='#A8F181')
    bn_send.label.set_fontsize(16)  
    bn_send.on_clicked(lambda a = a,b=b : check_ans(a,b))
    plt.show()

#---------------- x gf ------------------
def GFquiz2():
    ######################################
############### Quiz
    def gf2str(val):
        if val == -1:
            mytext = r'$0$'
        elif val==0:
            mytext = r'$1$'
        elif val==1:
            mytext = r'$\alpha$'
        else:
            mytext = r'$\alpha^' + str(val) + '$'
        return mytext
###########################################
    def show_answer(event,operation,k):
        if operation == 'x':
            ans2_text.set_text(gf2str(k-1))
            global your_ans 
            your_ans = k
    def check_ans(a,b):
        if your_ans-1 == correct_ans:
            check2_text.set_text('Correct')
        else :
            check2_text.set_text('Incorrect!')

# main of GFQUIZ

    fig4 = plt.figure()
    fig4.canvas.set_window_title('Mull GF Quiz')
    plt.axis('off')
    plt.title('A simple test for GF(8)')
    myaxes = plt.axes([0,0,1,1])  
    # โจทย์2 x
    myaxes.text(0.41,0.84,'Quiz',fontdict=myfont3)
    a = random.randint(-1,6)
    b = random.randint(-1,6)
    
    prob2 = gf2str(a) + ' $\cdot$ ' + gf2str(b) + ' = '
    myaxes.text(0.1,0.45,prob2,fontdict=myfont)
    myaxes.text(0.28,0.43,'............',fontdict=myfont)
    ans2_text = myaxes.text(0.33,0.45,'  ',fontdict=myfont2, color = '#6510C4')
    check2_text = myaxes.text(0.41,0.12,'  ',fontdict=myfont2, color = 'green')
    correct_ans = gf_mul(a,b,GFrep)
    bn_prob2 = [0]*8
    for k in range(4):
        bn_prob2[k] = matButton(plt.axes([0.5+0.1*k,0.45,0.09,0.09]),gf2str(k-1),color='pink', hovercolor='#D179E7')
        bn_prob2[k].label.set_fontsize(16)
        bn_prob2[k].on_clicked(lambda e,k=k :show_answer(e,'x',k))
        bn_prob2[4+k] = matButton(plt.axes([0.5+0.1*k,0.35,0.09,0.09]),gf2str(4+k-1),color='pink', hovercolor='#D179E7')
        bn_prob2[4+k].label.set_fontsize(16)
        bn_prob2[4+k].on_clicked(lambda e,k=k :show_answer(e,'x',4+k)) 

    bn_send = matButton(plt.axes([0.66, 0.1, 0.15, 0.075]),'check',color='#F0F181', hovercolor='#A8F181')
    bn_send.label.set_fontsize(16)  
    bn_send.on_clicked(lambda a = a,b=b : check_ans(a,b))
    plt.show()


#---------------------- main code --------------------------

root = Tk()
root.title('GF Quiz')
root.resizable(width=False,height=False)
winWidth = 620
winHeight = 481
winSize = str(winWidth)+'x'+str(winHeight)
root.geometry(winSize)

tkimage = PhotoImage(file='bg2.png')
tkimage = tkimage.zoom(2,2)
tkimage = tkimage.subsample(2)
bg_pic = Label(root,image = tkimage)
mylabel = Label(root,text = 'GALOIS',fg = 'black', font = ("Arial", 50, 'bold'), bg = 'white')
mylabel.place(x = 200, y =150 )
bg_pic.place(x=0, y=0, relwidth=1, relheight=1)

#--- button for +
bt_1 = Button(root, compound=TOP,text = '+',font = ("Arial", 80, 'bold'),
                fg='pink',
                relief='raised',
                borderwidth=6,width=20, command=GFquiz1)# command = from def นำไปสู่หน้าอีกหน้า
bt_1.place(width=90,height=90,x=160,y=250)

#--- button for x
bt_2 = Button(root, compound=TOP,text = 'X',font = ("Arial", 60, 'bold'),
                fg='pink',relief='raised',
                borderwidth=6,width=20,
                command=GFquiz2)# command = from def นำไปสู่หน้าอีกหน้า
bt_2.place(width=90,height=90,x=365,y=250)


## Global variables
your_ans = 0

primitivePoly = [1,1,0,1]
GFrep = createGFrepresentation(primitivePoly)

root.mainloop()