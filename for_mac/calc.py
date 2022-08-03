import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    try:
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
    except IndexError:
        calc.insert(0, '0')
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)
    calc['state'] = tk.DISABLED


def add_operation(oper):
    calculate()
    value = calc.get()
    try:
        if value[-1] in '+-*/':
            value += value[:-1]
    except IndexError:
        calc.insert(0, '0')
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + oper)
    calc['state'] = tk.DISABLED


def calculate():
    value = calc.get()
    try:
        if value[-1] in '+-*/':
            value = value + value[:-1]
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, eval(value))
    except (NameError, SyntaxError, IndexError):
        calc.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo('ZeroDivisionError', f'You cannot division by zero' '\n'
                                                 'Try again!')
        calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def edit():
    calc['state'] = tk.NORMAL
    value = calc.get()
    value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 20, 'bold'), command=lambda: add_digit(digit))


def make_digit_operation(oper):
    return tk.Button(text=oper, bd=5, font=('Arial', 20, 'bold'), fg='#006600', command=lambda: add_operation(oper))


def make_calc_operation(oper):
    return tk.Button(text=oper, bd=5, font=('Arial', 20, 'bold'), fg='#006600', command=calculate)


def make_clear_operation(oper):
    return tk.Button(text=oper, bd=5, font=('Arial', 20, 'bold'), fg='#006600', command=clear)


def press_key(event):
    print(repr(event))
    if event.char.isdigit() or event.char == '.':
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    if event.keycode in (402653245, 603979789):
        calculate()
    if event.keycode == 855638143:
        edit()


win = tk.Tk()
win.geometry(f'282x345+900+150')
win.resizable(False, False)
win.title('Calculator')
win['bg'] = '#404040'
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 30, 'bold'), fg='white', width=16)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, sticky='we')

make_digit_button('7').grid(row=1, column=0, sticky='wesn')
make_digit_button('8').grid(row=1, column=1, sticky='wesn')
make_digit_button('9').grid(row=1, column=2, sticky='wesn')
make_digit_button('4').grid(row=2, column=0, sticky='wesn')
make_digit_button('5').grid(row=2, column=1, sticky='wesn')
make_digit_button('6').grid(row=2, column=2, sticky='wesn')
make_digit_button('1').grid(row=3, column=0, sticky='wesn')
make_digit_button('2').grid(row=3, column=1, sticky='wesn')
make_digit_button('3').grid(row=3, column=2, sticky='wesn')
make_digit_button('0').grid(row=4, column=0, columnspan=2, sticky='wesn')
make_digit_button('.').grid(row=4, column=2, sticky='wesn')

make_digit_operation('+').grid(row=1, column=3, sticky='wesn')
make_digit_operation('-').grid(row=2, column=3, sticky='wesn')
make_digit_operation('*').grid(row=3, column=3, sticky='wesn')
make_digit_operation('/').grid(row=4, column=3, sticky='wesn')

make_calc_operation('=').grid(row=5, column=2, columnspan=2, sticky='wesn')

make_clear_operation('C').grid(row=5, column=0, columnspan=2, sticky='wesn')

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.mainloop()
