'''from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similar("surname","name"))

if 'name'=='surname':
    print('a')

import re

name = input()
surname = input()
age = input()
belt = input()
pk = input()

data_list = [name, surname, age, belt, pk]

name_patt = r'^[A-ZĀ-Ž]+[a-zā-ž]+$'
age_patt = r'\d{1,3}'
belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
pk_patt = r'\d{6}+[-]+\d{5}'

pattern_list = [name_patt, name_patt, age_patt, belt_patt, pk_patt]

#datu pareizrakstīšanas pārbaude
for i in range(5):
    if re.match(pattern_list[i], data_list[i]):
        print(data_list[i])
        print(pattern_list[i])
    else:
        print('a')'''
import re
from tkinter import messagebox

name_patt = r'^[A-ZĀ-Ž][a-zā-ž]$'
age_patt = r'\d[1-3]'
belt_patt = r'[0-9]{1,2}[\sDan, \sKyu]'
pk_patt = r'\d[6]+[-]+\d[5]'

what = input()
on = input()

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