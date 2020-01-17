from random import randint
from tkinter import *
import time
import sys
import tkinter as tk
import pygame
import button


leftClick = False

a = (randint(0, 9))
b = (randint(0, 9))
c = (randint(0, 9))
d = (randint(0, 9))
e = (randint(0, 9))

list1 = [a]
list2 = [a, b]
list3 = [a, b, c]
list4 = [a, b, c, d]
list5 = [a, b, c, d, e]

root = Tk()

abc = ""
list6 = []
enter = "enter numbers: "


s = StringVar()
root.title("Spomin_(beta)")


def leftClick1():
   print(" 1 ")
   label_.configure(text=" 1 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "1 \n")
   txt1.config(state="disabled")


def leftClick2():
   print(" 2 ")
   label_.configure(text=" 2 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "2 \n")
   txt1.config(state="disabled")


def leftClick3():
   print(" 3 ")
   label_.configure(text=" 3 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "3 \n")
   txt1.config(state="disabled")


def leftClick4():
   print(" 4 ")
   label_.configure(text=" 4 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "4 \n")
   txt1.config(state="disabled")


def leftClick5():
   print(" 5 ")
   label_.configure(text=" 5 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "5 \n")
   txt1.config(state="disabled")


def leftClick6():
   print(" 6 ")
   label_.configure(text=" 6 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "6 \n")
   txt1.config(state="disabled")


def leftClick7():
   print(" 7 ")
   label_.configure(text=" 7 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "7 \n")
   txt1.config(state="disabled")


def leftClick8():
   print(" 8 ")
   label_.configure(text=" 8 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "8 \n")
   txt1.config(state="disabled")


def leftClick9():
   print(" 9 ")
   label_.configure(text=" 9 ")
   txt1.config(state="normal")
   txt1.insert(tk.INSERT, "9 \n")
   txt1.config(state="disabled")

def bdel():
    txt1.config(state="normal")
    txt1.insert(tk.END, "\n")
    txt1.config(state="disabled")

def odgovor():
   if (list6) != list5:
       print("Napačno...ponovi vajo!")
       print("napisal si.........", list6)
       print("pravilno je bilo...", list5)
       time.sleep(0.4)

       txt1.config(state="normal")
       txt1.insert(tk.INSERT, "odgovor\n")
       txt1.config(state="disabled")
   else:
       print("")
       print("BRAVO!!!!")
       print("napisal si ", list5)
       txt1.insert(0.0, odgovor)

       txt1.config(state="normal")
       txt1.insert(tk.INSERT, "plisti")
       txt1.config(state="disabled")

def close_window():
   root.destroy()
   exit()



def plisti():
    sys.stdout.write("\r" + str(list1))
    time.sleep(0.5)
    sys.stdout.write("\r" + str(list2))
    time.sleep(0.5)
    sys.stdout.write("\r" + str(list3))
    time.sleep(0.5)
    sys.stdout.write("\r" + str(list4))
    time.sleep(0.5)
    sys.stdout.write("\r" + str(list5))
    time.sleep(0.5)
    sys.stdout.write("\r" + str(abc))
    time.sleep(0.5)


    a1 = int(input("enter: "))
    list6.append(a1)
    a2 = int(input("enter: "))
    list6.append(a2)
    a3 = int(input("enter: "))
    list6.append(a3)
    a4 = int(input("enter: "))
    list6.append(a4)
    a5 = int(input("enter: "))
    list6.append(a5)
    time.sleep(0.5)



    odgovor()



txt1 = Text(root, width=30, height=4, bg="white")
txt1.grid(row=12, column=0, columnspan=4)

txt2 =Entry(root, width=3).grid(row=11, column=0, sticky=W)





b1 = Button(root, text=" 1 ", command=leftClick1, height=5, width=10)
b1.grid(row=2, column=0)

b2 = Button(root, text=" 2 ", command=leftClick2, height=5, width=10)
b2.grid(row=2, column=1)

b3 = Button(root, text=" 3 ", command=leftClick3, height=5, width=10)
b3.grid(row=2, column=2)

b4 = Button(root, text=" 4 ", command=leftClick4, height=5, width=10)
b4.grid(row=3, column=0)

b5 = Button(root, text=" 5 ", command=leftClick5, height=5, width=10)
b5.grid(row=3, column=1)

b6 = Button(root, text=" 6 ", command=leftClick6, height=5, width=10)
b6.grid(row=3, column=2)

b7 = Button(root, text=" 7 ", command=leftClick7, height=5, width=10)
b7.grid(row=4, column=0)

b8 = Button(root, text=" 8 ", command=leftClick8, height=5, width=10)
b8.grid(row=4, column=1)

b9 = Button(root, text=" 9 ", command=leftClick9, height=5, width=10)
b9.grid(row=4, column=2)

def b12():
   b12 = Button(text=" DELETE ", fg="black", bg="red", font=20, height=1, width=6, command=bdel)
   b12.grid(row=12, column=5)

b12()

label_ = Label(root, text=plisti)
label_.grid(row=6, column=0, columnspan=3)

klik = Button(root, text="START", font=10, fg="black", bg="green", command=plisti, height=1, width=26)
klik.place(x=0, y=0)

exi = Button(root, text="EXIT", width=40, bg="red", command=close_window).grid(row=15,column=0, sticky=S, columnspan=8)

# enter
# b11 = Button(text="ENTER", fg="black", bg="green", command=ent, font=10, height=1, width=6 ).grid(row=5, column=5)





frame = Frame(root)
frame.bind("<Button-1>", leftClick)
frame.grid(row=0, column=0)


root.mainloop()
