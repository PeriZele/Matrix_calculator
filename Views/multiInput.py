import tkinter as tk




def clear_input_frame():
    for widget in multi_input_frame.winfo_children():
        widget.destroy()


validation_label = None
def handle_input_button_click(r1, c1, r2, c2):
    global validation_label
    print(r1, c1, r2, c2)
    if validate_dimensions(r1, c1, r2, c2):
        clear_input_frame()
        create_matrices(int(r1), int(c1), int(r2), int(c2))
        #display_single_operations_menu()
    else:
        if not validation_label:
            validation_label = tk.Label(multi_input_frame, text="Invalid input") 
            validation_label.pack()
        else:
            validation_label.config(text="Invalid Input")


def validate_dimensions(r1, c1, r2, c2):
    try:
        if int(r1) > 1 and int(r1) < 10 and int(c1) > 1 and int(c1) < 10 and int(r2) > 1 and int(r2) < 10 and int(c2) > 1 and int(c2) < 10:
            return True
        else:
            return False
    except:
        return False
        


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


def get_matrix_values(matrix_1, matrix_2):
    return [[[entry.get() for entry in row] for row in matrix_1], [[entry.get() for entry in row] for row in matrix_2]]

def create_matrices(r1, c1, r2, c2):
    matrix_frame_1 = tk.Frame(multi_input_frame)
    matrix_frame_2 = tk.Frame(multi_input_frame)

    matrix_frame_1.pack(side="left")
    matrix_frame_2.pack(side="right")



    matrix_1 = create_matrix_entry(matrix_frame_1, r1, c1)
    matrix_2 = create_matrix_entry(matrix_frame_2, r2, c2)




def display_multi_input(master):
    global multi_input_frame
    multi_input_frame = tk.Frame(master, width=500, height=100, bd=3, relief="solid")
    
    multi_input_frame_upper = tk.Frame(multi_input_frame,  bd=3, relief="solid")
    multi_input_frame_lower = tk.Frame(multi_input_frame,  bd=3, relief="solid")


    input_label_1 = tk.Label(multi_input_frame_upper, text="Matrix 1: ")
    input_divider_1 = tk.Label(multi_input_frame_upper, text=" X ")

    input_x_1 = tk.Entry(multi_input_frame_upper ,bd=1)
    input_y_1 = tk.Entry(multi_input_frame_upper ,bd=1)

    input_label_2 = tk.Label(multi_input_frame_lower, text="Matrix 2: ")
    input_divider_2 = tk.Label(multi_input_frame_lower, text=" X ")

    input_x_2 = tk.Entry(multi_input_frame_lower ,bd=1)
    input_y_2 = tk.Entry(multi_input_frame_lower ,bd=1)


    input_btn = tk.Button(multi_input_frame, text="Next", command=lambda: handle_input_button_click(input_x_1.get(), input_y_1.get(), input_x_2.get(), input_y_2.get()))

    multi_input_frame.place(relx=0.5, rely=0.5, anchor='center')
    multi_input_frame_upper.pack()
    multi_input_frame_lower.pack()

    input_label_1.pack(side="left")
    input_x_1.pack(side="left")
    input_divider_1.pack(side="left")
    input_y_1.pack(side="left")
    input_label_2.pack(side="left")
    input_x_2.pack(side="left")
    input_divider_2.pack(side="left")
    input_y_2.pack(side="left")
    input_btn.pack(side="left")



