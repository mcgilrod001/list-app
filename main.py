import customtkinter as ctk
import tkinter

class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets
        self.lable = ctk.CTkLabel(self, text="list")
        self.lable.grid(row=0, column=0, padx=20)


class RadioButton(ctk.CTkRadioButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        

class root(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.my_frame = MyFrame(master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")
        self.my_radio_button = RadioButton(master=self.my_frame, Text="radio button")
        self.my_radio_button.grid(row=0, column =1, sticky="nsew")
root = root()
root.mainloop()