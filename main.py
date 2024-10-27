import tkinter as tk
from GUI.app import App

root = tk.Tk()
window_width = 350
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = screen_width - window_width  # Align to the right
position_y = 0  # Align to the top

if __name__ == "__main__":
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    app = App(root)
    root.mainloop()
