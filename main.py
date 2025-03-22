import itertools
import sqlite3 as db
import re
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.simpledialog import askinteger

#------------------------------------------------

#Datu baze izveide

conn = db.connect('karate.db')
curr = conn.cursor()            

#-----------------------------------------------

#Vecākais class Dalibnieks ar inicializēšanu

class Dalibnieks:                             
    Dalibnieka_vards=""
    Dalibnieka_uzvards=""
    Dalibnieka_dzimums=""
    Dalibnieka_vecums=""
    Dalibnieka_svars=0
    Dalibnieka_josta=""
    Dalibnieka_pk=""

    id_iter_dalibnieks=itertools.count()

    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        self.Dalibnieka_vards=vards
        self.Dalibnieka_uzvards=uzvards
        self.Dalibnieka_dzimums=dzimums
        self.Dalibnieka_vecums=vecums
        self.Dalibnieka_svars=svars
        self.Dalibnieka_josta=josta
        self.Dalibnieka_pk=pk
        self.Dalibnieka_id=next(self.id_iter_dalibnieks)+1

    def dalibnieka_info(self):
        return[
            self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_dzimums, self.Dalibnieka_vecums, self.Dalibnieka_svars, self.Dalibnieka_josta, self.Dalibnieka_pk
        ]

#----------------------------------------------------------

#Bērnu class cīņas dalibniekam

class Kumite(Dalibnieks):
    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        super().__init__(vards, uzvards, dzimums, vecums, svars, josta, pk)
    id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #Svaras kategorijas
    kategorijas_vir=[61, 68, 76, 85, 300]
    kategorijas_vir_name=["-60 kg", "61-67 kg", "68-75 kg", "76-84 kg", "85+ kg"]
    kategorijas_siev=[51, 56, 62, 69, 300]
    kategorijas_siev_name=["-50 kg", "51-55 kg", "56-61 kg", "62-68 kg", "69+ kg"]

    #svara kategorijas noteikšana
    
    def svara_kategorija(self):
        self.id_reg = 0
        self.Dalibnieka_svara_kategorija=""
        if self.Dalibnieka_dzimums[0]=="s":
            stop=False
            a=0
            b=1
            c=1
            while stop!=True:
                if self.Dalibnieka_svars in range(1, self.kategorijas_siev[0]):
                    print(self.kategorijas_siev_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_siev_name[c-1]
                    self.id_reg = self.id[c-1+5]
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_siev[a], self.kategorijas_siev[b]):
                    c+=1
                    print(self.kategorijas_siev_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_siev_name[c-1]
                    self.id_reg = self.id[c-1+5]
                    stop=True
                else:
                    a=a+1
                    b=b+1
                    c+=1
        elif self.Dalibnieka_dzimums[0]=="v":
            stop=False
            a=0
            b=1
            c=1
            while stop!=True:
                if self.Dalibnieka_svars in range(1, self.kategorijas_vir[0]):
                    print(self.kategorijas_vir_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_vir_name[c-1]
                    self.id_reg = self.id[c-1]
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_vir[a], self.kategorijas_vir[b]):
                    c+=1
                    print(self.kategorijas_vir_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_vir_name[c-1]
                    self.id_reg = self.id[c-1]
                    stop=True
                else:
                    a=a+1
                    b=b+1
                    c+=1
        else:
            print("Who are you?")

    #Dalibnieka reģistrešana

    def registration(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        
        conn.execute("INSERT INTO Dalibnieks_kumite(name, surname, age, belt, personal_code, id_weight_cathegory, gender) VALUES(?, ?, ?, ?, ?, ?, ?)", (self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_svara_kategorija, self.gender))
        conn.commit()

    def update(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        id_d = int(input("Ievadiet dalibnieka id: "))
        conn.execute("INSERT INTO Dalibnieks_kumite(id_dalibnieka_kumite, name, surname, age, belt, personal_code, id_weight_cathegory, gender) VALUES(?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id_dalibnieka_kumite) DO UPDATE SET name=excluded.name, surname=excluded.surname, age=excluded.age, belt=excluded.belt, personal_code=excluded.personal_code, id_weight_cathegory=excluded.id_weight_cathegory, gender=excluded.gender;", (id_d, self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_svara_kategorija, self.gender))
        conn.commit()

#-------------------------------------------------------------------

#Otrais bernu class kata Dalibniekam


class Kata(Dalibnieks):
    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        super().__init__(vards, uzvards, dzimums, vecums, svars, josta, pk)
        self.Dalibnieka_kata=""
    
    def kata(self):
        kata = conn.execute("SELECT * from Kata")
        print("Kata list: ")
        for r in kata:
            print(r)
        
        stop= False
        while stop!=True:
            kata_num = int(input('Ievadiet kata id: '))
            for i in range(103):
                cur = conn.execute("SELECT * from Kata WHERE id_kata = ?", (i,))
                kata = cur.fetchall()
                if kata_num == i:
                    agree = input(f"{kata} ir jūsu kata? ")
                    if agree=='True':
                        self.Dalibnieka_kata_id=i
                        stop=True
                    else:
                        print("Mēģini vēl reiz")
        


    #Dalibnieka registresana    
    def registration(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        
        conn.execute("INSERT INTO Dalibnieks_kata(name, surname, age, belt, personal_code, id_kata, geneder) VALUES(?, ?, ?, ?, ?, ?, ?)", (self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_kata_id, self.gender))
        conn.commit()


    def update_vards(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        id_d = entry_id.get()
        #vards_d = int(input("Ievadiet dalibnieka id: "))
        conn.execute("INSERT INTO Dalibnieks_kata(id_dalibnieka_kata, name, surname, age, belt, personal_code, id_kata, geneder) VALUES(?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id_dalibnieka_kata) DO UPDATE SET name=excluded.name, surname=excluded.surname, age=excluded.age, belt=excluded.belt, personal_code=excluded.personal_code, id_kata=excluded.id_kata, geneder=excluded.geneder;", (id_d, self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_kata_id, self.gender))
        conn.commit()

#------------------------------------------------------------

#Tkinter

#------------------------------------------------------------

#Kata līmenis

def kata_level():

    #Registracijas logs

    def reg_logs():

        def kata_list():
            global names
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("SELECT kata from Kata")
                names = []
                name_all=cursor.fetchall()
                for katas in name_all:
                    names.append(katas[0])
                conn.close()
                

            except Exception as e:
                messagebox.showerror("Error", f"Neizdevas nolasīt kata nosaukumus: {e}")

        def parbaude():
            vards = entry_vards.get()
            uzvards = entry_uzvards.get()
            dzimums = entry_dzimums.get()
            vecums = entry_vecums.get()
            masa = entry_masa.get()
            josta = entry_josta.get()
            pk = entry_pk.get()

            vards_patt = r'^[A-ZĀ-Ž]{1}[a-zā-ž]+$|^[A-ZĀ-Ž]{1}[a-zā-ž]+\s+[A-ZĀ-Ž]{1}[a-zā-ž]+$'
            vecums_patt = r'^\d+$'
            masa_patt = r'^\d{2,3}$'
            #josta_patt = r'^\d{2}+\s+[a-z]$'
            josta_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
            pk_patt = r'\d{6}+[-]+\d{5}'

            if re.match(vards_patt, vards) and re.match(vards_patt, uzvards):
                
                if re.match(vecums_patt, vecums):
                    
                    if re.match(josta_patt, josta):

                        if re.match(masa_patt, masa):

                            if re.match(pk_patt, pk):
                                kata_reg()
                            else:
                                messagebox.showerror("", "Personas kods ir nepareizā formatā")
                        else:
                            messagebox.showerror("", "Masa ir nepareizā formatā")
                        
                    else:
                        messagebox.showerror("", "Josta ir nepareizā formatā")

                else:
                    messagebox.showerror("", "Vecums ir nepareizā formatā")
            else:
                messagebox.showerror("", "Vārds vai uzvārds ir nepareizā formatā")


        def kata_reg():
            global dal
            vards = entry_vards.get()
            uzvards = entry_uzvards.get()
            dzimums = entry_dzimums.get()
            vecums = entry_vecums.get()
            masa = entry_masa.get()
            josta = entry_josta.get()
            pk = entry_pk.get()

            if vards and uzvards and dzimums and vecums.isdigit()>0 and masa.isdigit()>0 and josta and pk:
                try:
                    vecums = int(vecums)
                    masa = int(masa)
                    dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    dal=Kata(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    get_var = kata_combobox.get()
                    conn = db.connect('karate.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT id_kata from Kata where kata = ?;", (get_var,),)
                    id_kata = cursor.fetchone()
                    print(id_kata)
                    dal.Dalibnieka_kata_id=id_kata[0]
                    dal.registration()

                    messagebox.showinfo("Success", "Dalibnieks tik reģistrēts")

                except ValueError:
                    messagebox.showerror("Error")
            else:
                messagebox.showerror("Error")


        
        

        

        reg_log = Toplevel()
        reg_log.title("Registrācija")

        kata_list()

        Label(reg_log, text="Ievadiet datus", padx=10, pady=10).grid(column=0, row=0)


        v = Label(reg_log, text="Vards:").grid(column=0, row=1)
        entry_vards = Entry(reg_log)
        entry_vards.grid(column=1, row=1, padx=5, pady=5)


        u = Label(reg_log, text="Uzvards:").grid(column=0, row=2)
        entry_uzvards = Entry(reg_log)
        entry_uzvards.grid(column=1, row=2, padx=5, pady=5)
        

        d = Label(reg_log, text="Dzimums:").grid(column=0, row=3)
        entry_dzimums = Entry(reg_log)
        entry_dzimums.grid(column=1, row=3, padx=5, pady=5)
        

        ve = Label(reg_log, text="Vecums:").grid(column=0, row=4)
        entry_vecums = Entry(reg_log)
        entry_vecums.grid(column=1, row=4, padx=5, pady=5)
        

        m = Label(reg_log, text="Masa:").grid(column=0, row=5)
        entry_masa = Entry(reg_log)
        entry_masa.grid(column=1, row=5, padx=5, pady=5)
        

        j = Label(reg_log, text="Josta:").grid(column=0, row=6)
        entry_josta = Entry(reg_log)
        entry_josta.grid(column=1, row=6, padx=5, pady=5)
        

        p = Label(reg_log, text="Personas kods:").grid(column=0, row=7)
        entry_pk = Entry(reg_log)
        entry_pk.grid(column=1, row=7, padx=5, pady=5)

        Label(reg_log, text="Kata:").grid(column=0, row=8)
        kata_combobox = ttk.Combobox(reg_log, width=30, state="readonly", values=names)
        kata_combobox.grid(column=1, row=8, padx=10)

        Button(reg_log, text="Saglabat", padx=10, pady=10, command=kata_reg).grid(column=1, row=9)

    #Atjaunošanas logs

    def upd_logs():

        def kata_list():
            global names
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("SELECT kata from Kata")
                names = []
                name_all=cursor.fetchall()
                for katas in name_all:
                    names.append(katas[0])
                conn.close()
                

            except Exception as e:
                messagebox.showerror("Error", f"Neizdevas nolasīt kata nosaukumus: {e}")
        

        def kata_reg():
            global dal
            vards = entry_vards.get()
            uzvards = entry_uzvards.get()
            dzimums = entry_dzimums.get()
            vecums = entry_vecums.get()
            masa = entry_masa.get()
            josta = entry_josta.get()
            pk = entry_pk.get()

            if vards and uzvards and dzimums and vecums.isdigit()>0 and masa.isdigit()>0 and josta and pk:
                try:
                    vecums = int(vecums)
                    masa = int(masa)
                    dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    dal=Kata(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    get_var = kata_combobox.get()
                    conn = db.connect('karate.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT id_kata from Kata where kata = ?;", (get_var,),)
                    id_kata = cursor.fetchone()
                    print(id_kata)
                    dal.Dalibnieka_kata_id=id_kata[0]
                    dal.update()

                    messagebox.showinfo("Success", "Dalibnieks tik reģistrēts")

                except ValueError:
                    messagebox.showerror("Error")
            else:
                messagebox.showerror("Error")

        def upd_one():
            
            def update_one():
                id_d = entry_id.get()
                what = entry_what.get()
                on = entry_on.get()
                if what and on:
                    curr.execute("INSERT INTO Dalibnieks_kata(id_dalibnieka_kata) VALUES(?, ?) ON CONFLICT(id_dalibnieka_kata) DO UPDATE SET ;", (id_d,))

            upd_one_root = Toplevel()
            upd_one_root.geometry("200x250")

            Label(upd_one_root, text="Sportista id: ").grid(column=1, row=0)
            entry_id = Entry(upd_one_root)
            entry_id.grid(column=1, row=1)

            Label(upd_one_root, text="Ko jus gribat atjaunot: ").grid(column=1, row=2)
            entry_what = Entry(upd_one_root)
            entry_what.grid(column=1, row=3)

            Label(upd_one_root, text="Uz ko jus gribat atjaunot: ").grid(column=1, row=4)
            entry_on = Entry(upd_one_root)
            entry_on.grid(column=1, row=5)

            Button(upd_one_root, text="Atjaunot", padx=10, pady=10).grid(column=1, row=6)

        def upd_all():
        

            kata_list()

            reg_log = Toplevel()
            reg_log.title("Registrācija")



            Label(reg_log, text="Ievadiet datus", padx=10, pady=10)#.grid(column=0, row=0)

            Label(reg_log, text="Id:").grid(column=0, row=0)
            entry_id = Entry(reg_log)
            entry_id.grid(column=1, row=0, padx=5, pady=5)


            Label(reg_log, text="Vards:").grid(column=0, row=1)
            entry_vards = Entry(reg_log)
            entry_vards.grid(column=1, row=1, padx=5, pady=5)


            Label(reg_log, text="Uzvards:").grid(column=0, row=2)
            entry_uzvards = Entry(reg_log)
            entry_uzvards.grid(column=1, row=2, padx=5, pady=5)
            

            Label(reg_log, text="Dzimums:").grid(column=0, row=3)
            entry_dzimums = Entry(reg_log)
            entry_dzimums.grid(column=1, row=3, padx=5, pady=5)
            

            Label(reg_log, text="Vecums:").grid(column=0, row=4)
            entry_vecums = Entry(reg_log)
            entry_vecums.grid(column=1, row=4, padx=5, pady=5)
            

            Label(reg_log, text="Masa:").grid(column=0, row=5)
            entry_masa = Entry(reg_log)
            entry_masa.grid(column=1, row=5, padx=5, pady=5)
            

            Label(reg_log, text="Josta:").grid(column=0, row=6)
            entry_josta = Entry(reg_log)
            entry_josta.grid(column=1, row=6, padx=5, pady=5)
            

            Label(reg_log, text="Personas kods:").grid(column=0, row=7)
            entry_pk = Entry(reg_log)
            entry_pk.grid(column=1, row=7, padx=5, pady=5)

            Label(reg_log, text="Kata:").grid(column=0, row=8)
            kata_combobox = ttk.Combobox(reg_log, width=30, state="readonly", values=names)
            kata_combobox.grid(column=1, row=8, padx=10)

            Button(reg_log, text="Saglabat", padx=10, pady=10, command=kata_reg).grid(column=1, row=9)

        upd_root = Toplevel()
        upd_root.geometry("200x250")

        Button(upd_root, text="Atjaunot vienu daļu", padx=10, pady=10).grid(column=0, row=0)
        Button(upd_root, text="Atjaunot visu", padx=10, pady=10, command=upd_all).grid(column=0, row=1)


    #Atrašanas logs

    def find_logs():

        def print_all():
            conn = db.connect('karate.db')
            cursor = conn.cursor()
            cursor.execute("select * from Dalibnieks_kata INNER JOIN kata on Dalibnieks_kata.id_kata = Kata.id_kata")
            info = cursor.fetchall()

            messagebox.showinfo("Visi dalibnieki", info)

        def find_by_id():

            id_dal = entry_id.get()
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("select * from Dalibnieks_kata INNER JOIN kata on Dalibnieks_kata.id_kata = Kata.id_kata where id_dalibnieka_kata = ?", (id_dal,))
                info = cursor.fetchall()
                print(info[0][0])

                messagebox.showinfo("Dalibnieks", f"Dalibnieka vārds: {info[0][1]}\nDalibnieka uzvārds: {info[0][2]}\nDalibnieka vecums: {info[0][3]}\nDalibnieka vārds: {info[0][9]}\n")
            except Exception as e:
                messagebox.showerror('Error', e)


        find_log = Toplevel()

        all_btn = Button(find_log, text="Noprintēt visus", padx=10, pady=10, command=print_all).grid(column=0, row=0, padx=10, pady=10)

        Label(find_log, text="Ievadiet id:").grid(column=0, row=1, padx=10, pady=10)
        entry_id = Entry(find_log)
        entry_id.grid(column=0, row=2, padx=10, pady=10)
        atrast = Button(find_log, text="Atrast ar id", padx=10, pady=10, command=find_by_id).grid(column=0, row=3, padx=10, pady=10)

    #Dzēšanas logs

    def del_logs():

        def del_dalib():
            id_dal = entry_del_id.get()
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("DELETE from Dalibnieks_kata where id_dalibnieka_kata = ?", (id_dal,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Dalibnieks tiek nodzēsts")

            except Exception as e:
                messagebox.showerror("Error", e)



        del_log = Toplevel()
        Label(del_log, text="Ievadiet id:").grid(column=0, row=0, padx=10, pady=10)
        entry_del_id = Entry(del_log)
        entry_del_id.grid(column=0, row=1, padx=10, pady=10)
        Button(del_log, text="Dzēst", padx=10, pady=10, command=del_dalib).grid(column=0, row=2, padx=5, pady=5)



    kata_logs = Toplevel()
    kata_logs.geometry("200x250")
    kata_logs.title("Kata sacensības")
    
    Button(kata_logs, text="Registracija", padx=10, pady=10, command=reg_logs).grid(column=1, row=0, padx=30, pady=10)
    Button(kata_logs, text="Atjaunot datus", padx=10, pady=10, command=upd_logs).grid(column=1, row=1, padx=30, pady=10)
    Button(kata_logs, text="Atrast", padx=10, pady=10, command=find_logs).grid(column=1, row=2, padx=30, pady=10)
    Button(kata_logs, text="Nodzēst", padx=10, pady=10, command=del_logs).grid(column=1, row=3, padx=30, pady=10)

#------------------------------------------------------------

#Cīņas līmenis

def kumite_level():

    #Registracijas logs

    def reg_logs():

        

        def kata_reg():
            global dal
            vards = entry_vards.get()
            uzvards = entry_uzvards.get()
            dzimums = entry_dzimums.get()
            vecums = entry_vecums.get()
            masa = entry_masa.get()
            josta = entry_josta.get()
            pk = entry_pk.get()

            if vards and uzvards and dzimums and vecums.isdigit()>0 and masa.isdigit()>0 and josta and pk:
                try:
                    vecums = int(vecums)
                    masa = int(masa)
                    dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    dal=Kumite(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    dal.svara_kategorija()
                    dal.registration()

                    messagebox.showinfo("Success", "Dalibnieks tik reģistrēts")

                except ValueError:
                    messagebox.showerror("Error")
            else:
                messagebox.showerror("Error")
        
        reg_log = Toplevel()
        reg_log.title("Registrācija")



        Label(reg_log, text="Ievadiet datus", padx=10, pady=10).grid(column=0, row=0)


        v = Label(reg_log, text="Vards:").grid(column=0, row=1)
        entry_vards = Entry(reg_log)
        entry_vards.grid(column=1, row=1, padx=5, pady=5)


        u = Label(reg_log, text="Uzvards:").grid(column=0, row=2)
        entry_uzvards = Entry(reg_log)
        entry_uzvards.grid(column=1, row=2, padx=5, pady=5)
        

        d = Label(reg_log, text="Dzimums:").grid(column=0, row=3)
        entry_dzimums = Entry(reg_log)
        entry_dzimums.grid(column=1, row=3, padx=5, pady=5)
        

        ve = Label(reg_log, text="Vecums:").grid(column=0, row=4)
        entry_vecums = Entry(reg_log)
        entry_vecums.grid(column=1, row=4, padx=5, pady=5)
        

        m = Label(reg_log, text="Masa:").grid(column=0, row=5)
        entry_masa = Entry(reg_log)
        entry_masa.grid(column=1, row=5, padx=5, pady=5)
        

        j = Label(reg_log, text="Josta:").grid(column=0, row=6)
        entry_josta = Entry(reg_log)
        entry_josta.grid(column=1, row=6, padx=5, pady=5)
        

        p = Label(reg_log, text="Personas kods:").grid(column=0, row=7)
        entry_pk = Entry(reg_log)
        entry_pk.grid(column=1, row=7, padx=5, pady=5)


        Button(reg_log, text="Saglabat", padx=10, pady=10, command=kata_reg).grid(column=1, row=9)

    #Atrašanas logs

    def find_logs():

        def print_all():
            conn = db.connect('karate.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * from Dalibnieks_kumite")
            info = cursor.fetchall()

            messagebox.showinfo("Visi dalibnieki", info)

        def find_by_id():

            id_dal = entry_id.get()
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("select * from Dalibnieks_kumite where id_dalibnieka_kumite = ?", (id_dal,))
                info = cursor.fetchall()
                messagebox.showinfo("Dalibnieks", f"Dalibnieka vārds: {info[0][1]}\nDalibnieka uzvārds: {info[0][2]}\nDalibnieka vecums: {info[0][3]}\nDalibnieka svara kategorija: {info[0][6]}")
            except Exception as e:
                messagebox.showerror('Error', e)


        find_log = Toplevel()

        Button(find_log, text="Noprintēt visus", padx=10, pady=10, command=print_all).grid(column=0, row=0, padx=10, pady=10)

        Label(find_log, text="Ievadiet id:").grid(column=0, row=1, padx=10, pady=10)
        entry_id = Entry(find_log)
        entry_id.grid(column=0, row=2, padx=10, pady=10)
        Button(find_log, text="Atrast ar id", padx=10, pady=10, command=find_by_id).grid(column=0, row=3, padx=10, pady=10)

    #Dzēšanas logs

    def del_logs():

        def del_dalib():
            id_dal = entry_del_id.get()
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("DELETE from Dalibnieks_kumite where id_dalibnieka_kumite = ?", (id_dal,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Dalibnieks tiek nodzēsts")

            except Exception as e:
                messagebox.showerror("Error", e)



        del_log = Toplevel()

        Label(del_log, text="Ievadiet id:").grid(column=0, row=0, padx=10, pady=10)
        entry_del_id = Entry(del_log)
        entry_del_id.grid(column=0, row=1, padx=10, pady=10)
        Button(del_log, text="Dzēst", padx=10, pady=10, command=del_dalib).grid(column=0, row=2, padx=5, pady=5)

    


    kumite_logs = Toplevel()
    kumite_logs.geometry("200x250")
    kumite_logs.title("Kumite sacensības")

    Button(kumite_logs, text="Registracija", padx=10, pady=10, command=reg_logs).grid(column=1, row=0, padx=30, pady=10)
    Button(kumite_logs, text="Atjaunot datus", padx=10, pady=10).grid(column=1, row=1, padx=30, pady=10)
    Button(kumite_logs, text="Atrast", padx=10, pady=10, command=find_logs).grid(column=1, row=2, padx=30, pady=10)
    Button(kumite_logs, text="Nodzēst", padx=10, pady=10, command=del_logs).grid(column=1, row=3, padx=30, pady=10)

#------------------------------------------------------------

#Galvenais logs
root = Tk()
root.geometry("200x250")
root.title("Sacensības sistēma")
label1 = Label(root, text="Izvēlies sacensības kategoriju: ", padx=10, pady=10).grid(column=2, row=0)

kat_btn = Button(root, text="Kata", padx=30, pady=20, command=kata_level).grid(column=2, row=1, padx=10, pady=10)
kumite_btn = Button(root, text="Kumite", padx=30, pady=20, command=kumite_level).grid(column=2, row=2, padx=10, pady=10)

root.mainloop()
           
           



