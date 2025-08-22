from tkinter import Tk, Frame, Menu

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Diet Planner & Calorie Calculator")
        self.master.geometry("800x600")

        self.create_menu()
        self.create_frames()

    def create_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        user_menu = Menu(menu)
        menu.add_cascade(label="User", menu=user_menu)
        user_menu.add_command(label="Profile", command=self.show_user_profile)
        
        food_menu = Menu(menu)
        menu.add_cascade(label="Food", menu=food_menu)
        food_menu.add_command(label="Database", command=self.show_food_database)

        meal_menu = Menu(menu)
        menu.add_cascade(label="Meal", menu=meal_menu)
        meal_menu.add_command(label="Planner", command=self.show_meal_planner)

        report_menu = Menu(menu)
        menu.add_cascade(label="Reports", menu=report_menu)
        report_menu.add_command(label="View Reports", command=self.show_reports)

    def create_frames(self):
        self.frames = {}
        for F in (UserProfileView, FoodDatabaseView, MealPlannerView, ReportsView):
            page_name = F.__name__
            frame = F(parent=self.master, controller=self)
            self.frames[page_name] = frame

        self.show_frame("UserProfileView")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_user_profile(self):
        self.show_frame("UserProfileView")

    def show_food_database(self):
        self.show_frame("FoodDatabaseView")

    def show_meal_planner(self):
        self.show_frame("MealPlannerView")

    def show_reports(self):
        self.show_frame("ReportsView")

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()