import tkinter as tk
import random

window = tk.Tk()
window.title('WINDOWS')
window.geometry("300x300")

label = tk.Label(window, text='любимая а ты меня любишь?)))')
label.place(relx = 0.5 ,rely = 0.5 ,anchor = "center")

click_count1=0
click_count2=0

def click1():
    global click_count1 
    click_count1 += 1
    if click_count1 == 1:
        label.config(text = "ну пиздец нахуй")
    elif click_count1 ==2:
        label.config(text = "пон")
    elif click_count1 == 5 :
        window.destroy()
    else :
        label.config(text = "...")
        newx = random.randint (0 , 220)
        newy = random.randint (0 , 220)
        button1.place (x = newx ,y = newy)


def click2():
    global click_count2 
    click_count2 +=1
    label.config (text="передумай плиз")
    newx1 = random.randint (0,220)
    newy2 = random.randint (0,220)
    button2.place(x = newx1 , y = newy2)
button1 = tk.Button(window , text = "мивинку больше" ,command = click1 )
button2 = tk.Button(window , text = "нет" ,command = click2)

button1.place(relx=0.70, rely=0.5)
button2.place(relx=0.2, rely=0.5)

window.mainloop()