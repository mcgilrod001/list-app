# imports
import customtkinter as ctk
import tkinter

# root setup
root = ctk.CTk()

# general settings
ctk.set_default_color_theme('dark-blue')
ctk.set_appearance_mode('dark')
root.geometry("300x200")
root.title("listy")

# classess
class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets
        self.lable = ctk.CTkLabel(self, text="list", font=("roboto", 20))
        self.lable.pack_configure(side="top", pady= 10)
class checky(ctk.CTkCheckBox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        def checkbox_event(self):
            print("checkbox toggled, current value:", self.check_var.get())
        # self.height = 50
        # self.width = 150
        self.fg_color = ("#ffffff", "#363636")
        self.check_var = ctk.StringVar(value="on")
        self.variable = self.check_var 
        self.command = checkbox_event
        self.on_value = "on"
        self.off_value = "off"
# temp data set

tasks = ["task 1", "task 2", "task 3"]
# instances list TODO: save this so you dont have to recreate each item
instances = {}
def destructo(name):
    instances[name].destroy() 
def plant_destroy_button(name):
    destroy_button = ctk.CTkButton(master=instances[name], height=30, width=30, text="x", font=("roboto", 20), fg_color=("#ffffff", "#424242"), hover_color='red', command=lambda:destructo(name))
    destroy_button.pack_configure(side="right")


main_frame =  MyFrame(master=root, width=300, height=200, corner_radius=0, fg_color="transparent")
main_frame.pack()

for i in range(len(tasks)):
    name = f'task_{i+1}'
    # remeber instances[name] is always equal to the last task in the list]
    instances[name] = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color = ("#ffffff", "#363636"))
    instances[name].pack_propagate(False)
    instances[name].pack_configure(side='top', pady=1)
    
    # create check box in frame
    checkbox = ctk.CTkCheckBox(master=instances[name], text=name)
    checkbox.pack_configure(side="left")
    plant_destroy_button(name)

root.mainloop()

# TODO:
# experimetnal (commented out may need later)
"""
# frame1 = ctk.CTkFrame(master=root, height=10, width=150, fg_color=("#ffffff", "#363636"))
# frame1.pack_configure(side = 'top',fill = 'y', pady=1)
# def frame_shrink():
    # frame.configure(height=50)

# f1 = ctk.CTkFrame(master=root, height=50, width=150, fg_color = ("#ffffff", "#363636"))
# f1.pack_configure(side='top', fill='y', pady=1)
# button = ctk.CTkButton(root, command=frame_shrink)
# button.pack()
# checkbox = ctk.CTkCheckBox(frame, text="CTkCheckBox", )
# checkbox.pack_configure(side = 'top')
"""
"""
what is the problem
    i need a check box to appear with a variable
    i need to be able to tell if that check box is checked
    i need the check box inside of a frame
    i need need to be able to create as many as i want
"""
        