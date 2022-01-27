from tkinter import *
import random

root = Tk()
root.title('Rolling Dice')
root.geometry('700x450')
root.config(bg='white')

def roll():
    text = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f"{random.choice(text)}{random.choice(text)}",bg='white')
    label.pack()

label = Label(root,text='',font=('times',260))

btn = Button(root,text='Lets roll...',font=260,command=roll,width=30,height=2)
btn.pack(anchor=CENTER,pady=10)

root.mainloop()