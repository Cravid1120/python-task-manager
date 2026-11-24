import sqlite3

class Database: 
    
    def __init__(self):
        self.connection = sqlite3.connect("tasks.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            title TEXT,
            completed INTEGER
            )
            """)

    def add_task(self, title):

        self.cursor.execute(
            """
            INSERT INTO tasks (title, completed)
            VALUES (?, ?)
            """,
            (title, 0)
        )

        self.connection.commit()

db = Database()

db.add_task("Buy Milk")

print ("Task saved.")

        

        