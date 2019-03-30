from tkinter import *
window = Tk()
window.configure(bg="#A5FFAC")
window.title("Main")
window.geometry("400x800")
window.resizable(0, 0)

def openOrders():
    def exit():
        order.destroy()
    order = Tk()
    order.configure(bg="#9896E8")
    # #cecece
    order.title("Add Order")
    order.geometry("1000x800")
    order.resizable(0, 0)

    btn1 = Button(order, text="Add +", bg="#FFB2B2", height=2, width=10)
    btn2 = Button(order, text="Show menu", bg="#FFB2B2", height=2, width=10)
    btn3 = Button(order, text="Show Orders", bg="#FFB2B2", height=2, width=10)
    btn4 = Button(order, text="Daily", bg="#FFB2B2", height=2, width=10)
    btn5 = Button(order, text="Exit", bg="#FFB2B2", height=2, width=10, command=exit)
    btn1.grid(row=1, column=1, pady=10)
    btn2.grid(row=2, column=1, pady=10)
    btn3.grid(row=3, column=1, pady=10)
    btn4.grid(row=4, column=1, pady=10)
    btn5.grid(row=4, column=1, pady=10)
    order.mainloop()

def openMenu():
    def openDrinks():
        label1.pack()
        btn2.pack()
    def openFood():
        label2.pack()
    drinks = "\tИмя-Цена\tID\n" \
           "\tСок-1\t\t[1]\n" \
           "\tВода-1\t\t[2]\n" \
           "\tКола-2\t\t[3]\n" \
           "\tМолоко-2\t\t[4]" \

    food = "\tИмя-Цена\tID\n" \
             "\tСок-1\t\t[1]\n" \
             "\tВода-1\t\t[2]\n" \
             "\tКола-2\t\t[3]\n" \
             "\tМолоко-2\t\t[4]"
    menu =Tk()
    menu.title("Menu")
    menu.geometry("400x800")
    menu.resizable(0, 0)
    btn1 = Button(menu, text='Напитки', command=openDrinks, bg="#FFB2B2", height=2, width=10)
    btn2 = Button(menu, text='Еда', command=openFood, bg="#FFB2B2", height=2, width=10)
    label1 = Label(menu, text=drinks, font="Arial")
    label2 = Label(menu, text=food, font="Arial")

    btn1.pack()

    menu.mainloop()

label1 = Label(window, text="Ali Restaraunt", font="Tahoma 20", bg="#A5FFAC", fg="black")
label2 = Label(window, text="Ali(c)2019 | All rights resrved", bg="#A5FFAC", fg="black")
button1 = Button(window, text="Открыть Меню", font="Tahoma 20", bg="#9896E8", fg="white", command=openMenu)
button2 = Button(window, text="Добавить заказ", font="Tahoma 20", bg="#9896E8", fg="white", command=openOrders)
button3 = Button(window, text="Посмотреть все заказы", font="Tahoma 20", bg="#9896E8", fg="white")
button4 = Button(window, text="Дневной зароботок", font="Tahoma 20", bg="#9896E8", fg="white")

label1.pack(pady=10)
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
label2.pack(side=BOTTOM)
window.mainloop()