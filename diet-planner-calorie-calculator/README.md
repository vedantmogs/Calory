# Diet Planner & Calorie Calculator

## Overview
The Diet Planner & Calorie Calculator is a Python application built using Tkinter that helps users manage their dietary needs by providing features for user profiles, a food database, meal planning, and reporting. This application is designed to assist users in tracking their calorie intake and making informed dietary choices.

## Features
- **User Profiles**: Create and manage user profiles, including personal information and dietary preferences.
- **Food Database**: Access a comprehensive database of food items with nutritional information.
- **Meal Planner**: Plan meals by selecting food items and calculating total calories and macronutrients.
- **Reports**: Generate daily and weekly reports on calorie intake and visualize data using charts.
- **Extra Features**: Additional functionalities such as BMR and TDEE calculations to help users understand their caloric needs.

## Project Structure
```
diet-planner-calorie-calculator
├── src
│   ├── main.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── user_controller.py
│   │   ├── food_controller.py
│   │   ├── meal_controller.py
│   │   └── report_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── food.py
│   │   ├── meal.py
│   │   └── report.py
│   ├── views
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── user_profile.py
│   │   ├── food_database.py
│   │   ├── meal_planner.py
│   │   └── reports.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── data
│       ├── __init__.py
│       ├── foods.json
│       └── users.json
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd diet-planner-calorie-calculator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/main.py
   ```
2. Follow the on-screen instructions to create a user profile, add food items, plan meals, and generate reports.

## Requirements
- Python 3.x
- Tkinter
- SQLite
- Matplotlib

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.