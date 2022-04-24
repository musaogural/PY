from __future__ import division
from tkinter import *

depo = ""
pencere = Tk()
pencere.resizable(width=FALSE,height=FALSE)
#pencere.iconbitmap("cal.ico")
ekran = Entry(width=20)
ekran.grid(row=0, column=0, columnspan=3,ipady=4)

def hesapla(tus):
    global depo
    if tus in "0123456789":
        ekran.insert(END,tus)
        depo = depo + tus
    if tus in "+-/*":
        depo = depo + tus
        ekran.delete(0,END)
    if tus == "=":
        ekran.delete(0,END)
        hesap = eval(depo,{"__builtins__":None},{})
        depo = str(hesap)
        ekran.insert(END,depo)
    if tus == "C":
        ekran.delete(0,END)
        depo = ""

liste = [\
            "9", "8", "7",
            "6", "5", "4",
            "3", "2", "1",
            "0", "+", "-",
            "/", "*", "=",
            "C"]

sira = 1
sutun = 0
for i in liste:
    komut = lambda x=i: hesapla(x)
    Button(text=i,width=5,relief=GROOVE,command=komut).grid(row=sira, column=sutun) 
    sutun += 1
    if sutun > 2:
        sutun = 0
        sira += 1

mainloop()
