import tkinter as tk
import sys
sys.path.append('/Users/perneszmatyas/Documents/Coding/se_project/Matrix_calculator')
from Functions import functions
import numpy as np


validation_label = None
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
            validation_label = tk.Label(single_input_frame, text="Invalid input") 
            validation_label.pack()
        else:
            validation_label.config(text="Invalid Input")

def display_single_operations_menu():


    single_operations_menu_frame = tk.Frame(single_input_frame)

    determinant_button = tk.Button(single_operations_menu_frame, text="Determinant", command= lambda: handle_determinant_click(get_matrix_values(matrix)))
    inverse_button = tk.Button(single_operations_menu_frame, text="Inverse", command= lambda: handle_inverse_click(get_matrix_values(matrix)))
    rank_button = tk.Button(single_operations_menu_frame, text="Rank", command= lambda: handle_rank_click(get_matrix_values(matrix)))
    transpose_button = tk.Button(single_operations_menu_frame, text="Transpose", command= lambda: handle_transpose_click(get_matrix_values(matrix)))
    gauss_button = tk.Button(single_operations_menu_frame, text="Gauss-Jordan", command= lambda: handle_gauss_click(get_matrix_values(matrix)))

    single_operations_menu_frame.pack(pady="30")

    determinant_button.pack(side="left", padx="5")
    inverse_button.pack(side="left", padx="5")
    rank_button.pack(side="left", padx="5" )
    transpose_button.pack(side="left", padx="5")
    gauss_button.pack(side="left", padx="5")

# validate the dimensions input
def validate_dimensions(r, c):
    try:
        if int(r) > 1 and int(r) < 10 and int(c) > 1 and int(c) < 10:
            return True
        else:
            return False
    except:
        return False
        

# validate the matrix itself
def validate_matrix(matrix_values):
    for row in matrix_values:
        for element in row:
            try:
                int(element)
            except:
                return False
    return True



# Single operatoin handlers
def handle_determinant_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        if len(matrix_values) == len(matrix_values[0]):
            result_value = functions.calcDeterminant(matrix_values)
            clear_input_frame()
            result_label = tk.Label(single_input_frame, text=result_value)
            result_label.pack()
        else:
            if not validation_label:
                validation_label = tk.Label(single_input_frame, text="Determinant calculation only applicable with square matrix") 
                validation_label.pack()
            else:
                validation_label.config(text="Determinant calculation only applicable with square matrix")
    else:
        if not validation_label:
                validation_label = tk.Label(single_input_frame, text="Invalid Input") 
                validation_label.pack()
        else:
                validation_label.config(text="Invalid input")
def handle_inverse_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        if len(matrix_values) == len(matrix_values[0]):
            result_value = functions.calcInverse(matrix_values)
            clear_input_frame()
            result_label = tk.Label(single_input_frame, text=result_value)
            result_label.pack()
        else:
            if not validation_label:
                validation_label = tk.Label(single_input_frame, text="Inverse calculation only applicable with square matrix") 
                validation_label.pack()
            else:
                validation_label.config(text="Inverse calculation only applicable with square matrix")
    else:
        if not validation_label:
                validation_label = tk.Label(single_input_frame, text="Invalid Input") 
                validation_label.pack()
        else:
                validation_label.config(text="Invalid input")
def handle_rank_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        # Perform calculations for rank
        clear_input_frame()
        result_label = tk.Label(single_input_frame, text="Rank Result")
        result_label.pack()
    else:
        if not validation_label:
                validation_label = tk.Label(single_input_frame, text="Invalid Input") 
                validation_label.pack()
        else:
                validation_label.config(text="Invalid input")
def handle_transpose_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        # Perform calculations for transpose
        clear_input_frame()
        result_label = tk.Label(single_input_frame, text="Transpose Result")
        result_label.pack()
    else:
        if not validation_label:
                validation_label = tk.Label(single_input_frame, text="Invalid Input") 
                validation_label.pack()
        else:
                validation_label.config(text="Invalid input")
def handle_gauss_click(matrix_values):
    global validation_label
    if validate_matrix(matrix_values):
        result_value = functions.calcGauss(matrix_values)
        clear_input_frame()
        result_label = tk.Label(single_input_frame, text=result_value)
        result_label.pack()
    else:
        if not validation_label:
                validation_label = tk.Label(single_input_frame, text="Invalid Input") 
                validation_label.pack()
        else:
                validation_label.config(text="Invalid input")

def single_input(master):

    global single_input_frame
    single_input_frame = tk.Frame(master, width=500, height=100, bd=3, relief="solid")

    input_label = tk.Label(single_input_frame, text="Dimensions: ")
    input_divider = tk.Label(single_input_frame, text=" X ")

    input_x = tk.Entry(single_input_frame ,bd=1)
    input_y = tk.Entry(single_input_frame ,bd=1)


    input_btn = tk.Button(single_input_frame, text="Next", command=lambda: handle_input_button_click(input_x.get(), input_y.get()))

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
            entry = tk.Entry(master, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row.append(entry)
        matrix.append(row)
    return matrix


def get_matrix_values(matrix):
    return [[float(entry.get()) for entry in row] for row in matrix]

def create_matrix(r, c):
    matrix_frame = tk.Frame(single_input_frame)
    matrix_frame.pack()

    # Create a 3x3 matrix of entry fields
    matrix = create_matrix_entry(matrix_frame, r, c)






