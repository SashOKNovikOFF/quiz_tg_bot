import os
import sqlite3
from environs import Env


# Устанавливаем соединение с базой данных
Env.read_env()
db_path = '/data' if os.environ["AMVERA"] == 1 else 'data'
connection = sqlite3.connect(f'{db_path}/users.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
user_id INTEGER,
username TEXT NOT NULL,
current_points INTEGER,
current_level INTEGER,
current_riddle INTEGER,
total_riddles_num INTEGER
)
''')

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Преобразуем результаты в список словарей
users_list = []
for user in users:
    user_dict = {
        'user_id': user[0],
        'username': user[1],
        'current_points': user[2],
        'current_level': user[3],
        'current_riddle': user[4],
        'total_riddles_num': user[5]
    }
    users_list.append(user_dict)

# Выводим результаты
for user in users_list:
  print(user)

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
