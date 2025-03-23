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
                if re.match(pattern_list[i-1], data_list[i-1]):
                    pass
                else:
                    print('a')

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

    def update_function():
        what = entry_what.get()
        on = entry_on.get()
        who = entry_who.get()
        changes = False
        name_list = ['surname', 'age', 'belt', 'personal code', 'name']

        

        for i in range(5):
            if similar(name_list[i], what) == 1:
                what = name_list[i]
                #print(what)
                changes = True
                break
            elif similar(name_list[i], what)>0.6:
                if what == 'surname':
                    what = 'surname'
                    changes = True
                    #print(what)
                    break
                elif what == 'name':
                    what = 'name'
                    changes = True
                    #print(what)
                    break
                else:
                    response = messagebox.askyesno("", f"Do you mean {name_list[i]}?")
                    if response == True:
                        what = name_list[i]
                        changes = True
                        break
                    else:
                        pass

        if what == entry_what.get() and changes == False:
                messagebox.showinfo("", "Try again: remember program has only options like name, surname, age, belt, and personal code")



        name_patt = r'^[A-ZĀ-Ž][a-zā-ž]$'
        age_patt = r'\d[1-3]'
        belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
        pk_patt = r'\d[6]+[-]+\d[5]'


        if what == 'name' or what == 'surname':
            if re.match(name_patt, on):
                pass

                
            
                


    update_root = Toplevel()
    update_root.geometry('500x500+750+300')

    entry_what = Entry(update_root)
    entry_what.pack()

    entry_on = Entry(update_root)
    entry_on.pack()

    entry_who = Entry(update_root)
    entry_who.pack()

    Button(update_root, text='Save', padx=10, pady=10, command=update_function).pack()

main_root = Tk()
main_root.geometry("500x500+750+300")
main_root.resizable(width=False, height=False)



registration = Button(main_root, text="Registration", padx=10, pady=10, command=registration_root_function).pack()
update = Button(main_root, text="Update", padx=10, pady=10, command=update_root_function).pack()


main_root.mainloop()