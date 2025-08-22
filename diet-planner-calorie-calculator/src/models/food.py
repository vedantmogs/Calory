class Food:
    def __init__(self, food_id, name, serving_size, calories, protein, carbs, fat):
        self.food_id = food_id
        self.name = name
        self.serving_size = serving_size
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def __repr__(self):
        return f"Food(id={self.food_id}, name={self.name}, serving_size={self.serving_size}, calories={self.calories}, protein={self.protein}, carbs={self.carbs}, fat={self.fat})"