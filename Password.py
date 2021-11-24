import random

from tkinter import *

from functools import partial

top = Tk()
top.title("Password Generator")
top.geometry("800x600")

def generate(upr, lwr, nbr, sbl):    
    upper=""
    lower=""
    numbers=""
    symbols=""
    
    if upr.get()==1:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if lwr.get()==1:
        lower = "abcdefghijklmnopqrstuvwxyz"

    if nbr.get()==1:
        numbers = "0123456789"

    if sbl.get()==1:
        symbols = "!@#$%&*()./_"  

    bigString = lower + upper + numbers + symbols
    
    length = 8
    password="".join(random.sample(bigString, length))
    print("Strong Password: ", password)


upr = IntVar()
lwr = IntVar()
nbr = IntVar()
sbl = IntVar()


c1 = Checkbutton(top, text="Upper", variable=upr, onvalue=1, offvalue=0).place(x=100, y=50)

c2 = Checkbutton(top, text="Lower", variable=lwr, onvalue=1, offvalue=0).place(x=100, y=150)

c3 = Checkbutton(top, text="Numbers", variable=nbr, onvalue=1, offvalue=0).place(x=100, y=250)

c4 = Checkbutton(top, text="Symbols", variable=sbl, onvalue=1, offvalue=0).place(x=100, y=350)

generate = partial(generate, upr, lwr, nbr, sbl)
b = Button(top, text="Generate Password", command=generate).place(x=200, y=400)


top.mainloop()
