from tkinter import Frame, Label, Entry, Button, StringVar, IntVar, messagebox
from controllers.user_controller import UserController

class UserProfileView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.user_controller = UserController()
        self.init_ui()

    def init_ui(self):
        self.master.title("User Profile")
        
        Label(self, text="Age:").grid(row=0, column=0)
        self.age_var = IntVar()
        Entry(self, textvariable=self.age_var).grid(row=0, column=1)

        Label(self, text="Gender:").grid(row=1, column=0)
        self.gender_var = StringVar()
        Entry(self, textvariable=self.gender_var).grid(row=1, column=1)

        Label(self, text="Weight (kg):").grid(row=2, column=0)
        self.weight_var = IntVar()
        Entry(self, textvariable=self.weight_var).grid(row=2, column=1)

        Label(self, text="Height (cm):").grid(row=3, column=0)
        self.height_var = IntVar()
        Entry(self, textvariable=self.height_var).grid(row=3, column=1)

        Label(self, text="Activity Level:").grid(row=4, column=0)
        self.activity_var = StringVar()
        Entry(self, textvariable=self.activity_var).grid(row=4, column=1)

        Button(self, text="Calculate BMR & TDEE", command=self.calculate).grid(row=5, columnspan=2)

        self.result_label = Label(self, text="")
        self.result_label.grid(row=6, columnspan=2)

    def calculate(self):
        try:
            age = self.age_var.get()
            gender = self.gender_var.get()
            weight = self.weight_var.get()
            height = self.height_var.get()
            activity_level = self.activity_var.get()

            bmr, tdee = self.user_controller.calculate_bmr_tdee(age, gender, weight, height, activity_level)
            self.result_label.config(text=f"BMR: {bmr:.2f} kcal, TDEE: {tdee:.2f} kcal")
        except Exception as e:
            messagebox.showerror("Error", str(e))