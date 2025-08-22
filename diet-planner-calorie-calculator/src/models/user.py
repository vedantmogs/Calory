class User:
    def __init__(self, age, gender, weight, height, activity_level):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.bmr = self.calculate_bmr()
        self.tdee = self.calculate_tdee()

    def calculate_bmr(self):
        if self.gender.lower() == 'male':
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

    def calculate_tdee(self):
        activity_multiplier = {
            'sedentary': 1.2,
            'lightly active': 1.375,
            'moderately active': 1.55,
            'very active': 1.725,
            'super active': 1.9
        }
        return self.bmr * activity_multiplier.get(self.activity_level, 1.2)