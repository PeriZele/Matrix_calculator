import tkinter as tk


def main_menu(master):
    main_menu_frame = tk.Frame(master, width=600, height=400, bg='lightblue', relief="solid", padx=5, pady=5)
  

    padding_weight = int(1)

    main_menu_frame.columnconfigure(0, weight=5)
    main_menu_frame.columnconfigure(1, weight=padding_weight)
    main_menu_frame.columnconfigure(2, weight=5)
    main_menu_frame.columnconfigure(3, weight=padding_weight)
    main_menu_frame.columnconfigure(4, weight=5)
    main_menu_frame.columnconfigure(5, weight=padding_weight)
    main_menu_frame.columnconfigure(6, weight=5)

    main_menu_frame.rowconfigure(0, weight=2)
    main_menu_frame.rowconfigure(1, weight=1)
    main_menu_frame.rowconfigure(2, weight=2)

    add_button = tk.Button(main_menu_frame, bd=1, text="Add")
    substract_button = tk.Button(main_menu_frame, bd=1, text="Substract")
    multiply_button = tk.Button(main_menu_frame, bd=1, text="Multiply")
    inverse_button = tk.Button(main_menu_frame, bd=1, text="Inverse")
    determinant_button = tk.Button(main_menu_frame, bd=1, text="Determinant")
    gauss_button = tk.Button(main_menu_frame, bd=1, text="Gauss-Jordan")
    transpose_button = tk.Button(main_menu_frame, bd=1, text="Transpose")
    rank_button = tk.Button(main_menu_frame, bd=1, text="Rank")

    add_button.grid(column=0, row=0, sticky="nwse")
    substract_button.grid(column=2, row=0, sticky="nwse")
    multiply_button.grid(column=4, row=0, sticky="nwse")
    inverse_button.grid(column=6, row=0, sticky="nwse")
    determinant_button.grid(column=0, row=2, sticky="nwse")
    gauss_button.grid(column=2, row=2, sticky="nwse")
    transpose_button.grid(column=4, row=2, sticky="nwse")
    rank_button.grid(column=6, row=2, sticky="nwse")



    main_menu_frame.pack_propagate(0)
    main_menu_frame.pack()