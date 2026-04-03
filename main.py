import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from infomodule import numinfo


placeholder = "Example : 03400000000"
root = tk.Tk()
root.title("Phone Number Information")
root.resizable(False, False)

style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

leftframe = ttk.Frame(frame)
leftframe.grid(row=0, column=0)


def print_data():
    num = inp_number.get()
    data = numinfo(num)
    if data['status'] == 'success':
        name = ttk.Label(data_show, text=f"Name : {data['name']}")
        name.grid(row=0, column=0, sticky="w")
        number = ttk.Label(data_show, text=f"Number : {data['number']}")
        number.grid(row=1, column=0, sticky="w")
        gender = ttk.Label(data_show, text=f"Gender : {data['gender']}")
        gender.grid(row=2, column=0, sticky="w")
        operator = ttk.Label(data_show, text=f"Operaor : {data['operator']}")
        operator.grid(row=3, column=0, sticky="w")
        cnic = ttk.Label(data_show, text=f"CNIC : {data['cnic']}")
        cnic.grid(row=4, column=0, sticky="w")
        address = ttk.Label(data_show, text=f"Address : {data['address']}")
        address.grid(row=5, column=0, pady=2, sticky="w")
    else:messagebox.showerror("error", "Data not found in database")

def on_focus_in(event):
    if inp_number.get() == placeholder:
        inp_number.delete(0, "end")
        inp_number.config(foreground="white")

def on_focus_out(event):
    if not inp_number.get():
        inp_number.insert(0, placeholder)
        inp_number.config(foreground="grey")

infoframe = ttk.Frame(leftframe)
infoframe.grid(row=0, column=0, padx=5, pady=5)

numlable = ttk.Label(infoframe, text="Input number")
numlable.grid(row=0, column=0, sticky="ew")




inp_number = ttk.Entry(infoframe)

inp_number.insert(0, placeholder)
inp_number.config(foreground="grey")
inp_number.bind("<FocusIn>", on_focus_in)
inp_number.bind("<FocusOut>", on_focus_out)
inp_number.grid(row=1, column=0, sticky="ew", padx=(0, 5), pady=5)

inbton = ttk.Button(infoframe, text="Search", command=print_data)
inbton.grid(row=1, column=1, sticky="w", padx=2, pady=5)

data_show = ttk.Labelframe(leftframe, text="Target Information", padding=(20, 10))
data_show.grid(row=1, column=0, padx=20, pady=20)





root.mainloop()


