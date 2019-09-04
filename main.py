import tkinter as tk
from tkinter import simpledialog, ttk
import tkinter.messagebox

root = tk.Tk()
root.withdraw()
text = simpledialog.askstring(title="Text",
                              prompt="Insert Text")
app = tk.Tk()
# choice = ""

app.title("sENSITIVE-cASE")
labelTop = ttk.Label(app,
                     text="Choose the desired action")
labelTop.grid(column=0, row=0)


# Button Action
def click():
    if choices.get() == "swap case":
        result = str.swapcase(text)
        print(result)
        tkinter.messagebox.showinfo("Results", result + " Copy from terminal")
        # root2 = tk.Tk()
        # root2.withdraw()
        # T = tk.Text(root, height=2, width=30)
        # T.pack()
        # T.insert(tk.END, result)
        # tk.mainloop()
    elif choices.get() == "all lowercase":
        result = text.lower()
        print(result)
        tkinter.messagebox.showinfo("Results", result + " Copy from terminal")
        # print(result)
        # root2 = tk.Tk()
        # root2.withdraw()
        # T = tk.Text(root, height=2, width=30)
        # T.pack()
        # T.insert(tk.END, result)
        # tk.mainloop()
    elif choices.get() == "all uppercase":
        result = text.upper()
        print(result)
        tkinter.messagebox.showinfo("Results", result +" \n(open from terminal if you want to copy it)")
        # print(result)
        # root2 = tk.Tk()
        # root2.withdraw()
        # T = tk.Text(root, height=2, width=30)
        # T.pack()
        # T.insert(tk.END, result)
        # tk.mainloop()
    else:
        # root2 = tk.Tk()
        # root2.withdraw()
        # T = tk.Text(root, height=2, width=30)
        # T.pack()
        # T.insert(tk.END, "Error, please enter a valid action.")
        # tk.mainloop()
        result = "Error, please enter a valid action."

    action.configure(text=result)


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
