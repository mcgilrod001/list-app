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
class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets
        self.lable = ctk.CTkLabel(self, text="list", font=("roboto", 20))
        self.lable.pack_configure(side="top", pady= 10)

# temp data set
tasks = ["task 1", "task 2", "task 3"]
# instances list TODO: save this so you dont have to recreate each item
instances = {}
already_packed = []
def destructo(name):
    instances[name].destroy() 

def plant_destroy_button(name):
    destroy_button = ctk.CTkButton(master=instances[name], height=30, width=30, text="x", font=("roboto", 20), fg_color=("#ffffff", "#424242"), hover_color='red', command=lambda:destructo(name))
    destroy_button.pack_configure(side="right", padx=1, pady=1)


main_frame =  ScrollableFrame(master=root, width=300, height=500, corner_radius=0, fg_color="transparent")
main_frame.pack(fill='both', expand=True)
def list_packer():
    for i in range(len(tasks)):
        name = f'task_{i+1}'
        # remeber instances[name] is always equal to the last task in the list]
        instances[name] = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color=("#ffffff", "#363636"))
        instances[name].pack_propagate(False)
        instances[name].pack_configure(side='top', pady=1)
        
        # create check box in frame
        checkbox = ctk.CTkCheckBox(master=instances[name], text=name)
        checkbox.pack_configure(side="left")
        plant_destroy_button(name)
        already_packed.append(name)
list_packer()

def add_task_contstructor():
    # new task box/button
    global add_task_frame
    add_task_frame = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color=("#ffffff", "#363636"))
    add_task_frame.pack_propagate(False)
    add_task_frame.pack_configure(side="top",pady=1)

    global task_entry
    task_entry = ctk.CTkEntry(master=add_task_frame, placeholder_text="Add Task", border_color='#363636')
    task_entry.pack_configure(side='left', pady=1, fill='both', expand=True)

    global submit_button
    submit_button = ctk.CTkButton(master=add_task_frame, height=30, width=30, text="", font=("roboto", 20), command=lambda: task_entry.get()) #send to the list packer
    submit_button.pack_configure(side='right', padx=1, pady= 1)

add_task_contstructor()

def add_task_destroyer():
    global add_task_frame
    global task_entry
    global submit_button
    add_task_frame.destroy()
    task_entry.destroy()
    submit_button.destroy()


# testing for fucntion incase something changes and for whatever reason there are less tasks on the screen then there should be or one is added after packing.
# print(list(instances.keys()))
# print(already_packed)
# already_packed.pop()

# tests if what has been packed matches what needs to be packed
if already_packed == list(instances.keys()):
    pass
else:
    # find what is different
    for i in range (len(list(instances.keys()))):
        try:
            if i >= len(already_packed):
                already_packed.append("")
            print(f'origonal key:{list(instances.keys())[i]} already packed key:{already_packed[i]}')
        except IndexError:
            print("o fuk")
        # destroy them all then replace them
    
            
root.mainloop()
"""
# TODO create a function that destroyes all the packed items, if there is an order error or if some are missing, and then repacks them correctly, should aslo destroy
the add task frame so it can be placed again at the bottom, should recreate all the frames/tasks in correct order including tasks that were added with add task box 
"""
# TODO add a delete when completed function
# TODO be able to add tasks
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
        