import os
import sqlite3
from environs import Env


# Создаем шаблон заполнения словаря с пользователями
user_dict_template = {
    'username': "",
    'current_points': 0,
    'current_level': 1,
    'current_riddle': 0,
    'current_riddles_list': "",
    'lang': "",
    'tale_num': 0
}

# Инициализируем "базу данных"
users_db = {}


def initialize_database():
    # Устанавливаем соединение с базой данных
    Env.read_env()
    db_path = '/data' if os.environ["AMVERA"] == 1 else 'data'
    connection = sqlite3.connect(f'{db_path}/users.db')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()

    # Преобразуем результаты в список словарей
    for user in users:
        user_dict = {
            'username': user[2],
            'current_points': user[3],
            'current_level': user[4],
            'current_riddle': user[5],
            'current_riddles_list': user[6],
            'lang': user[8],
            'tale_num': user[9]
        }
        users_db[user[1]] = user_dict


def add_userinfo_in_db(user_id: int, user_information: dict):
    # Устанавливаем соединение с базой данных
    Env.read_env()
    db_path = '/data' if os.environ["AMVERA"] == 1 else 'data'
    connection = sqlite3.connect(f'{db_path}/users.db')
    cursor = connection.cursor()
	
    cursor.execute(
        f'INSERT INTO Users (user_id, username, current_points, current_level, '
        f'current_riddle, current_riddles_list, lang, tale_num) '
        f'SELECT ?, ?, ?, ?, ?, ?, ?, ?'
        f'WHERE NOT EXISTS (SELECT * FROM Users WHERE user_id = ?)',
        (user_id, user_information['username'], user_information['current_points'],
         user_information['current_level'], user_information['current_riddle'],
         user_information['current_riddles_list'],
         user_information['lang'], user_information['tale_num'],
         user_id
        )
    )

    connection.commit()
    connection.close()


def update_username_in_db(user_id: int, user_information: dict):
    # Устанавливаем соединение с базой данных
    Env.read_env()
    db_path = '/data' if os.environ["AMVERA"] == 1 else 'data'
    connection = sqlite3.connect(f'{db_path}/users.db')
    cursor = connection.cursor()
    
    cursor.execute(
        f'UPDATE Users SET username = ? WHERE user_id = ?',
        (user_information['username'], user_id)
    )
    
    connection.commit()
    connection.close()


def update_language_in_db(user_id: int, user_information: dict):
    # Устанавливаем соединение с базой данных
    Env.read_env()
    db_path = '/data' if os.environ["AMVERA"] == 1 else 'data'
    connection = sqlite3.connect(f'{db_path}/users.db')
    cursor = connection.cursor()
    
    cursor.execute(
        f'UPDATE Users SET lang = ? WHERE user_id = ?',
        (user_information['lang'], user_id)
    )
    
    connection.commit()
    connection.close()


def update_userinfo_in_db(user_id: int, user_information: dict):
    # Устанавливаем соединение с базой данных
    Env.read_env()
    db_path = '/data' if os.environ["AMVERA"] == 1 else 'data'
    connection = sqlite3.connect(f'{db_path}/users.db')
    cursor = connection.cursor()
	
    cursor.execute(
        f'UPDATE Users SET current_points = ? WHERE user_id = ?',
        (user_information['current_points'], user_id)
    )
    cursor.execute(
        f'UPDATE Users SET current_level = ? WHERE user_id = ?',
        (user_information['current_level'], user_id)
    )
    cursor.execute(
        f'UPDATE Users SET current_riddle = ? WHERE user_id = ?',
        (user_information['current_riddle'], user_id)
    )
    cursor.execute(
        f'UPDATE Users SET current_riddles_list = ? WHERE user_id = ?',
        (user_information['current_riddles_list'], user_id)
    )
    cursor.execute(
        f'UPDATE Users SET tale_num = ? WHERE user_id = ?',
        (user_information['tale_num'], user_id)
    )
    
    connection.commit()
    connection.close()