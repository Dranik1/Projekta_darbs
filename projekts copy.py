from tkinter import *
from tkinter import messagebox
import re
import sqlite3
from difflib import SequenceMatcher



conn = sqlite3.connect('dalibnieki.db')
cur = conn.cursor()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def registration_root_function():

    def registration_function():
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

            conn.execute("INSERT INTO Dalibnieks(name, surname, age, belt, pk) VALUES(?, ?, ?, ?, ?)", (name, surname, age, belt, pk))
            conn.commit()
            messagebox.showinfo('+', "Registration is complete")
        except Exception as e:
            messagebox.showerror("-", e)


    registration_root = Toplevel()
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

    Button(registration_root, text="Registrtion", command=registration_function).pack()

def update_root_function():
    update_root = Toplevel()

    entry_what = Entry(update_root)
    entry_what.pack()

    entry_on = Entry(update_root)
    entry_on.pack()

    Button(update_root, text='Save', padx=10, pady=10).pack()

main_root = Tk()
main_root.geometry("500x500+750+300")
main_root.resizable(width=False, height=False)



registration = Button(main_root, text="Registration", padx=10, pady=10, command=registration_root_function).pack()
update = Button(main_root, text="Update", padx=10, pady=10).pack()


main_root.mainloop()