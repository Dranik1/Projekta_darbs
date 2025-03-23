import ctypes
from tkinter import *
from tkinter import messagebox
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

'''print(screensize)

root_number = 0


def root_size():
    def main_root_size():
        global size
        x_position = (screensize[0]-500)/2
        y_position = (screensize[1]-500)/2
        size = '500x500'+'+'+str(int(x_position))+'+'+str(int(y_position))
    #size = '500x500'
    #size_int = 500
    main_root_size()

    main_root = Tk()
    main_root.geometry(size) 
    main_root.resizable(width=False, height=False)


    main_root.mainloop()

root_size()'''


def root_size():
    def main_root_size():
        response = messagebox.askyesno("", "Do you mean a?")
        if response == True:
            messagebox.showinfo("clickes yes")
        else:
            messagebox.showinfo('clicked no')
    #size = 
    #size_int = 500
    main_root_size()

    main_root = Tk()
    main_root.geometry('500x500') 
    main_root.resizable(width=False, height=False)
    Button(main_root, text="Proba", command=main_root_size).pack()


    main_root.mainloop()

root_size()