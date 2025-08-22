class UserController:
    def __init__(self, database_connection):
        self.db_connection = database_connection

    def create_user(self, user_data):
        # Code to insert user_data into the database
        pass

    def update_user(self, user_id, updated_data):
        # Code to update user information in the database
        pass

    def get_user(self, user_id):
        # Code to retrieve user information from the database
        pass

    def calculate_bmr(self, weight, height, age, gender):
        if gender.lower() == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        return bmr

    def calculate_tdee(self, bmr, activity_level):
        activity_multipliers = {
            'sedentary': 1.2,
            'lightly active': 1.375,
            'moderately active': 1.55,
            'very active': 1.725,
            'super active': 1.9
        }
        return bmr * activity_multipliers.get(activity_level, 1.2)