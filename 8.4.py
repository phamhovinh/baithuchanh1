from tkinter import *
window= Tk()
window.title("welcome to likegeeks app")
window.geometry("350x200")
lbl=Label(window,text='hello')
lbl.grid(column=0,row=0)
def clicked():
    lbl.configure(text="button was clicked")
btn=Button(window,text="click me", command=clicked)
btn.grid(column=1,row=0)
window.mainloop()


