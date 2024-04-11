from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Mod Menu")

def on_option_selected():
    selected_option = option_var.get()
    if selected_option == 1:
        print("Option 1 has been called")
    elif selected_option == 2:
        print("Option 2 has been called")
    elif selected_option == 3:
        print("Option 3 has been called")
    else:
        print("Invalid option")

# Create a frame for the menu
menu_frame = ttk.LabelFrame(root, text="Options")
menu_frame.pack(pady=20)

# Create a variable to store the selected option
option_var = IntVar()

# Create radio buttons for each option
option1 = Radiobutton(menu_frame, text="Option 1", variable=option_var, value=1, command=on_option_selected)
option1.pack(side=LEFT, padx=10)

option2 = Radiobutton(menu_frame, text="Option 2", variable=option_var, value=2, command=on_option_selected)
option2.pack(side=LEFT, padx=10)

option3 = Radiobutton(menu_frame, text="Option 3", variable=option_var, value=3, command=on_option_selected)
option3.pack(side=LEFT, padx=10)

# Create a button to confirm the selection
confirm_button = ttk.Button(root, text="Confirm", command=on_option_selected)
confirm_button.pack(pady=10)

root.mainloop()