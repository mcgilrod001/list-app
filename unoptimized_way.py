import customtkinter as ctk
import tkinter


root = ctk.CTk()

# basic window setup
ctk.set_default_color_theme('dark-blue')
ctk.set_appearance_mode('dark')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.title("listy")

my_frame = ctk.CTkScrollableFrame(master=root, width=300, height=200, corner_radius=0, fg_color="transparent")
my_frame.grid(row=0, column=0, sticky="nsew")
main_label = ctk.CTkLabel(master=my_frame, text="listy")
# main_label.grid(row=0, column=0, sticky="nsew")
main_label.grid(row=0, column = 5,)
my_radio_button = ctk.CTkRadioButton(master=my_frame, text="radio button")
# my_radio_button.grid(row=0, column =2, sticky="nsew")

root.mainloop()
# idea is to open and modify another python file with a bunch of radio buttons so when a task is updated it can render.