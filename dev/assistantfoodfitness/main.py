# main.py
from workout import Workout
from nutrition import Nutrition
from habit_tracker import HabitTracker
from progress_tracker import ProgressTracker
from config_loader import load_config
import openai

def chat_interface(user_input):
    config = load_config()
    openai.api_key = config['openai']['api_key']
    
    prompt = f"The user says: {user_input}. Provide fitness or nutritional advice."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    print(response.choices[0].text)

if __name__ == "__main__":
    user_id = 1  # Example user

    # Instantiate components
    workout = Workout()
    nutrition = Nutrition()
    habit_tracker = HabitTracker()
    progress_tracker = ProgressTracker()

    # Example chat interface usage
    user_input = input("Ask your assistant something: ")
    chat_interface(user_input)
