import tkinter as tk
from tkinter import messagebox
from singleInput import single_input
from multiInput import display_multi_input
import customtkinter

# main_font = customtkinter.CTkFont(family="Helvetica", size=12)


# Function to handle the main menu button click
def handle_main_menu_click():
    remove_current_view()
    display_main_menu()

# Function to remove the current view
def remove_current_view():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Function to display the main menu
def display_main_menu():
    main_menu_frame = tk.Frame(main_frame, width=600, height=400, bg='#f0f0f0', relief="solid", padx=20, pady=20)

    single_operation_button = customtkinter.CTkButton(
    master= main_menu_frame,
    command= handle_single_operation_click,
    text= "Single Matrix Operation",
    text_color="white", 
    hover= True,
    hover_color= "#3f98d7",
    height=80,
    width= 240,
    corner_radius=5,
    border_color= "white", 
    bg_color="white",
    fg_color= "#3b8cc6")

    multi_operation_button = customtkinter.CTkButton(
    master= main_menu_frame,
    command= handle_multi_operation_click,
    text= "Multiple Matrix Operations",
    text_color="white",
    hover= True,
    hover_color= "#3f98d7",
    height=80,
    width= 240,
    corner_radius=5,
    border_color= "white", 
    bg_color="white",
    fg_color= "#3b8cc6")

    main_menu_frame.pack_propagate(0)
    main_menu_frame.pack(fill=tk.BOTH, expand=True)
    single_operation_button.pack(side="left", padx=10)
    multi_operation_button.pack(side="right", padx=10)

# Function to handle the click on single matrix operation button
def handle_single_operation_click():
    remove_current_view()
    single_input(main_frame)

# Function to handle the click on multiple matrix operation button
def handle_multi_operation_click():
    remove_current_view()
    display_multi_input(main_frame)

# Constants for window size
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 675

# Window initialization
window = tk.Tk()
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.title("Matrix Calculator")

# Frames for header, main content, and footer
header_frame = tk.Frame(window, width=WINDOW_WIDTH, height=75, borderwidth=3, relief="solid", bg='#3498db')
main_frame = tk.Frame(window, width=WINDOW_WIDTH, height=500, borderwidth=3, relief="solid", bg='#f0f0f0')
footer_frame = tk.Frame(window, width=WINDOW_WIDTH, height=100, borderwidth=3, relief="solid", bg='#3498db')

# Title label
title_label = tk.Label(header_frame, text="Matrix Calculator", font=("Helvetica", 18, "bold"), bg='#3498db', fg='#ffffff')

# Home button to return to the main menu
home_button = customtkinter.CTkButton(
    master= footer_frame,
    command= handle_main_menu_click,
    text= "Main Menu",
    text_color="black",
    height=40,
    width= 120,
    corner_radius=5,
    bg_color="#3b8cc6",
    fg_color= "white")


# Frame packing to maintain original size
for frame in [header_frame, main_frame, footer_frame]:
    frame.pack_propagate(False)
    frame.pack()

# Packing widgets into frames
title_label.pack(pady=15)
home_button.pack(pady=15)

# Initial display of the main menu
display_main_menu()

# Run the application
window.mainloop()
