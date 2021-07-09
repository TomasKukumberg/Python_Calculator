import tkinter as tk


def init_gui():

    bt = tk.Button(window, width=5, text='0', command=lambda:append_txt_display('0'))
    bt.grid(padx = 5, pady=5, column=0, row=1)
    bt = tk.Button(window, width=5, text='1', command=lambda:append_txt_display('1'))
    bt.grid(padx = 5, pady=5, column=1, row=1)
    bt = tk.Button(window, width=5, text='2', command=lambda:append_txt_display('2'))
    bt.grid(padx = 5, pady=5, column=2, row=1)
    bt = tk.Button(window, width=5, text='3', command=lambda:append_txt_display('3'))
    bt.grid(padx = 5, pady=5, column=3, row=1)
    bt = tk.Button(window, width=5, text='4', command=lambda:append_txt_display('4'))
    bt.grid(padx = 5, pady=5, column=0, row=2)
    bt = tk.Button(window, width=5, text='5', command=lambda:append_txt_display('5'))
    bt.grid(padx = 5, pady=5, column=1, row=2)
    bt = tk.Button(window, width=5, text='6', command=lambda:append_txt_display('6'))
    bt.grid(padx = 5, pady=5, column=2, row=2)
    bt = tk.Button(window, width=5, text='7', command=lambda:append_txt_display('7'))
    bt.grid(padx = 5, pady=5, column=3, row=2)
    bt = tk.Button(window, width=5, text='8', command=lambda:append_txt_display('8'))
    bt.grid(padx = 5, pady=5, column=0, row=3)
    bt = tk.Button(window, width=5, text='9', command=lambda:append_txt_display('9'))
    bt.grid(padx = 5, pady=5, column=1, row=3)
    bt = tk.Button(window, width=5, text='+', command=lambda:append_txt_display('+'))
    bt.grid(padx = 5, pady=5, column=2, row=3)
    bt = tk.Button(window, width=5, text='-', command=lambda:append_txt_display('-'))
    bt.grid(padx = 5, pady=5, column=3, row=3)
    bt = tk.Button(window, width=5, text='*', command=lambda:append_txt_display('*'))
    bt.grid(padx = 5, pady=5, column=0, row=4)
    bt = tk.Button(window, width=5, text='/', command=lambda:append_txt_display('/'))
    bt.grid(padx = 5, pady=5, column=1, row=4)
    bt = tk.Button(window, width=5, text='.', command=lambda:append_txt_display('.'))
    bt.grid(padx = 5, pady=5, column=2, row=4)
    bt = tk.Button(window, width=5, text='=', command=lambda: calc_result())
    bt.grid(padx = 5, pady=5, column=3, row=4)
    bt = tk.Button(window, width=5, text='DEL', command=lambda: del_last())
    bt.grid(padx = 5, pady=5, column=0, row=5)
    bt = tk.Button(window, width=5, text='C', command=lambda: flush_screen())
    bt.grid(padx = 5, pady=5, column=1, row=5)
    bt = tk.Button(window, width=5, text='%', command=lambda: append_txt_display('%'))
    bt.grid(padx = 5, pady=5, column=2, row=5)
    bt = tk.Button(window, width=5, text='**', command=lambda: append_txt_display('**'))
    bt.grid(padx = 5, pady=5, column=3, row=5)
    bt = tk.Button(window, width=5, text='(', command=lambda: append_txt_display('('))
    bt.grid(padx = 5, pady=5,  column=0, row=6)
    bt = tk.Button(window, width=5, text=')', command=lambda: append_txt_display(')'))
    bt.grid(padx = 5, pady=5, column=1, row=6)

def append_txt_display(i):
    if display.cget('text') == 'Error':
        display.config(text='' + str(i))
    else:
        input = display.cget("text")
        display.config(text=str(input) + str(i))

def calc_result():
    try:
        result = eval(display.cget("text"))
    except:
        result = 'Error'
    finally:
        display.config(text=result)

def flush_screen():
    display.config(text='')

def del_last():
    txt = display.cget("text")
    txt_str = (str(txt))[:len(str(display.cget("text"))) - 1]
    display.config(text=txt_str)

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Calculator')

    display = tk.Label(window, text='')
    display.grid(column=0, row=0, columnspan=4)

    init_gui()
    window.eval('tk::PlaceWindow . center')
    window.mainloop()
