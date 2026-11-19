import random
import tkinter as tk

window = tk.Tk()
window.title('Hello world')
window.geometry("500x500")

label = tk.Label (window ,text="Hello World!")
label.place(relx=0.5 ,rely = 0.5 , anchor= 'center')

click_count=0

newx=random.randint(0,200)
newy=random.randint(0,200)


def buttonclick ():
    global click_count
    click_count +=1
    if click_count == 1:
        label.config(text="HELLO WORLD!!!")
        button.place(x=newx ,y=newy)
    else:
        label.config(text="HEEEEELLOOOOOO WOOOOOORLD du arschloch")

def windowdestroy ():
    window.destroy()

    
button1=tk.Button(window ,text = "hello window" , command = buttonclick)
button1.place(relx= 0.5 ,rely= 0.6,anchor = 'center')

button2=tk.Button(window, text="X",command=windowdestroy )
button2.place(relx=1,rely=0 ,anchor = "ne")

window.mainloop()


