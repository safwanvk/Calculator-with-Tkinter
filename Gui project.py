from tkinter import *

expression = ''


def press(num):
    global expression
    expression = expression + str(num)
    display.set(expression)


def result():
    try:
        global expression
        total = str(eval(expression))
        display.set(expression + '=' + total)
        expression = ''
    except:
        display.set('error')
        expression = ''


def clear():
    global expression
    display.set('')
    expression = ''


if __name__ == "__main__":
    window = Tk()
    window.geometry('300x300')
    window.title('calculator')
    window.configure(bg='black')

    display = StringVar()
    display_field = Label(window, textvariable=display)
    display_field.grid(columnspan=4, ipadx=70)
    display.set('|')

    btn7 = Button(window, text='7', bg='grey', fg='white', command=lambda: press(7), height=1, width=5)
    btn8 = Button(window, text='8', fg='white', command=lambda: press(8), height=1, width=5, bg='grey')
    btn9 = Button(window, text='9', fg='white', command=lambda: press(9), height=1, width=5, bg='grey')
    btn_div = Button(window, text='/', fg='white', command=lambda: press('/'), height=1, width=5, bg='grey')
    btn4 = Button(window, text='4', fg='white', command=lambda: press(4), height=1, width=5, bg='grey')
    btn5 = Button(window, text='5', fg='white', command=lambda: press(5), height=1, width=5, bg='grey')
    btn6 = Button(window, text='6', fg='white', command=lambda: press(6), height=1, width=5, bg='grey')
    btn_mul = Button(window, text='x', fg='white', command=lambda: press('*'), height=1, width=5, bg='grey')
    btn1 = Button(window, text='1', fg='white', command=lambda: press(1), height=1, width=5, bg='grey')
    btn2 = Button(window, text='2', fg='white', command=lambda: press(2), height=1, width=5, bg='grey')
    btn3 = Button(window, text='3', fg='white', command=lambda: press(3), height=1, width=5, bg='grey')
    btn_min = Button(window, text='-', fg='white', command=lambda: press('-'), height=1, width=5, bg='grey')
    btn0 = Button(window, text='0', fg='white', command=lambda: press(0), height=1, width=5, bg='grey')
    btn_des = Button(window, text='.', fg='white', command=lambda: press('.'), height=1, width=5, bg='grey')
    btn_plus = Button(window, text='+', fg='white', command=lambda: press('+'), height=1, width=5, bg='grey')
    btn_res = Button(window, text='=', fg='white', command=result, height=1, width=5, bg='blue')
    btn_clr = Button(window, text='C', fg='white', command=clear, height=1, width=5, bg='grey')

    btn7.grid(row=1, column=0)
    btn8.grid(row=1, column=1)
    btn9.grid(row=1, column=2)
    btn_div.grid(row=1, column=3)
    btn4.grid(row=2, column=0)
    btn5.grid(row=2, column=1)
    btn6.grid(row=2, column=2)
    btn_mul.grid(row=2, column=3)
    btn1.grid(row=3, column=0)
    btn2.grid(row=3, column=1)
    btn3.grid(row=3, column=2)
    btn_min.grid(row=3, column=3)
    btn0.grid(row=4, column=0)
    btn_des.grid(row=4, column=1)
    btn_plus.grid(row=4, column=2)
    btn_res.grid(row=4, column=3)
    btn_clr.grid(row=1, column=4)

    window.mainloop()
