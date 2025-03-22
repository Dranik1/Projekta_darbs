import ctypes
from tkinter import *
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

print(screensize)





def root_size():
    def main_root_size():
        global size
        x_position = (screensize[0]-500)/2
        y_position = (screensize[1]-500)/2
        size = '500x500'+'+'+str(int(x_position))+'+'+str(y_position)
    #size = '500x500'
    #size_int = 500
    main_root_size()

    main_root = Tk()
    main_root.geometry(size) 
    main_root.resizable(False)


    main_root.mainloop()

root_size()