import random as r
import tkinter
from tkinter import *
from typing import Sized


def AddCap(Cap): return Cap[r.randint(0, len(Cap))]
def AddNoCap(NoCap): return NoCap[r.randint(0, len(NoCap))]
def AddCar(Car): return Car[r.randint(0, len(Car))]
def AddNum(Num): return Num[r.randint(0, len(Num))]


caracters = {
    "Cap": "ABCDEFGHIJKLMNOPQRSTUVWXYUZ",
    "NoCap": "abcdefghijklmnopqrstuvwxyz",
    "Car": "~=-!@#$%^&*()_+{[}]\;<>?",
    "Num": "01223456789"
}

Password = ""


def CreatePass(n, inpuu):
    while (n > 0):
        Password = ""
        State = 0
        for i in range(n):
            State = r.randint(0, 4)
            if (State == 0):
                Password += AddCap(caracters["Cap"])
            elif (State == 1):
                Password += AddNoCap(caracters["NoCap"])
            elif (State == 2):
                Password += AddCar(caracters["Car"])
            else:
                Password += AddNum(caracters["Num"])
        inpuu.delete(0, 'end')
        inpuu.insert(0, Password)


def APP(IN):
    n = 0
    n = int(IN.get())
    if (n > 0):
        CreatePass(n, IN)
    elif (n <= 0 and not IN.get().isnumeric):
        print("DUMBASS U WASTED MY TIME ! YOU SHOULD ADD A NUMBER IN THE INPUT U STUPID ! THAT'S WHY YOU'RE ADOPTEDD")
        exit()
    else:
        pass


# GUI
root = Tk()
TextTitle = Label(root, text="ENTER PASS LENGTH", padx=20,
                  pady=20, fg="#333")
TextTitle.pack()
Inp = Entry(root, width=40, justify='center', )
Inp.pack(ipady=7)
Sub = Button(root, text="Generate", padx=45,
             pady=10, borderwidth=1, bg="#339966", fg="#fff", command=lambda: APP(Inp))
Sub.pack(pady=20,)
root.geometry("500x200")
root.mainloop()
