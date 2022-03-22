

import webbrowser

from tkinter import *

root = Tk()

root.title("WebBrowsers")

root.geometry("660x660")
def youtube():
    webbrowser.open("https://www.youtube.com/results?search_query=healthly+food")

def whatsappweb():
    webbrowser.open("www.whatsappweb.com")

def instagram():
    webbrowser.open("https://www.instagram.com/fitness_food_trainer/")

def gmail():
    webbrowser.open("www.gmail.com")


Label(root, text="WELCOME TO MY FAVOURITE \nWEBSITES", font="Helvtica 25 bold").pack()
Label(root,text="Click on the buttons to open website",font="LUCIDA").pack()

f=Frame(root,background='lightgreen',width=660)
f.pack(side='left')
myyoutube = Button(f, text="Food_YOUTUBE", command=youtube,font="LUCIDA 12 bold",width=14).grid(row=0,column=0)
mywhatsapp = Button(f, text="WHATSAPP WEB", command=whatsappweb,font="LUCIDA 12 bold",width=14).grid(row=0,column=1)
myinstagram = Button(f, text="INSTAGRAM", command=instagram,font="LUCIDA 12 bold",width=14).grid(row=0,column=2)
mygmail= Button(f, text="GMAIL" , command=gmail,font="LUCIDA 12 bold",width=14).grid(row=0,column=3)

root.mainloop()