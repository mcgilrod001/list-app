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
tasks = ['1', 'task', '3'] #should never be empty
# instances list TODO: save this so you dont have to recreate each item
instances = {}
# already_packed = [] # proboly dont need, just compare instace keys, with tasks if they dont match, either delete everything and repack everything, or  only repack what is needed.
def destructo(name):
    instances[name].destroy()
     

def plant_destroy_button(name):
    destroy_button = ctk.CTkButton(master=instances[name], height=30, width=30, text="x", font=("roboto", 20), fg_color=("#ffffff", "#424242"), hover_color='red', command=lambda:destructo(name))
    destroy_button.pack_configure(side="right", padx=1, pady=1)
    # TODO add perminant delete funciton so it removes the item from tasks list

# main frame
main_frame =  ScrollableFrame(master=root, width=300, height=500, corner_radius=0, fg_color="transparent")
main_frame.pack(fill='both', expand=True)

def task_packer():
    for task in tasks:
        name = f'{task.replace(" ", "_")}'
        # remeber instances[name] is always equal to the last task in the list]
        instances[name] = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color=("#ffffff", "#363636"))
        instances[name].pack_propagate(False)
        instances[name].pack_configure(side='top', pady=1)
        
        # create check box in frame
        checkbox = ctk.CTkCheckBox(master=instances[name], text=task) # make sure name is set to the text entry
        checkbox.pack_configure(side="left")
        plant_destroy_button(name)
        # already_packed.append(name)
task_packer()
def pack_from_entry():
    """
    # def task_isInstance_check():
        # if tasks == list(instances.keys()):
        #     print("there are no new tasks") # i cant think of a single situation where this should unless they enter a blank string or one that already exists
        # else:
        #     print(f'intances list: {list(instances.keys())} \n task list: {tasks}')
    # task_isInstance_check()          
    """
    # destroy everything
    destroy_all()
    global instances
    task_packer()
def destroy_all():
    global instances
    for instance in instances:
        print(instance)
        destructo(instance)
    instances = {}

# destroys everything
destroy_everything_button = ctk.CTkButton(master=main_frame,command=destroy_all) 
destroy_everything_button.pack_configure(side='bottom')

def add_task_to_tasks(task_name):
    def check_for_blanks(task_name):
        return all(char == ' ' for char in task_name)
    if  check_for_blanks(task_name):
        print("string is emty")
    elif task_name in tasks: 
        print("task already in task")
    else: #should only pass this check if it isnt already in tasks and isnt blank.
        tasks.append(task_name)
        # print(tasks)
        pack_from_entry()


def add_task_contstructor():
    # new task box/button
    global add_task_frame
    add_task_frame = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color=("#ffffff", "#363636"))
    add_task_frame.pack_propagate(False)
    add_task_frame.pack_configure(side="bottom",pady=1)

    global task_add_containter
    task_add_containter = ctk.CTkEntry(master=add_task_frame, placeholder_text="Add Task", border_color='#363636')
    task_add_containter.pack_configure(side='left', pady=1, fill='both', expand=True)

    global submit_button
    submit_button = ctk.CTkButton(master=add_task_frame, height=30, width=30, text="", font=("roboto", 20), command=lambda: add_task_to_tasks(task_add_containter.get())) #send to the list packer
    submit_button.pack_configure(side='right', padx=1, pady= 1)

add_task_contstructor()

def add_task_destroyer():
    global add_task_frame
    global task_add_containter
    global submit_button
    add_task_frame.destroy()
    task_add_containter.destroy()
    submit_button.destroy()


# testing for fucntion incase something changes and for whatever reason there are less tasks on the screen then there should be or one is added after packing.
# print(list(instances.keys()))
# print(already_packed)
# already_packed.pop()

# tests if what has been packed matches what needs to be packed
"""
if tasks == list(instances.keys()):
    pass
else:
    # find what is different
    for i in range (len(list(instances.keys()))):
        try:
            if i >= len(tasks):
                already_packed.append("")
            print(f'origonal key:{list(instances.keys())[i]} already packed key:{already_packed[i]}')
        except IndexError:
            print("o fuk")
        # destroy them all then replace them
    # pack any
"""
            
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
"""
    for i in range(len(tasks)):
        name = f'{task_name.replace(" ","_")}'
        # remeber instances[name] is always equal to the last task in the list]
        instances[name] = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color=("#ffffff", "#363636"))
        instances[name].pack_propagate(False)
        instances[name].pack_configure(side='top', pady=1)
        
        # create check box in frame
        checkbox = ctk.CTkCheckBox(master=instances[name], text=name) # make sure name is set to the text entry
        checkbox.pack_configure(side="left")
        plant_destroy_button(name)
        # already_packed.append(name)
        
""" 