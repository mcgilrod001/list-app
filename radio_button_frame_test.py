import customtkinter as ctk
import tkinter


root = ctk.CTk()

# basic window setup
ctk.set_default_color_theme('dark-blue')
ctk.set_appearance_mode('dark')
root.geometry("500x200")
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
root.title("listy")


class checky(ctk.CTkCheckBox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.height = 50
        self.width = 150
        self.fg_color=("#ffffff", "#363636")
        self.check_var = ctk.StringVar(value="on")
    
    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get())



    
frame = ctk.CTkFrame(master=root, height=50, width=150, fg_color=("#ffffff", "#363636"))
frame.pack_configure(side = 'top',fill = 'both', pady=1)
frame1 = ctk.CTkFrame(master=root, height=50, width=150, fg_color=("#ffffff", "#363636"))
frame1.pack_configure(side = 'top',fill = 'both', pady=1)

checkbox = ctk.CTkCheckBox(frame, text="CTkCheckBox", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox1 = ctk.CTkCheckBox(frame1, text="", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox1.pack_configure(side = 'top')
checkbox.pack_configure(side = 'top')




root.mainloop()
