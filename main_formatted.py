# imports
import customtkinter as ctk

# class for scrollable expanding scroll frame and head label
class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets
        self.label = ctk.CTkLabel(self, text="list", font=("roboto", 20))
        self.label.pack_configure(side="top", pady= 10)

# destroys and wipes task
def destroy_single(name): #removes task
    instances[name].destroy()
    tasks.remove(task_instance_pairing[name])

# destroys an instance
def destroy_instance(name): #keeps task
    instances[name].destroy()

# places destroy button in individual task frames
def place_destroy_button(name):
    destroy_button = ctk.CTkButton(master=instances[name], height=30, width=30, text="x", font=("roboto", 20), fg_color=("#ffffff", "#424242"), hover_color='red', command=lambda:destroy_single(name))
    destroy_button.pack_configure(side="right", padx=1, pady=1)

# places tasks from task list
def task_packer():
    # formats name, pairs instance name with task name, assigns frame to intances[name]
    # sets that frame to not propogate so it dosnt shrink or expand, packs it, packs the checkbox and desctruction button
    for task in tasks:
        name = f'{task.replace(" ", "_")}'
        
        # pairs name of task to name of instance in pairing dict
        task_instance_pairing[name] = task
        
        # NOTE remeber instances[name] is always equal to the last task in the list]
        instances[name] = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color=("#ffffff", "#363636"))
        instances[name].pack_propagate(False)
        instances[name].pack_configure(side='top', pady=1)
        
        # creates check box in frame
        checkbox = ctk.CTkCheckBox(master=instances[name], text=task) # make sure name is set to the text entry
        checkbox.pack_configure(side="left")
        
        # places delete button
        place_destroy_button(name)

# destroys then repacks everything with the updated task list
def pack_from_entry():
    # destroy everything for repack
    destroy_instances()
    # repack
    task_packer()

# destroys instances and wipes instances for repacking
def destroy_instances():
    global instances
    for instance in instances:
        destroy_instance(instance)
    # ensures instances is clear
    instances = {}

# destroys everything
def destroy_all():
    global instances
    for instance in instances:
        destroy_single(f'{instance}')

# add tasks to task list and calls repack function
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

# creates and packs container to add new tasks
def new_task_container():
    # task entry frame
    new_task_frame = ctk.CTkFrame(master=main_frame, height=30, width=250, fg_color=("#ffffff", "#363636"))
    new_task_frame.pack_propagate(False)
    new_task_frame.pack_configure(side="bottom",pady=1)
    
    # task entry
    task_input = ctk.CTkEntry(master=new_task_frame, placeholder_text="Add Task", border_color='#363636')
    task_input.pack_configure(side='left', pady=1, fill='both', expand=True)

    # submit button
    submit_button = ctk.CTkButton(master=new_task_frame, height=30, width=30, text="", font=("roboto", 20), command=lambda: add_task_to_tasks(task_input.get())) #send to the list packer
    submit_button.pack_configure(side='right', padx=1, pady= 1)


# root setup
Root = ctk.CTk()

# general config
ctk.set_default_color_theme('dark-blue')
ctk.set_appearance_mode('dark')
Root.geometry("300x200")
Root.title("listy")

# task list
tasks = ['1', 'task', '3'] 

# instances dict
instances = {}

# a dict whith the names set as the task names, and the values of those names set as the corresponding instance name.
task_instance_pairing = {} 

# main frame
main_frame =  ScrollableFrame(master=Root, width=300, height=500, corner_radius=0, fg_color="transparent")
main_frame.pack(fill='both', expand=True)

task_packer()

# button to destroy all tasks
delete_all_button = ctk.CTkButton(master=main_frame, text='Delete All tasks', font=("roboto", 20), fg_color=("#ffffff", "#424242"), hover_color='red',command=lambda:destroy_all())
delete_all_button.pack_configure(side='bottom', pady=5)

new_task_container()

Root.mainloop()

# TODO list

# TODO fix edge case of user putting in a task with an undescore, with the same name as one with a space
#    EX: task_3, task 3
#    this tries to force the instances dict, to create two identical keys, which is not allowed in python
    
# TODO add a delete when completed function
 
# TODO add ability to save task list to file, or some other form of saving method

# TODO add bottom/side bar (may be collapsable/animated) this is for the light and dark mode function as well as saving, i like bottom bar idea.

# TODO add error reporting to app, so the user knows what is going wrong

# dev comments remove in prod
"""
what is the problem
    i need a check box to appear with a variable
    i need to be able to tell if that check box is checked
    i need the check box inside of a frame
    i need need to be able to create as many as i want
"""