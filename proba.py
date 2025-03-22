'''import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print(screensize)'''

from tkinter import *
from tkinter import messagebox
import re

def check():
    name = entry_name.get()
    surname = entry_surname.get()
    age = entry_age.get()
    belt = entry_belt.get()
    pk = entry_pk.get()

    data_list = [name, surname, age, belt, pk]

    name_patt = r'^[A-ZĀ-Ž][a-zā-ž]$'
    age_patt = r'\d[1-3]'
    belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
    pk_patt = r'\d[6]+[-]+\d[5]'

    pattern_list = [name_patt, name_patt, age_patt, belt_patt, pk_patt]

    try:
        for i in range(5):
            re.match(pattern_list[i-1], data_list[i-1])
        messagebox.showinfo('+', "+")
    except Exception as e:
        messagebox.showerror("-", e)


registration_root = Tk()
registration_root.geometry('500x500+900+300')

entry_name = Entry(registration_root)
entry_name.pack()

entry_surname = Entry(registration_root)
entry_surname.pack()

entry_age = Entry(registration_root)
entry_age.pack()

entry_belt = Entry(registration_root)
entry_belt.pack()

entry_pk = Entry(registration_root)
entry_pk.pack()

Button(registration_root, text="Check", command=check).pack()

registration_root.mainloop()