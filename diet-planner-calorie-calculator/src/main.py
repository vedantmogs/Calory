import tkinter as tk
from views.main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("Diet Planner & Calorie Calculator")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()