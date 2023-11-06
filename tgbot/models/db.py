import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def db_init(self):
        with self.connection:
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS Users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT DEFAULT '0',
                city TEXT DEFAULT '0',
                age TEXT DEFAULT '0',
                phone TEXT DEFAULT '0'
                )
                """)

    def db_user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def db_get_all_users(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM Users").fetchall()
            return result

    def db_get_all_city_users(self, city):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM Users WHERE city = ?", (city,)).fetchall()
            return result

    def db_add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO Users (user_id) VALUES (?)", (user_id,))

    def db_get_user(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,)).fetchone()

    # def db_get_user_tariff(self, user_id):
    #     with self.connection:
    #          self.cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,)).fetchall()
