#Bibleoteku izsaukšana
from tkinter import *
from tkinter import messagebox, ttk
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

        name_patt = r'^[A-ZĀ-Ž]{1}[a-zā-ž]+$'
        age_patt = r'\d{1,3}'
        belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
        pk_patt = r'\d{6}-\d{5}'
        #pk_patt = r'\d'

        pattern_list = [name_patt, name_patt, age_patt, belt_patt, pk_patt]


        #datu pareizrakstīšanas pārbaude
        try:
            for i in range(len(data_list)):
                print(i)
                if re.match(pattern_list[i], data_list[i]):
                    print("b")
                else:
                    messagebox.showerror("ValueError", f"{name_list[i]} is in incorrect form")
                    break
            if i == 4:
                if where == "rezekne":
                    conn.execute("INSERT INTO Dalibnieki_rezekne(name, surname, age, belt, pk) VALUES(?, ?, ?, ?, ?)", (name, surname, age, belt, pk))
                elif where == "kraslava":
                    conn.execute("INSERT INTO Dalibnieki_kraslava(name, surname, age, belt, pk) VALUES(?, ?, ?, ?, ?)", (name, surname, age, belt, pk))
                elif where == "preili":
                    conn.execute("INSERT INTO Dalibnieki_preili(name, surname, age, belt, pk) VALUES(?, ?, ?, ?, ?)", (name, surname, age, belt, pk))
                else:
                    messagebox.showerror("", "Unexpexted error")
                            
                conn.commit()
                messagebox.showinfo('+', "Registration is complete")

        except Exception as e:
            messagebox.showerror("-", e)

        registration_root.destroy()


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

    Button(registration_root, text="Registration", command=registration_function).pack(padx=10, pady=10)

#funkcija atjaunošanas logam
def update_root_function():
    name_list = ['surname', 'age', 'belt', 'name']
    #atjaunošanas funkcija
    def update_function():
        what = entry_what.get()
        on = entry_on.get()
        who = entry_who.get()


        #pārbaude datu pareizrakstību
        name_patt = r'^[A-ZĀ-Ž]{1}[a-zā-ž]+$'
        age_patt = r'\d{1,3}'
        belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'



        
        if where == "rezekne":
            if what == 'name':
                if re.match(name_patt, on):
                    conn.execute("UPDATE Dalibnieki_rezekne SET name = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'name error')
            elif what == 'surname':
                if re.match(name_patt, on):
                    conn.execute("UPDATE Dalibnieki_rezekne SET surname = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'surname error')
            elif what == 'age':
                if re.match(age_patt, on):
                    conn.execute("UPDATE Dalibnieki_rezekne SET age = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'age error')
            elif what == 'belt':
                if re.match(belt_patt, on):
                    conn.execute("UPDATE Dalibnieki_rezekne SET belt = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'belt error')
            else:
                messagebox.showerror("", "Unexpected error")

            
            #Izmaiņas datu bāzē
            

            messagebox.showinfo("Data is updated", "Data is updated")
        elif where == "kraslava":
            if what == 'name':
                if re.match(name_patt, on):
                    conn.execute("UPDATE Dalibnieki_kraslava SET name = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'name error')
            elif what == 'surname':
                if re.match(name_patt, on):
                    conn.execute("UPDATE Dalibnieki_kraslava SET surname = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'surname error')
            elif what == 'age':
                if re.match(age_patt, on):
                    conn.execute("UPDATE Dalibnieki_kraslava SET age = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'age error')
            elif what == 'belt':
                if re.match(belt_patt, on):
                    conn.execute("UPDATE DDalibnieki_kraslava SET belt = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'belt error')
            else:
                messagebox.showerror("", "Unexpected error")

            
            #Izmaiņas datu bāzē
            

            messagebox.showinfo("Data is updated", "Data is updated")
        elif where == "preili":
            if what == 'name':
                if re.match(name_patt, on):
                    conn.execute("UPDATE Dalibnieki_preili SET name = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'name error')
            elif what == 'surname':
                if re.match(name_patt, on):
                    conn.execute("UPDATE Dalibnieki_preili SET surname = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'surname error')
            elif what == 'age':
                if re.match(age_patt, on):
                    conn.execute("UPDATE Dalibnieki_preili SET age = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'age error')
            elif what == 'belt':
                if re.match(belt_patt, on):
                    conn.execute("UPDATE Dalibnieki_preili SET belt = ? WHERE pk = ?;", (on, who))
                    conn.commit()
                else:
                    messagebox.showerror('', 'belt error')
            else:
                messagebox.showerror("", "Unexpected error")

            
            #Izmaiņas datu bāzē
            

            messagebox.showinfo("Data is updated", "Data is updated")
        else:
            messagebox.showerror("", "Unexpected error")

        update_root.destroy()

       


    update_root = Toplevel()
    update_root.geometry('500x500+750+300')

    Label(update_root, text="Ievadiet ko jūs gribāt izmainīt (name, surname, age, belt, pk)").pack()
    entry_what = ttk.Combobox(update_root, values=name_list, state='readonly')
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
            if where == "rezekne":
                conn.execute("Delete from Dalibnieki_rezekne where pk = ?", (pk, ))
                conn.commit()
                messagebox.showinfo("", "Deletion is complete")
            elif where == "kraslava":
                conn.execute("Delete from Dalibnieki_kraslava where pk = ?", (pk, ))
                conn.commit()
                messagebox.showinfo("", "Deletion is complete")
            elif where == "preili":
                conn.execute("Delete from Dalibnieki_preili where pk = ?", (pk, ))
                conn.commit()
                messagebox.showinfo("", "Deletion is complete")
            else:
                messagebox.showerror("", "Unexpected error")

        except Exception as e:
            messagebox.showerror("", e)

        delete_root.destroy()
    
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
        pk_patt = r'\d{6}-\d{5}'

        try:
            if re.match(pk_patt, pk):
                if where == "rezekne":
                    cur.execute("Select * from Dalibnieki_rezekne where pk = ?", (pk, ))
                elif where == "kraslava":
                    cur.execute("Select * from Dalibnieki_kraslava where pk = ?", (pk, ))
                elif where == "preili":
                    cur.execute("Select * from Dalibnieki_preili where pk = ?", (pk, ))
                else:
                    messagebox.showerror("", "Unexpected error")
                result = cur.fetchone()
                if result == None:
                    messagebox.showinfo("", "There is no perticipants with such personal code")
                else:
                    messagebox.showinfo("", result)
            
            else:
                messagebox.showerror("ValueError", "Please write personal code correctly")
        
        except Exception as e:
            messagebox.showerror("Unexpected Error", e)

        find_root.destroy()

    find_root = Toplevel()
    find_root.geometry("500x500+750+300")
    find_root.resizable(width=False, height=False)

    Label(find_root, text="Ievadiet personas kodu").pack()
    entry_pk = Entry(find_root)
    entry_pk.pack(padx=10, pady=5)

    Button(find_root, text="Find", padx=10, pady=10, command=find_function).pack(padx=10, pady=10)

def calendar_root_function():
    calendar_root = Toplevel()
    calendar_main = Calendar(calendar_root, firstweekday="monday")
    calendar_main.pack()


def rezekne_root():
    global where
    where = "rezekne"

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

def kraslava_root():
    global where
    where = "kraslava"

    #Galvenais logs
    main_root = Tk()
    main_root.geometry("500x500+750+300")
    main_root.resizable(width=False, height=False)



    Button(main_root, text="Registration", padx=10, pady=10, command=registration_root_function).pack(padx=10, pady=10)
    Button(main_root, text="Update", padx=10, pady=10, command=update_root_function).pack(padx=10, pady=10)
    Button(main_root, text="Find", padx=10, pady=10, command=find_root_function).pack(padx=10, pady=10)
    Button(main_root, text="Delete", padx=10, pady=10, command=delete_root_function).pack(padx=10, pady=10)
    Button(main_root, text="Calendar", padx=10, pady=10, command=calendar_root_function).pack(padx=10, pady=10)


    main_root.mainloop()

def preili_root():
    global where
    where = "preili"

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

choice_root = Tk()
choice_root.geometry("500x500+750+300")
choice_root.resizable(width=False, height=False)

Button(choice_root, text="Rezekne", padx=10, pady=10, command=rezekne_root).pack(padx=10, pady=10)
Button(choice_root, text="Kraslava", padx=10, pady=10, command=kraslava_root).pack(padx=10, pady=10)
Button(choice_root, text="Preili", padx=10, pady=10, command=preili_root).pack(padx=10, pady=10)

choice_root.mainloop()