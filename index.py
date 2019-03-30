from tkinter import *
window = Tk()
window.configure(bg = "#A5FFAC")
window.title("Menu")
window.geometry("400x800")
window.resizable(0,0)

def openMenu():
    menu = Tk()
    menu.configure(bg="#9896E8")
    # #cecece
    menu.title("Menu")
    menu.geometry("1000x800")
    menu.resizable(0, 0)
    menu.mainloop()


label1 = Label(window, text="Restaurant",font="Tahoma 20",bg="#A5FFAC",fg="black")
button1= Button(window, text="Открыть Меню", font = "Tahoma 20",bg="#9896E8",fg = "white",command=openMenu)
button2= Button(window, text="Добавить заказ", font = "Tahoma 20",bg="#9896E8",fg = "white")
button3= Button(window, text="Посмотреть все заказы", font = "Tahoma 20",bg="#9896E8",fg = "white")
button4= Button(window, text="Дневной зароботок", font = "Tahoma 20",bg="#9896E8",fg = "white")

label1.pack(pady = 10)
button1.pack(pady = 10)
button2.pack(pady = 10)
button3.pack(pady = 10)
button4.pack(pady = 10)
window.mainloop()