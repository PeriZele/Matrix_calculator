import tkinter as tk
from singleInput import single_input


#functions

# Back to main menu
def handle_main_menu_click():
    remove_current_view()
    display_main_menu()



# Display main menu
def display_main_menu():

    # framing for the menu
    main_menu_frame = tk.Frame(main_frame, width=600, height=400, bg='lightblue', relief="solid", padx=5, pady=5)

    # menu buttons
    single_operaion_button = tk.Button(main_menu_frame, bd=1, text="Single Matrix Operation",   command=handle_single_operation_click)
    multi_operaion_button = tk.Button(main_menu_frame, bd=1, text="Mulitple Matrix Operation")

    # menu frame to keep original size
    main_menu_frame.pack_propagate(0)

    
    main_menu_frame.pack()
    single_operaion_button.pack(side="left")
    multi_operaion_button.pack(side="right")


    # remove the current view

# Destroys all widget in main_frame
def remove_current_view():
    for widget in main_frame.winfo_children():
        widget.destroy()

# main menu handlers
def handle_single_operation_click():
    remove_current_view()
    single_input(main_frame)












# window geometry constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 675

# window generatoin
window = tk.Tk()
window.geometry("900x675")


# framing of the page
header_frame  = tk.Frame(window, width= WINDOW_WIDTH, height = 75,  borderwidth=3, relief="solid" )
main_frame  = tk.Frame(window, width= WINDOW_WIDTH, height = 500,  borderwidth=3, relief="solid" )
footer_frame  = tk.Frame(window, width= WINDOW_WIDTH, height = 100,  borderwidth=3, relief="solid" )

# title
title_label = tk.Label(header_frame,text="Matrix Calculator")

# navigation buttons
home_button = tk.Button(footer_frame, text="MENU", command=handle_main_menu_click)

# frames to to keep original size
header_frame.pack_propagate(False)
main_frame.pack_propagate(False)  
footer_frame.pack_propagate(False)









    






# packing
header_frame.pack()
main_frame.pack()
display_main_menu()
footer_frame.pack()
title_label.pack()
home_button.pack()


# run app
window.mainloop()