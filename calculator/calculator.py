from tkinter import *

# creating window
mw = Tk()
mw.title("Calculator")


def clear():
    db.delete(0, END)

list=['+','-','*','/']
first_num = 0
math = ''
math_sign=''

def calc(math_type,ms):
    global first_num, math,math_sign
    math_sign=ms
    first_num = db.get()
    clear()
    math = math_type
    for x in list:
        first_num=first_num.replace(x,'')
    db.insert(0,first_num+math_sign)


def equal():
    global first_num, math
    second_num = db.get().replace(first_num+math_sign,'')
    clear()
    if math == "add":
        result = int(first_num) + int(second_num)
    elif math == "sub":
        result = int(first_num) - int(second_num)
    if math == "mul":
        result = int(first_num) * int(second_num)
    if math == "div":
        result = int(first_num) / int(second_num)

    db.insert(0, str(result))



def clk_btn(num):
    cur_num = db.get()
    clear()
    final_num = cur_num + num
    db.insert(0, final_num)


db = Entry(mw, width=26, font=("Arial", 18), justify=RIGHT)
db.grid(padx=10, pady=10, columnspan=3)

btn_0 = Button(mw, text="0", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("0"))
btn_1 = Button(mw, text="1", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("1"))
btn_2 = Button(mw, text="2", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("2"))
btn_3 = Button(mw, text="3", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("3"))
btn_4 = Button(mw, text="4", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("4"))
btn_5 = Button(mw, text="5", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("5"))
btn_6 = Button(mw, text="6", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("6"))
btn_7 = Button(mw, text="7", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("7"))
btn_8 = Button(mw, text="8", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("8"))
btn_9 = Button(mw, text="9", padx=36, pady=10, font=("Arial", 14), command=lambda: clk_btn("9"))
btn_clear = Button(mw, text="clear", padx=80, pady=10, font=("Arial", 14), command=clear)
btn_add = Button(mw, text="+", padx=36, pady=10, font=("Arial", 14), command=lambda: calc("add","+"))
btn_sub = Button(mw, text="-", padx=36, pady=10, font=("Arial", 14), command=lambda: calc("sub","-"))
btn_mul = Button(mw, text="*", padx=36, pady=10, font=("Arial", 14), command=lambda: calc("mul","*"))
btn_div = Button(mw, text="/", padx=36, pady=10, font=("Arial", 14), command=lambda: calc("div","/"))
btn_equal = Button(mw, text="=", padx=36, pady=38, font=("Arial", 14), command=lambda: equal())

btn_0.grid(row=4, column=0, padx=2, pady=2)
btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_mul.grid(row=5, column=0, padx=2, pady=2)
btn_div.grid(row=5, column=1, padx=2, pady=2)

btn_add.grid(row=6, column=0, padx=2, pady=2)
btn_sub.grid(row=6, column=1, padx=2, pady=2)

btn_equal.grid(row=5, column=2, padx=2, pady=2, rowspan=2)
mw.mainloop()
