import tkinter as tk

def clear_input_frame():
    for widget in single_input_frame.winfo_children():
        widget.destroy()

def handle_input_button_click(r, c):
    clear_input_frame()
    create_matrix(r, c)
    display_single_operations_menu()

def display_single_operations_menu():

    single_operations_menu_frame = tk.Frame(single_input_frame)

    determinant_button = tk.Button(single_operations_menu_frame, text="Determinant", command= lambda: handle_determinant_click(get_matrix_values(matrix)))
    inverse_button = tk.Button(single_operations_menu_frame, text="Inverse")
    rank_button = tk.Button(single_operations_menu_frame, text="Rank")
    transpose_button = tk.Button(single_operations_menu_frame, text="Transpose")
    gauss_button = tk.Button(single_operations_menu_frame, text="Gauss-Jordan")

    single_operations_menu_frame.pack(pady="30")

    determinant_button.pack(side="left", padx="5")
    inverse_button.pack(side="left", padx="5")
    rank_button.pack(side="left", padx="5" )
    transpose_button.pack(side="left", padx="5")
    gauss_button.pack(side="left", padx="5")
    
def handle_determinant_click(matrix_values):
    print(matrix_values)
    #do the calculations
    clear_input_frame()
    result_label = tk.Label(single_input_frame, text=matrix_values)
    result_label.pack()

def handle_inverse_click(matrix_values):
    print(matrix_values)
    # Perform calculations for inverse
    clear_input_frame()
    result_label = tk.Label(single_input_frame, text="Inverse Matrix Result")
    result_label.pack()


def handle_rank_click(matrix_values):
    print(matrix_values)
    # Perform calculations for rank
    # ...
    clear_input_frame()
    result_label = tk.Label(single_input_frame, text="Rank Result")
    result_label.pack()


def handle_transpose_click(matrix_values):
    print(matrix_values)
    # Perform calculations for transpose
    clear_input_frame()
    result_label = tk.Label(single_input_frame, text="Transpose Result")
    result_label.pack()


def handle_gauss_jordan_click(matrix_values):
    print(matrix_values)
    # Perform calculations for Gauss-Jordan elimination
    clear_input_frame()
    result_label = tk.Label(single_input_frame, text="Gauss-Jordan Result")
    result_label.pack()

def single_input(master):

    global single_input_frame
    single_input_frame = tk.Frame(master, width=500, height=100, bd=3, relief="solid")

    input_label = tk.Label(single_input_frame, text="Dimensions: ")
    input_divider = tk.Label(single_input_frame, text=" X ")

    input_x = tk.Entry(single_input_frame ,bd=1)
    input_y = tk.Entry(single_input_frame ,bd=1)


    input_btn = tk.Button(single_input_frame, text="Next", command=lambda: handle_input_button_click(int(input_x.get()), int(input_y.get())))

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
    return [[entry.get() for entry in row] for row in matrix]

def create_matrix(r, c):
    matrix_frame = tk.Frame(single_input_frame)
    matrix_frame.pack()

    # Create a 3x3 matrix of entry fields
    matrix = create_matrix_entry(matrix_frame, r, c)






