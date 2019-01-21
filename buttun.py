import tkinter as tk

def write_slogan():
    print("Tkinter is easy")

root = tk.Tk()

frm = tk.Frame(root)
frm.pack()

btn = tk.Button(frm,
                text="QUIT",
                fg="red",
                font="14",
                command=quit)

btn.pack(side= tk.LEFT)

slogan = tk.Button(frm,
                   text = "HELLO",
                   fg = "blue",
                   font = "16",
                   command = write_slogan)

slogan.pack(side = tk.LEFT)
root.mainloop()