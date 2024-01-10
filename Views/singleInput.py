import tkinter as tk
from tkinter import Label, Entry, Button
import sys  
sys.path.append('/Users/perneszmatyas/Documents/Coding/se_project/Matrix_calculator')
from Functions import functions
import customtkinter

validation_label = None
matrix = None

def clear_input_frame():
    global validation_label
    for widget in single_input_frame.winfo_children():
        widget.destroy()
    validation_label = None

def handle_input_button_click(r, c):
    global validation_label
    if validate_dimensions(r, c):
        clear_input_frame()
        create_matrix(int(r), int(c))
        display_single_operations_menu()
    else:
        if not validation_label:
            validation_label = Label(single_input_frame, text="Invalid input", fg="red")
            validation_label.pack()
        else:
            validation_label.config(text="Invalid Input")

def display_single_operations_menu():
    single_operations_menu_frame = tk.Frame(single_input_frame, bg="#f0f0f0")

    determinant_button = customtkinter.CTkButton(
        master=single_operations_menu_frame,
        command=lambda: handle_determinant_click(get_matrix_values(matrix)),
        text="Determinant",
        text_color="white",
        hover=True,
        hover_color="#3f98d7",
        height=40,
        width=120,
        corner_radius=5,
        border_color="white",
        bg_color="white",
        fg_color="#3b8cc6",
    )

    inverse_button = customtkinter.CTkButton(
        master=single_operations_menu_frame,
        command=lambda: handle_inverse_click(get_matrix_values(matrix)),
        text="Inverse",
        text_color="white",
        hover=True,
        hover_color="#3f98d7",
        height=40,
        width=120,
        corner_radius=5,
        border_color="white",
        bg_color="white",
        fg_color="#3b8cc6",
    )

    rank_button = customtkinter.CTkButton(
        master=single_operations_menu_frame,
        command=lambda: handle_rank_click(get_matrix_values(matrix)),
        text="Rank",
        text_color="white",
        hover=True,
        hover_color="#3f98d7",
        height=40,
        width=120,
        corner_radius=5,
        border_color="white",
        bg_color="white",
        fg_color="#3b8cc6",
    )

    transpose_button = customtkinter.CTkButton(
        master=single_operations_menu_frame,
        command=lambda: handle_transpose_click(get_matrix_values(matrix)),
        text="Transpose",
        text_color="white",
        hover=True,
        hover_color="#3f98d7",
        height=40,
        width=120,
        corner_radius=5,
        border_color="white",
        bg_color="white",
        fg_color="#3b8cc6",
    )

    gauss_button = customtkinter.CTkButton(
        master=single_operations_menu_frame,
        command=lambda: handle_gauss_click(get_matrix_values(matrix)),
        text="Gauss-Jordan",
        text_color="white",
        hover=True,
        hover_color="#3f98d7",
        height=40,
        width=120,
        corner_radius=5,
        border_color="white",
        bg_color="white",
        fg_color="#3b8cc6",
    )

    single_operations_menu_frame.pack(pady=30)

    determinant_button.pack(side="left", padx=5)
    inverse_button.pack(side="left", padx=5)
    rank_button.pack(side="left", padx=5)
    transpose_button.pack(side="left", padx=5)
    gauss_button.pack(side="left", padx=5)

def validate_dimensions(r, c):
    try:
        if 1 < int(r) < 10 and 1 < int(c) < 10 and r and c:
            return True
        else:
            return False
    except:
        return False

def validate_matrix(matrix_values):
    for row in matrix_values:
        for element in row:
            try:
                int(element)
            except:
                return False
    return True

def handle_determinant_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        if len(matrix_values) == len(matrix_values[0]):
            result_value = functions.calcDeterminant(matrix_values)
            clear_input_frame()
            result_label = Label(single_input_frame, text=result_value, font=("Helvetica", 14), bg="#f0f0f0")
            result_label.pack()
        else:
            if not validation_label:
                validation_label = Label(single_input_frame, text="Determinant calculation only applicable with a square matrix", fg="red")
                validation_label.pack()
            else:
                validation_label.config(text="Determinant calculation only applicable with a square matrix")
    else:
        if not validation_label:
            validation_label = Label(single_input_frame, text="Invalid Input", fg="red")
            validation_label.pack()
        else:
            validation_label.config(text="Invalid input")

def handle_inverse_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        if len(matrix_values) == len(matrix_values[0]):
            result_value = functions.calcInverse(matrix_values)
            clear_input_frame()
            result_label = Label(single_input_frame, text=result_value, font=("Helvetica", 14), bg="#f0f0f0")
            result_label.pack()
        else:
            if not validation_label:
                validation_label = Label(single_input_frame, text="Inverse calculation only applicable with a square matrix", fg="red")
                validation_label.pack()
            else:
                validation_label.config(text="Inverse calculation only applicable with a square matrix")
    else:
        if not validation_label:
            validation_label = Label(single_input_frame, text="Invalid Input", fg="red")
            validation_label.pack()
        else:
            validation_label.config(text="Invalid input")

def handle_rank_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        result_value = functions.calcRank(matrix_values)
        clear_input_frame()
        result_label = Label(single_input_frame, text=result_value, font=("Helvetica", 14), bg="#f0f0f0")
        result_label.pack()
    else:
        if not validation_label:
            validation_label = Label(single_input_frame, text="Invalid Input", fg="red")
            validation_label.pack()
        else:
            validation_label.config(text="Invalid input")

def handle_transpose_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        result_value = functions.calcTranspose(matrix_values)
        clear_input_frame()
        result_label = Label(single_input_frame, text=result_value, font=("Helvetica", 14), bg="#f0f0f0")
        result_label.pack()
    else:
        if not validation_label:
            validation_label = Label(single_input_frame, text="Invalid Input", fg="red")
            validation_label.pack()
        else:
            validation_label.config(text="Invalid input")

def handle_gauss_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        result_value = functions.calcGauss(matrix_values)
        clear_input_frame()
        result_label = Label(single_input_frame, text=result_value, font=("Helvetica", 14), bg="#f0f0f0")
        result_label.pack()
    else:
        if not validation_label:
            validation_label = Label(single_input_frame, text="Invalid Input", fg="red")
            validation_label.pack()
        else:
            validation_label.config(text="Invalid input")

def single_input(master):
    global single_input_frame
    single_input_frame = tk.Frame(master, width=500, height=100, bd=1, relief="solid", bg="#f0f0f0", padx=30, pady=30)

    input_label = Label(single_input_frame, text="Dimensions: ", font=("Helvetica", 16), bg="#f0f0f0")
    input_divider = Label(single_input_frame, text=" X ", font=("Helvetica", 16), bg="#f0f0f0")

    input_x = Entry(single_input_frame, bd=1, font=("Helvetica", 14))
    input_y = Entry(single_input_frame, bd=1, font=("Helvetica", 14))

    input_btn = customtkinter.CTkButton(
    master= single_input_frame,
    command=lambda: handle_input_button_click(input_x.get(), input_y.get()),
    text= "Next",
    text_color="white",
    hover= True,
    hover_color= "#3f98d7",
    height=40,
    width= 80,
    corner_radius=5,
    border_color= "white", 
    bg_color="white",
    fg_color= "#3b8cc6")


    single_input_frame.place(relx=0.5, rely=0.5, anchor='center')
    input_label.pack(side="left")
    input_x.pack(side="left")
    input_divider.pack(side="left")
    input_y.pack(side="left")
    input_btn.pack(side="left")

def create_matrix_entry(master, rows, columns):
    global matrix
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            entry = Entry(master, width=5, font=("Helvetica", 14))
            entry.grid(row=i, column=j, padx=5, pady=5)
            row.append(entry)
        matrix.append(row)
    return matrix

def get_matrix_values(matrix):
    return [[float(entry.get()) for entry in row] for row in matrix]

def create_matrix(r, c):
    matrix_frame = tk.Frame(single_input_frame, bg="#f0f0f0")
    matrix_frame.pack()

    # Create a matrix of entry fields
    matrix = create_matrix_entry(matrix_frame, r, c)
