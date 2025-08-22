from tkinter import Frame, Label, Entry, Button, Listbox, Scrollbar, StringVar, END, messagebox
import json

class FoodDatabaseView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.food_data = self.load_food_data()
        self.create_widgets()

    def load_food_data(self):
        try:
            with open('src/data/foods.json', 'r') as file:
                return json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load food data: {e}")
            return []

    def create_widgets(self):
        self.label = Label(self, text="Food Database", font=("Arial", 16))
        self.label.pack(pady=10)

        self.search_var = StringVar()
        self.search_entry = Entry(self, textvariable=self.search_var, width=30)
        self.search_entry.pack(pady=5)

        self.search_button = Button(self, text="Search", command=self.search_food)
        self.search_button.pack(pady=5)

        self.food_listbox = Listbox(self, width=50)
        self.food_listbox.pack(pady=10)

        self.scrollbar = Scrollbar(self, command=self.food_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.food_listbox.config(yscrollcommand=self.scrollbar.set)

        self.add_button = Button(self, text="Add Food Item", command=self.add_food_item)
        self.add_button.pack(pady=5)

    def search_food(self):
        search_term = self.search_var.get().lower()
        self.food_listbox.delete(0, END)
        for food in self.food_data:
            if search_term in food['name'].lower():
                self.food_listbox.insert(END, food['name'])

    def add_food_item(self):
        # Placeholder for adding food item functionality
        messagebox.showinfo("Info", "Add food item functionality not implemented yet.")