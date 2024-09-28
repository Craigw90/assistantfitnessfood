# progress_tracker.py
class ProgressTracker:
    def __init__(self):
        self.progress_data = {}

    def add_progress(self, user_id, weight, workouts_completed):
        self.progress_data[user_id] = {
            'weight': weight,
            'workouts_completed': workouts_completed
        }

    def get_progress(self, user_id):
        return self.progress_data.get(user_id, {})
