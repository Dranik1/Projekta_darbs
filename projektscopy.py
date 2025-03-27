#Bibleoteku izsaukšana
from tkinter import *
from tkinter import messagebox
import re
import sqlite3
from difflib import SequenceMatcher
from tkcalendar.calendar_ import Calendar

#Datu bāzes atveršana
conn = sqlite3.connect('dalibnieki.db')
cur = conn.cursor()

#Funkcija kas pārbauda vai vārdi ir lidzīgi
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#funkcija reģistrācijas logam
def registration_root_function():

    #reģistracijas funkcija
    def registration_function():
        name = entry_name.get()
        surname = entry_surname.get()
        age = entry_age.get()
        belt = entry_belt.get()
        pk = entry_pk.get()

        data_list = [name, surname, age, belt, pk]

        name_list = ['name', 'surname', 'age', 'belt', 'personal code']

        name_patt = r'^[A-ZĀ-Ž][a-zā-ž]$'
        age_patt = r'\d{1,3}'
        belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
        pk_patt = r'\d{6}+[-]+\d{5}'

        pattern_list = [name_patt, name_patt, age_patt, belt_patt, pk_patt]


        #datu pareizrakstīšanas pārbaude
        try:
            for i in range(5):
                if re.match(pattern_list[i], data_list[i]):
                    pass
                else:
                    messagebox.showerror("ValueError", f"{name_list[i]} is in incorrect form")

            conn.execute("INSERT INTO Dalibnieks(name, surname, age, belt, pk) VALUES(?, ?, ?, ?, ?)", (name, surname, age, belt, pk))
            conn.commit()
            messagebox.showinfo('+', "Registration is complete")
        except Exception as e:
            messagebox.showerror("-", e)


    registration_root = Toplevel()
    registration_root.geometry('500x500+900+300')

    Label(registration_root, text="Ievadiet vardu (Daniils)").pack()
    entry_name = Entry(registration_root)
    entry_name.pack(padx=10, pady=5)

    Label(registration_root, text="Ievadiet uzvardu (Ivanovs)").pack()
    entry_surname = Entry(registration_root)
    entry_surname.pack(padx=10, pady=5)

    Label(registration_root, text="Ievadiet vecumu (18)").pack()
    entry_age = Entry(registration_root)
    entry_age.pack(padx=10, pady=5)

    Label(registration_root, text="Ievadiet jostu (4 Kyu)").pack()
    entry_belt = Entry(registration_root)
    entry_belt.pack(padx=10, pady=5)

    Label(registration_root, text="Ievadiet personas kodu (123456-12345)").pack()
    entry_pk = Entry(registration_root)
    entry_pk.pack(padx=10, pady=5)

    Button(registration_root, text="Registrtion", command=registration_function).pack(padx=10, pady=10)

#funkcija atjaunošanas logam
def update_root_function():

    #atjaunošanas funkcija
    def update_function():
        what = entry_what.get()
        on = entry_on.get()
        who = entry_who.get()
        changes = False
        name_list = ['surname', 'age', 'belt', 'personal code', 'name']

        
        #pārbaude kādu datu lietotājs grīb mainīt
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

        if changes == False:
                messagebox.showinfo("", "Try again: remember program has only options like name, surname, age, belt, and personal code")


        #pārbaude datu pareizrakstību
        name_patt = r'^[A-ZĀ-Ž][a-zā-ž]$'
        age_patt = r'\d[1-3]'
        belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
        pk_patt = r'\d[6]+[-]+\d[5]'


        if what == 'name':
            if re.match(name_patt, on):
                pass
            else:
                messagebox.showerror('', 'name error')
        elif what == 'surname':
            if re.match(name_patt, on):
                pass
            else:
                messagebox.showerror('', 'surname error')
        elif what == 'age':
            if re.match(age_patt, on):
                pass
            else:
                messagebox.showerror('', 'age error')
        elif what == 'belt':
            if re.match(belt_patt, on):
                pass
            else:
                messagebox.showerror('', 'belt error')
        elif what == 'personal code':
            if re.match(pk_patt, on):
                pass
            else:
                messagebox.showerror('', 'personal code error')
        else:
            messagebox.showerror("", "Unexpected error")

        
        #Izmaiņas datu bāzē
        conn.execute("UPDATE Dalibnieks SET ? = ? WHERE pk = ?;", (what, on, who))
        conn.commit()

        messagebox.showinfo("Data is updated")
    


    update_root = Toplevel()
    update_root.geometry('500x500+750+300')

    Label(update_root, text="Ievadiet ko jūs gribāt izmainīt (name, surname, age, belt, pk)").pack()
    entry_what = Entry(update_root)
    entry_what.pack(padx=10, pady=5)

    Label(update_root, text="Ievadiet uz ko jūs gribāt izmainīt").pack()
    entry_on = Entry(update_root)
    entry_on.pack(padx=10, pady=5)

    Label(update_root, text="Ievadiet kam jūs gribāt to izmainīt (personas kodu)").pack()
    entry_who = Entry(update_root)
    entry_who.pack(padx=10, pady=5)

    Button(update_root, text='Save', padx=10, pady=10, command=update_function).pack(padx=10, pady=10)

#funkcija dzēšanas logam
def delete_root_function():

    def delete_function():
        pk = entry_pk.get()

        try:
            conn.execute("Delete from Dalibnieks where pk = ?", (pk, ))
            conn.commit()
            messagebox.showinfo("", "Deletion is complete")
        except Exception as e:
            messagebox.showerror("", e)
    
    delete_root = Toplevel()
    delete_root.geometry("500x500+750+300")
    delete_root.resizable(width=False, height=False)

    Label(delete_root, text="Ievadiet kas jūš gribāt izdzēst (personas kodu)").pack()
    entry_pk = Entry(delete_root)
    entry_pk.pack(padx=10, pady=5)

    Button(delete_root, text="Delete", padx=10, pady=10, command=delete_function).pack(padx=10, pady=10)

#funkcija atrašanas logam
def find_root_function():

    def find_function():
        pk = entry_pk.get()
        pk_patt = r'\d{6}+[-]+\d{5}'

        try:
            if re.match(pk_patt, pk):
                cur.execute("Select * from Dalibnieks where pk = ?", (pk, ))
                result = cur.fetchone()
                if result == None:
                    messagebox.showinfo("", "There is no perticipants with such personal code")
                else:
                    messagebox.showinfo("", result)
            
            else:
                messagebox.showerror("ValueError", "Please write personal code correctly")
        
        except Exception as e:
            messagebox.showerror("Unexpected Error", e)

    find_root = Toplevel()
    find_root.geometry("500x500+750+300")
    find_root.resizable(width=False, height=False)

    Label(find_root, text="Ievadiet personas kodu").pack()
    entry_pk = Entry(find_root)
    entry_pk.pack(padx=10, pady=5)

    Button(find_root, text="Find", padx=10, pady=10, command=find_function).pack(padx=10, pady=10)

def calendar_root_function():
    calendar_root = Toplevel()
    calendar_main = Calendar(calendar_root)
    calendar_main.pack()

#Galvenais logs
main_root = Tk()
main_root.geometry("500x500+750+300")
main_root.resizable(width=False, height=False)



registration = Button(main_root, text="Registration", padx=10, pady=10, command=registration_root_function).pack(padx=10, pady=10)
update = Button(main_root, text="Update", padx=10, pady=10, command=update_root_function).pack(padx=10, pady=10)
find = Button(main_root, text="Find", padx=10, pady=10, command=find_root_function).pack(padx=10, pady=10)
delete = Button(main_root, text="Delete", padx=10, pady=10, command=delete_root_function).pack(padx=10, pady=10)
cal = Button(main_root, text="Calendar", padx=10, pady=10, command=calendar_root_function).pack(padx=10, pady=10)


main_root.mainloop()