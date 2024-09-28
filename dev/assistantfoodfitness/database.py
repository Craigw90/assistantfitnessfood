# database.py
import os
import mysql.connector
from config_loader import load_config

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
        )
        self.cursor = self.connection.cursor()

    def get_user_data(self, user_id):
        sql = "SELECT * FROM user_profile WHERE user_id = %s"
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchone()

    def log_workout(self, user_id, workout_details):
        sql = "INSERT INTO workout_history (user_id, workout_date, workout_details) VALUES (%s, NOW(), %s)"
        self.cursor.execute(sql, (user_id, workout_details))
        self.connection.commit()

    def log_meal(self, user_id, meal_details):
        sql = "INSERT INTO meal_history (user_id, meal_date, meal_details) VALUES (%s, NOW(), %s)"
        self.cursor.execute(sql, (user_id, meal_details))
        self.connection.commit()
        
    # Other database methods...
