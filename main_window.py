from tkinter import *
from tkinter import ttk
from draw import Draw

class main_window_figure:
    def __init__(self) -> None:
        root = Tk()
        root.attributes('-fullscreen', True)
        
        frm = ttk.Frame(root)
        frm.grid(sticky="nsew")
        
        root.grid_rowconfigure(0, weight=1) 
        root.grid_columnconfigure(0, weight=1) 
        
        frm.grid_rowconfigure(0, weight=1)
        frm.grid_rowconfigure(1, weight=1)
        frm.grid_rowconfigure(2, weight=1)
        frm.grid_rowconfigure(3, weight=1)
        frm.grid_columnconfigure(0, weight=1)
        
        style = ttk.Style()
        style.configure("Custom.TButton", background="#4CAF50", 
                foreground="black", font=("Arial", 15))
        
        ttk.Label(frm, text="Введите высоту пирамиды", 
                  font=('Arial', 20)).grid(column=0, row=0)
        
        self.pyramid_height = ttk.Entry(frm, width=50, font=("Arial", 15))
        self.pyramid_height.grid(column=0, row=1)
        
        ttk.Button(frm, text="Получить 3D пирамиды", 
                   command = lambda : self.__pyramid_output(),
                   width=50, style="Custom.TButton").grid(column=0, row=2)
        
        ttk.Button(frm, text="Выход", command = root.destroy, 
                   width=50, style="Custom.TButton").grid(column=0, row=3)
        
        root.mainloop()
        
    def __getting_value(self):
        __values_string = self.pyramid_height.get()
        
        return __values_string
    
    def __pyramid_output(self):
        height = self.__getting_value()
        pyramid_window = Draw()
        pyramid_window.draw_figure(float(height))