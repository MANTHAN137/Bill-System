from tkinter import *
from datetime import date

import webbrowser
today = date.today()
date = today.strftime("%B %d, %Y")




root=Tk()

#>..........................Manthan Dhole 201080020.......................................<
#>..........................Basic Title ,Geometry and Logo Addition.......................<
try:
    logo=PhotoImage(file='logo.png')
    root.iconphoto(False,logo)
except:
    pass
root.geometry("1000x500")
root.maxsize(1000,500)
root.minsize(370,350)
root.title("Bill Management")


#>..........................Reset and Total Function in the bill counter..................<

def reset():
    eDosa.delete(0,END)
    eIdli.delete(0,END)
    eSamosa.delete(0,END)
    eKachodi.delete(0,END)
    eVada.delete(0,END)
    eCookies.delete(0,END)
    totalBill.set("Total")
def totalCal():
    try:a1=int(dosa.get())
    except:a1=0
    try:a2=int(idli.get())
    except:a2=0
    try:a3=int(samosa.get())
    except:a3=0
    try:a4=int(kachodi.get())
    except:a4=0
    try:a5=int(vada.get())
    except:a5=0
    try:a6=int(cookies.get())
    except:a6=0
    c1=60*a1
    c2=60*a2
    c3=60*a3
    c4=60*a4
    c5=60*a5
    c6=60*a6
    global t
    t="Rs"+str(c1+c2+c3+c4+c5+c6)
    totalBill.set(t)  
   

#>.....................................Project Heading...............................<

Label(text="Bill Management",bg="Black",fg="cyan",font=("calibri",23,'bold'),width="300",height="1",borderwidth=10,relief=SUNKEN).pack()

#>......................................Menu Card....................................<
f=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=290,borderwidth=2,relief=SUNKEN)
f.place(x=10,y=60)
Label(f,text="Date : "+date,font=("Gabriola",10,"bold"),fg="cyan",bg="black").place(x=80,y=0)

Label(f,text="Menu",font=("Gabriola",30,"bold"),fg="Black",bg="lightyellow").place(x=80,y=20)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa.......Rs.60/plate",fg="black",bg="lightyellow").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Idli.......Rs.60/plate",fg="black",bg="lightyellow").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Samosa.......Rs.60/plate",fg="black",bg="lightyellow").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Kachodi.......Rs.60/plate",fg="black",bg="lightyellow").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Vada.......Rs.60/plate",fg="black",bg="lightyellow").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cookies.......Rs.60/plate",fg="black",bg="lightyellow").place(x=10,y=230)


#>...................................Entry widgets in the bill counter.........................<
f1=Frame(root,bd=5,height=370,width=300,relief=SUNKEN,highlightbackground='black',highlightthickness=2)
f1.pack()

dosa=StringVar()
idli=StringVar()
samosa=StringVar()
kachodi=StringVar()
vada=StringVar()
cookies=StringVar()
#>...................................Menu Items.....................................<
Label(f1,font=("aria",20,'bold'),text='Dosa',width=12,fg="blue4").grid(row=1,column=0)
Label(f1,font=("aria",20,'bold'),text='Idli',width=12,fg="blue4").grid(row=2,column=0)
Label(f1,font=("aria",20,'bold'),text='Samosa',width=12,fg="blue4").grid(row=3,column=0)
Label(f1,font=("aria",20,'bold'),text='Kachodi',width=12,fg="blue4").grid(row=4,column=0)
Label(f1,font=("aria",20,'bold'),text='Vada',width=12,fg="blue4").grid(row=5,column=0)
Label(f1,font=("aria",20,'bold'),text='Cookies',width=12,fg="blue4").grid(row=6,column=0)

#>............................Entry Widget For number of items...........................<
eDosa=Entry(f1,font={'aria',20,'bold'},textvariable=dosa,bd=6,width=8,bg="lightpink")
eDosa.grid(row=1,column=1)
eIdli=Entry(f1,font={'aria',20,'bold'},textvariable=idli,bd=6,width=8,bg="lightpink")
eIdli.grid(row=2,column=1)
eSamosa=Entry(f1,font={'aria',20,'bold'},textvariable=samosa,bd=6,width=8,bg="lightpink")
eSamosa.grid(row=3,column=1)
eKachodi=Entry(f1,font={'aria',20,'bold'},textvariable=kachodi,bd=6,width=8,bg="lightpink")
eKachodi.grid(row=4,column=1)
eVada=Entry(f1,font={'aria',20,'bold'},textvariable=vada,bd=6,width=8,bg="lightpink")
eVada.grid(row=5,column=1)
eCookies=Entry(f1,font={'aria',20,'bold'},textvariable=cookies,bd=6,width=8,bg="lightpink")
eCookies.grid(row=6,column=1)

#>....................................Buttons Reset and Total................................<
bReset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=reset)
bReset.grid(row=7,column=0)
totalBill=StringVar()
totalBill.set("Total")
bTotal=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,textvariable=totalBill,text=totalBill,command=totalCal)
bTotal.grid(row=7,column=1)

#>....................................Calculator Code Start..................................<

f2=Frame(root,bg="lightyellow",highlightbackground="Black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=60)

frame = Frame(f2, relief=SUNKEN,borderwidth=5,highlightbackground="black",highlightthickness=1)
frame.pack(side="right")
calEntry=StringVar()
e = Entry(frame,width=15,font=('times',25,'bold'),textvariable=calEntry,borderwidth=5,relief=SUNKEN)
e.grid(row=0, column=0, columnspan=4)


def button_Quit():
    root.destroy()
def button_Clear():
    e.delete(0,END)

def button_add(number):
    a=calEntry.get()+number
    calEntry.set(a)
def evaluates():
    a=eval(calEntry.get())
    calEntry.set(a)
    

button1 = Button(frame, text="1", padx=5, pady=5,width=5,font=("times",12,"bold"),
                 command=lambda: button_add('1'))
button2 = Button(frame, text="2", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('2'))
button3 = Button(frame, text="3", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('3'))
button4 = Button(frame, text="4", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('4'))
button5 = Button(frame, text="5", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('5'))
button6 = Button(frame, text="6", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('6'))
button7 = Button(frame, text="7", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('7'))
button8 = Button(frame, text="8", font=("times",12,"bold"), padx=5, pady=5,width=5,
                 command=lambda: button_add('8'))
button9 = Button(frame, text="9", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('9'))
button0 = Button(frame, text="0", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=lambda: button_add('0'))
buttonAdd = Button(frame, text="+", padx=5, pady=5,width=5, font=("times",12,"bold"),
                   command=lambda:button_add('+'))
buttonSub = Button(frame, text="-", padx=5, pady=5,width=5, font=("times",12,"bold"),
                   command=lambda:button_add('-'))
buttonMulti = Button(frame, text="*", padx=5, pady=5,width=5, font=("times",12,"bold"),
                   command=lambda:button_add('*'))
buttonDiv = Button(frame, text="/", padx=5, pady=5,width=5, font=("times",12,"bold"),
                   command=lambda:button_add('/'))

buttonEq = Button(frame, text="=", padx=5, pady=5,width=5 ,font=("times",12,"bold"),
                  command=evaluates)
buttonC = Button(frame, text="C", padx=5, pady=5,width=5, font=("times",12,"bold"),
                 command=button_Clear)
buttonDot = Button(frame, text=".", padx=5, pady=5,width=5, font=("times",12,"bold"),
                   command=button_add)
buttonQuit = Button(frame, text="Quit", padx=5, font=("times",12,"bold"),
                     pady=5, width=5,command=button_Quit)
buttonb1 = Button(frame, text="(", padx=5, pady=5,width=5, font=("times",12,"bold"),
                   command=lambda:button_add("("))
buttonb2 = Button(frame, text=")", padx=5, font=("times",12,"bold"),
                     pady=5, width=5,command=lambda:button_add(")"))

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)
buttonDot.grid(row=4, column=0)


buttonAdd.grid(row=1, column=3)
buttonSub.grid(row=2, column=3)

buttonMulti.grid(row=3, column=3)
buttonDiv.grid(row=4, column=3)

buttonb1.grid(row=5,column=0)
buttonb2.grid(row=5,column=1)
buttonQuit.grid(row=5, column=2)
buttonEq.grid(row=5,column=3)
buttonC.grid(row=4,column=2)
#>...................................Web links..................................<
def youtube():
    webbrowser.open("https://www.youtube.com/results?search_query=healthly+food")
def instagram():
    webbrowser.open("https://www.instagram.com/fitness_food_trainer/")
def help():
    webbrowser.open("https://www.youtube.com/watch?v=_Seduw6b8x0")

Social=Frame(root,borderwidth=5,relief=SUNKEN,highlightbackground="Orange",highlightthickness=6)
Social.place(x=10,y=350)
Label(Social,text="sOCIAL fOODY zONE",font=("Lucida Calligraphy",21,'bold')).grid(row=0,column=0,columnspan=3)
Button(Social,text="Youtube-Recipes",width=20,font=("Times",20,"bold"),command=youtube,height=2).grid(row=1,column=0)
Button(Social,text="Instagram",width=9,font=("Times",20,"bold"),height=2,command=instagram).grid(row=1,column=1)
Button(Social,text="Help",width=10,font=("Times",20,"bold"),height=2,command=help).grid(row=1,column=2)

#>..................................Info Saver.................................<

def saveInfo():
    try:
        with open("Record.txt",'a') as file:
            file.write(f"{name.get(),contact.get(),credit.get(),bill.get()}\n")
        file.close()
    except:
        file=open('Record.txt','w')
        file.close()
def reseter():
    n=""
    name.set(n)
    contact.set(n)
    credit.set(n)
    bill.set(n)
        

infoSaver=Frame(root,relief=SUNKEN,highlightbackground="Orange",highlightthickness=6)
infoSaver.place(x=690,y=330)
Label(infoSaver,text="Save Info",font=("Lucida Calligraphy",10,'bold'),background="cyan").grid(row=0,column=0,columnspan=2)
Label(infoSaver,text="Name",font=("Lucida Calligraphy",12,'bold')).grid(row=1,column=0)
Label(infoSaver,text="Contact/Id",font=("Lucida Calligraphy",12,'bold')).grid(row=2,column=0)
Label(infoSaver,text="Credit",font=("Lucida Calligraphy",12,'bold')).grid(row=3,column=0)
Label(infoSaver,text="Bill",font=("Lucida Calligraphy",12,'bold')).grid(row=4,column=0)

name=StringVar()
contact=StringVar()
credit=StringVar()
bill=StringVar()

Entry(infoSaver,textvariable=name,width=26).grid(row=1,column=1)
Entry(infoSaver,textvariable=contact,width=26).grid(row=2,column=1)
Entry(infoSaver,textvariable=credit,width=26).grid(row=3,column=1)
Entry(infoSaver,textvariable=bill,width=26).grid(row=4,column=1)
Button(infoSaver,text="Reset",command=reseter).grid(row=5,column=0)
Button(infoSaver,text="Save",command=saveInfo).grid(row=5,column=1)

root.mainloop()