from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('calculator')
window.configure(bg='white')




def hello():
    print('button clicked')


btn7 = Button(window, text='7', command=hello)
btn8 = Button(window, text='8', command=hello)
btn9 = Button(window, text='9', command=hello)
btn_div = Button(window, text='/', command=hello)
btn4 = Button(window, text='4', command=hello)
btn5 = Button(window, text='5', command=hello)
btn6 = Button(window, text='6', command=hello)
btn_mul = Button(window, text='x', command=hello)
btn1 = Button(window, text='1', command=hello)
btn2 = Button(window, text='2', command=hello)
btn3 = Button(window, text='3', command=hello)
btn_min = Button(window, text='-', command=hello)
btn0 = Button(window, text='0', command=hello)
btn_dot = Button(window, text='.', command=hello)
btn_mod = Button(window, text='%', command=hello)
btn_plus = Button(window, text='+', command=hello)
btn_res = Button(window, text='=', command=hello)
btn_clr = Button(window, text='C', command=hello)


btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btn_div.grid(row=0, column=3)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn_mul.grid(row=1, column=3)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btn_min.grid(row=2, column=3)
btn0.grid(row=3, column=0)
btn_dot.grid(row=3, column=1)
btn_mod.grid(row=3, column=2)
btn_plus.grid(row=3, column=3)
btn_res.grid(row=0, column=4)
btn_clr.grid(row=0, column=5)


window.mainloop()
