def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        return 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    else:
        return 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'super active': 1.9
    }
    return bmr * activity_multipliers.get(activity_level, 1.2)

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height from cm to m
    return weight / (height_m ** 2)

def load_json_file(filepath):
    import json
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json_file(filepath, data):
    import json
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)