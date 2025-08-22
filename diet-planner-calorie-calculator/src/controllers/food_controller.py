class FoodController:
    def __init__(self, food_database):
        self.food_database = food_database

    def add_food_item(self, food_item):
        self.food_database.append(food_item)

    def search_food_item(self, name):
        return [food for food in self.food_database if food['name'].lower() == name.lower()]

    def select_food_item(self, food_id):
        for food in self.food_database:
            if food['id'] == food_id:
                return food
        return None

    def get_all_food_items(self):
        return self.food_database