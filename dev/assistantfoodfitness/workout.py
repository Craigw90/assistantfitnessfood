# workout.py
import openai
from database import Database
from config_loader import load_config

class Workout:
    def __init__(self):
        self.db = Database()
        config = load_config()  # Load config for OpenAI API key
        openai.api_key = config["openai"]["api_key"]

    def create_weekly_plan(self, user_id):
        user_data = self.db.get_user_data(user_id)
        fitness_goal = user_data['goal']
        available_equipment = user_data['equipment']

        workout_plan = self.generate_workout(fitness_goal, available_equipment)
        self.db.log_workout(user_id, workout_plan)
        print(f"Weekly workout plan: \n{workout_plan}")

    def generate_workout(self, fitness_goal, available_equipment):
        prompt = f"Create a weekly workout plan for {fitness_goal}. The user has the following equipment: {available_equipment}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300
        )
        return response.choices[0].text

    def optimize_plan(self, user_id, progress_data):
        prompt = f"Optimize the workout plan based on the following progress: {progress_data['progress']}, Weight change: {progress_data['weight']}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        optimized_plan = response.choices[0].text
        self.db.log_workout(user_id, optimized_plan)
        print(f"Optimized workout: \n{optimized_plan}")
