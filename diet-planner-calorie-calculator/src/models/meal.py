class Meal:
    def __init__(self):
        self.food_items = []  # List to store food items in the meal
        self.servings = []     # List to store servings for each food item

    def add_food_item(self, food_item, serving):
        self.food_items.append(food_item)
        self.servings.append(serving)

    def calculate_total_calories(self):
        total_calories = 0
        for food_item, serving in zip(self.food_items, self.servings):
            total_calories += food_item.calories * serving
        return total_calories

    def calculate_total_macros(self):
        total_protein = 0
        total_carbs = 0
        total_fat = 0
        for food_item, serving in zip(self.food_items, self.servings):
            total_protein += food_item.protein * serving
            total_carbs += food_item.carbs * serving
            total_fat += food_item.fat * serving
        return total_protein, total_carbs, total_fat

    def clear_meal(self):
        self.food_items.clear()
        self.servings.clear()