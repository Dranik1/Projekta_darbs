


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
        print('ok')
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