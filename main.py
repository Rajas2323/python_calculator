from tkinter import *
from tkinter import ttk
from tkinter import messagebox

exp = ""

#Methods

def equalpress():

    try:
        total = str(eval(exp))

        equation.set(total)


        expression = ""


    except:

        equation.set("")
        expression = ""
        messagebox.showerror("Error", "There was an error in Input")

def press(num):
    global exp

    exp = exp + str(num)
    equation.set(exp)

def clear():
    global exp
    exp = ""
    equation.set("")

#Methods


width = 418
height = 480
root = Tk()
root.resizable(False, False)

root.geometry(f"{width}x{height}+{500}+{230}")
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
s = ttk.Style()
s.theme_use("xpnative")
print(s.theme_names())
s.configure('TButton', font="Calibiri 40", relief="flat")


# Buttons===============================================
button_1 = ttk.Button(root, text="1", takefocus=False, width=3, command=lambda : press(1))
button_2 = ttk.Button(root, text="2", takefocus=False, width=3, command=lambda : press(2))
button_3 = ttk.Button(root, text="3", takefocus=False, width=3, command=lambda : press(3))
button_4 = ttk.Button(root, text="4", takefocus=False, width=3, command=lambda : press(4))
button_5 = ttk.Button(root, text="5", takefocus=False, width=3, command=lambda : press(5))
button_6 = ttk.Button(root, text="6", takefocus=False, width=3, command=lambda : press(6))
button_7 = ttk.Button(root, text="7", takefocus=False, width=3, command=lambda : press(7))
button_8 = ttk.Button(root, text="8", takefocus=False, width=3, command=lambda : press(8))
button_9 = ttk.Button(root, text="9", takefocus=False, width=3, command=lambda : press(9))
button_10 = ttk.Button(root, text="0", takefocus=False, width=3, command=lambda : press(0))
button_11 = ttk.Button(root, text=".", takefocus=False, width=3, command=lambda : press('.'))
button_12 = ttk.Button(root, text="=", takefocus=False, width=3, command=equalpress)
button_13 = ttk.Button(root, text="+", takefocus=False, width=3, command=lambda : press('+'))
button_14 = ttk.Button(root, text="-", takefocus=False, width=3, command=lambda : press('-'))
button_15 = ttk.Button(root, text="x", takefocus=False, width=3, command=lambda : press('*'))
button_16 = ttk.Button(root, text="/", takefocus=False, width=3, command=lambda : press('/'))
button_17 = ttk.Button(root, text="C", takefocus=False, width=13, command=clear)

# Buttons===============================================

button_1.place(x=10, y=100)
button_2.place(x=110, y=100)
button_3.place(x=210, y=100)
button_4.place(x=10, y=175)
button_5.place(x=110, y=175)
button_6.place(x=210, y=175)
button_7.place(x=10, y=250)
button_8.place(x=110, y=250)
button_9.place(x=210, y=250)
button_10.place(x=110, y=325)
button_11.place(x=10, y=325)
button_12.place(x=210, y=325)
button_13.place(x=310, y=100)
button_14.place(x=310, y=175)
button_15.place(x=310, y=250)
button_16.place(x=310, y=325)
button_17.place(x=13, y=400)




# Input Box=============================================
equation = StringVar()
entry_1 = ttk.Entry(root, justify=RIGHT, font="Calibiri 35", width=15, textvariable=equation)
entry_1.focus()
entry_1.place(x=10, y=10)

# Input Box=============================================


root.mainloop()
