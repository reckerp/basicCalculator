from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(background="#E3E3E3")
eq = ""


def clear():
    entry.delete(0, END)

def back_clear():
    current = entry.get()
    current = current[:-1]
    entry.delete(0, END)
    entry.insert(0, str(current))

def num(n):
    global eq
    current = entry.get()
    eq = current + n
    entry.delete(0, END)
    entry.insert(0, eq)

def equal():
    global eq
    try:
        equal = eval(eq)
        entry.delete(0, END)
        entry.insert(0, equal)
    except:
        entry.delete(0, END)
        entry.insert(0, "ERROR")



entry = Entry(root, width=18, borderwidth=4, bg="#535353", fg="white", font=("Helvetica", 40))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_ac = Button(root, text="AC", padx=40.5, pady=20, command=clear)
btn_ac.grid(row=1, column=0)

btn_back = Button(root, text="<-", padx=42, pady=20, command=back_clear)
btn_back.grid(row=1, column=1)

btn_modulo = Button(root, text="%", padx=44, pady=20, command=lambda: num("%"))
btn_division = Button(root, text="÷", padx=44, pady=20, command=lambda: num("/"))
btn_multiplication = Button(root, text="x", padx=45, pady=20, command=lambda: num("*"))
btn_addition = Button(root, text="+", padx=44, pady=20, command=lambda: num("+"))
btn_subtraction = Button(root, text="-", padx=45, pady=20, command=lambda: num("-"))
btn_comma = Button(root, text=".", padx=48, pady=20, command=lambda: num("."))
btn_equal = Button(root, text="=", padx=44, pady=20, command=equal)

btn_modulo.grid(row=1, column=2, pady=5)
btn_division.grid(row=1, column=3, pady=5)
btn_multiplication.grid(row=2, column=3, pady=5)
btn_addition.grid(row=3, column=3, pady=5)
btn_subtraction.grid(row=4, column=3, pady=5)
btn_comma.grid(row=5, column=2, pady=5)
btn_equal.grid(row=5, column=3, pady=5)



btn_1 = Button(root, text=1, padx=45, pady=20, command=lambda: num("1"))
btn_2 = Button(root, text=2, padx=45, pady=20, command=lambda: num("2"))
btn_3 = Button(root, text=3, padx=45, pady=20, command=lambda: num("3"))

btn_4 = Button(root, text=4, padx=45, pady=20, command=lambda: num("4"))
btn_5 = Button(root, text=5, padx=45, pady=20, command=lambda: num("5"))
btn_6 = Button(root, text=6, padx=45, pady=20, command=lambda: num("6"))

btn_7 = Button(root, text=7, padx=45, pady=20, command=lambda: num("7"))
btn_8 = Button(root, text=8, padx=45, pady=20, command=lambda: num("8"))
btn_9 = Button(root, text=9, padx=45, pady=20, command=lambda: num("9"))

btn_0 = Button(root, text=0, padx=101, pady=20, command=lambda: num("0"))

btn_1.grid(row=4, column=0, pady=5)
btn_2.grid(row=4, column=1, pady=5)
btn_3.grid(row=4, column=2, pady=5)

btn_4.grid(row=3, column=0, pady=5)
btn_5.grid(row=3, column=1, pady=5)
btn_6.grid(row=3, column=2, pady=5)

btn_7.grid(row=2, column=0, pady=5)
btn_8.grid(row=2, column=1, pady=5)
btn_9.grid(row=2, column=2, pady=5)

btn_0.grid(row=5, column=0, columnspan=2, pady=5)



root.mainloop()