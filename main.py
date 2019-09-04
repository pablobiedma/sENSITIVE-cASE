import tkinter as tk
from tkinter import simpledialog, ttk

root = tk.Tk()
root.withdraw()
text = simpledialog.askstring(title="Text",
                              prompt="Insert Text")
app = tk.Tk()
choice = ""


def sENSITIVE_cASE(text, choice):
    if choice == "swap case":
        result = str.swapcase(text)
        root2 = tk.Tk()
        root2.withdraw()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, result)
        tk.mainloop()

    elif choice == "all lowercase":
        result = text.lower()
        root2 = tk.Tk()
        root2.withdraw()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, result)
        tk.mainloop()
    elif choice == "all uppercase":
        result = text.upper()
        root2 = tk.Tk()
        root2.withdraw()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, result)
        tk.mainloop()
    else:
        root2 = tk.Tk()
        root2.withdraw()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, "Error, please enter a valid action.")
        tk.mainloop()


def check_cbox(event):
    global choice
    if choices.get() == 'swap case':
        choice = choices.get()
    if choices == "all lowercase":
        choice = choices.get()
    if choices.get() == "all uppercase":
        choice = choices.get()


app.title("sENSITIVE-cASE")
labelTop = ttk.Label(app,
                     text="Choose the desired action")
labelTop.grid(column=0, row=0)


# Button Action
def click():
    action.configure(text="chosen action is : " + choices.get())


# button Creation
action = ttk.Button(app, text="Click", command=click)
action.grid(column=1, row=1)
# Combobox Creation
number = tk.StringVar()
choices = ttk.Combobox(app, width=12, textvariable=number)
# Adding Values
choices['values'] = ("all uppercase", "swap case", "all lowercase")
choices.grid(column=0, row=1)
choices.current()
# Calling Main()
app.mainloop()
print(choices)

# change(text)
# def change(text, choice):
