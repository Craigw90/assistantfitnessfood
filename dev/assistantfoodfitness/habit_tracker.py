# habit_tracker.py
class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, user_id, habit):
        if user_id not in self.habits:
            self.habits[user_id] = []
        self.habits[user_id].append(habit)

    def track_habit(self, user_id, habit):
        if user_id in self.habits and habit in self.habits[user_id]:
            print(f"Habit '{habit}' tracked for user {user_id}.")
        else:
            print(f"Habit '{habit}' not found for user {user_id}.")
