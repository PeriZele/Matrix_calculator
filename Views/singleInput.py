import tkinter as tk

def clear_input_frame():
    for widget in single_input_frame.winfo_children():
        widget.destroy()

def handle_input_button_click():
    clear_input_frame()
    create_matrix()

def single_input(master):

    global single_input_frame
    single_input_frame = tk.Frame(master, width=500, height=100, bd=3, relief="solid")

    input_label = tk.Label(single_input_frame, text="Dimensions: ")
    input_divider = tk.Label(single_input_frame, text=" X ")

    input_x = tk.Entry(single_input_frame ,bd=1)
    input_y = tk.Entry(single_input_frame ,bd=1)

    input_btn = tk.Button(single_input_frame, text="Next", command=handle_input_button_click)

    single_input_frame.place(relx=0.5, rely=0.5, anchor='center')
    input_label.pack(side="left")
    input_x.pack(side="left")
    input_divider.pack(side="left")
    input_y.pack(side="left")
    input_btn.pack(side="left")



def create_matrix_entry(master, rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            entry = tk.Entry(master, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row.append(entry)
        matrix.append(row)
    return matrix


def create_matrix():
    rows = 3
    columns = 3

    matrix_frame = tk.Frame(single_input_frame)
    matrix_frame.pack()

    # Create a 3x3 matrix of entry fields
    matrix = create_matrix_entry(matrix_frame, rows, columns)



