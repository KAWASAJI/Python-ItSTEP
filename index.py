from tkinter import *
window = Tk()
window.configure(bg = "#A5FFAC")
window.title("Main")
window.geometry("400x800")
window.resizable(0,0)

def openMenu():
    menu = Tk()
    menu.configure(bg="#9896E8")
    # #cecece
    menu.title("Menu")
    menu.geometry("1000x800")
    menu.resizable(0, 0)

    btn1 = Button(menu, text="Add +", bg="#FFB2B2", height=2, width=10)
    btn2 = Button(menu, text="Delete -", bg="#FFB2B2", height=2, width=10)
    btn3 = Button(menu, text="Show Orders", bg="#FFB2B2", height=2, width=10)
    btn4 = Button(menu, text="Daily", bg="#FFB2B2", height=2, width=10)

    btn1.grid(row=1, column=1, pady=10)
    btn2.grid(row=2, column=1, pady=10)
    btn3.grid(row=3, column=1, pady=10)
    btn4.grid(row=4, column=1, pady=10)
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