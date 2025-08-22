class MealController:
    def __init__(self):
        self.meals = []

    def add_meal(self, food_items):
        meal = {
            'food_items': food_items,
            'total_calories': self.calculate_total_calories(food_items),
            'macros': self.calculate_macros(food_items)
        }
        self.meals.append(meal)

    def calculate_total_calories(self, food_items):
        total_calories = sum(item['calories'] * item['serving_size'] for item in food_items)
        return total_calories

    def calculate_macros(self, food_items):
        total_protein = sum(item['protein'] * item['serving_size'] for item in food_items)
        total_carbs = sum(item['carbs'] * item['serving_size'] for item in food_items)
        total_fat = sum(item['fat'] * item['serving_size'] for item in food_items)
        return {
            'protein': total_protein,
            'carbs': total_carbs,
            'fat': total_fat
        }

    def save_meal_to_log(self, meal):
        # Logic to save the meal to a daily log (e.g., database or file)
        pass

    def get_meals(self):
        return self.meals