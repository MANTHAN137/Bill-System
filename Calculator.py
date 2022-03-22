from tkinter import *
root = Tk()
root.title("Simple Calculator")
frame = Frame(root, relief=SOLID)
frame.grid()
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
    

button1 = Button(frame, text="1", padx=5, pady=5,width=5, font=("times",12,"bold"),
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
root.mainloop()
