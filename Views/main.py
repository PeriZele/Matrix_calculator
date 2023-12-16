import tkinter as tk
from mainMenu import main_menu



WINDOW_WIDTH = 900
WINDOW_HEIGHT = 675

window = tk.Tk()
window.geometry("900x675")



header_frame  = tk.Frame(window, width= WINDOW_WIDTH, height = 75,  borderwidth=3, relief="solid" )
main_frame  = tk.Frame(window, width= WINDOW_WIDTH, height = 500,  borderwidth=3, relief="solid" )
footer_frame  = tk.Frame(window, width= WINDOW_WIDTH, height = 100,  borderwidth=3, relief="solid" )


header_frame.pack_propagate(False)
main_frame.pack_propagate(False)  
footer_frame.pack_propagate(False)
main_menu(main_frame)




header_frame.pack()
main_frame.pack()
footer_frame.pack()


window.mainloop()