# nutrition.py
import openai
from database import Database
from config_loader import load_config

class Nutrition:
    def __init__(self):
        self.db = Database()
        config = load_config()  # Load OpenAI API key
        openai.api_key = config["openai"]["api_key"]

    def create_meal_plan(self, user_id):
        user_data = self.db.get_user_data(user_id)
        fitness_goal = user_data['goal']
        
        prompt = f"Create a weekly meal plan for {fitness_goal}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300
        )
        meal_plan = response.choices[0].text
        self.db.log_meal(user_id, meal_plan)
        print(f"Weekly meal plan: \n{meal_plan}")

    def adjust_macros(self, user_id, progress_data):
        prompt = f"Adjust the meal plan based on the progress: {progress_data['progress']}, Weight change: {progress_data['weight']}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        adjusted_meal_plan = response.choices[0].text
        self.db.log_meal(user_id, adjusted_meal_plan)
        print(f"Adjusted meal plan: \n{adjusted_meal_plan}")
