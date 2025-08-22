from tkinter import Frame, Label, Button, Listbox, StringVar, Entry, END, Scrollbar, messagebox
from controllers.food_controller import FoodController

class MealPlannerView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.food_controller = FoodController()
        self.selected_food_items = []

        self.init_ui()

    def init_ui(self):
        self.master.title("Meal Planner")
        
        Label(self, text="Meal Planner", font=("Helvetica", 16)).pack(pady=10)

        self.food_listbox = Listbox(self, selectmode='multiple', width=50)
        self.food_listbox.pack(pady=10)

        self.populate_food_list()

        Button(self, text="Add to Meal", command=self.add_to_meal).pack(pady=5)
        Button(self, text="Calculate Total", command=self.calculate_total).pack(pady=5)

        self.total_label = Label(self, text="Total Calories: 0")
        self.total_label.pack(pady=10)

        self.pack()

    def populate_food_list(self):
        foods = self.food_controller.get_all_foods()
        for food in foods:
            self.food_listbox.insert(END, f"{food['name']} - {food['calories']} cal")

    def add_to_meal(self):
        selected_indices = self.food_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Selection Error", "Please select at least one food item.")
            return
        
        for index in selected_indices:
            food_item = self.food_controller.get_food_by_index(index)
            self.selected_food_items.append(food_item)

        messagebox.showinfo("Success", "Food items added to meal.")

    def calculate_total(self):
        total_calories = sum(item['calories'] for item in self.selected_food_items)
        self.total_label.config(text=f"Total Calories: {total_calories}")