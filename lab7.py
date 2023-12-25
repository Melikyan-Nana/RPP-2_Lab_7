import requests
import time

url = 'http://127.0.0.1:5000/v1/login'


# Изменяем данные в каждом задании для проверки
users_list = [
    {"email": "xtra1@bk.ru", "password": "1234560"},
    {"email": "xtra2@bk.ru", "password": "1234561"},
    {"email": "xtra3@bk.ru", "password": "1234562"},
    {"email": "xtra4@bk.ru", "password": "1234563"},
    {"email": "xtra5@bk.ru", "password": "1234564"},
    {"email": "xtra6@bk.ru", "password": "1234565"},
    {"email": "xtra7@bk.ru", "password": "1234566"},
    {"email": "xtra8@bk.ru", "password": "1234567"},
    {"email": "xtra9@bk.ru", "password": "1234568"},
    {"email": "xtra10@bk.ru", "password": "1234569"},
    {"email": "xtra11@bk.ru", "password": "1234570"},
    {"email": "xtra12@bk.ru", "password": "1234571"},
    {"email": "xtra13@bk.ru", "password": "1234572"},
    {"email": "xtra7@bk.ru", "password": "1234566"},
    {"email": "xtra9@bk.ru", "password": "1234568"},
    {"email": "xtra10@bk.ru", "password": "1234569"},
    {"email": "xtra11@bk.ru", "password": "1234570"},
    {"email": "xtra12@bk.ru", "password": "1234571"},
    {"email": "xtra13@bk.ru", "password": "1234572"},
    {"email": "xtra7@bk.ru", "password": "1234566"},
    {"email": "xtra4@bk.ru", "password": "1234563"},
    {"email": "xtra9@bk.ru", "password": "1234568"},
    {"email": "xtra5@bk.ru", "password": "1234564"},
    {"email": "xtra10@bk.ru", "password": "1234569"},
    {"email": "xtra12@bk.ru", "password": "1234571"},
    {"email": "xtra13@bk.ru", "password": "12345672"}
]

for user in users_list:
    payload = {
        'email': user['email'],
        'password': user['password']}
    response = requests.post(url, data=payload)

    if response.status_code == 429:
        print(f'Слишком много запросов. Пауза на 1 минуту...,  {response.status_code}')
        time.sleep(60)
    elif response.status_code == 200:
        print(f'Username: {user["email"]}, Password: {user["password"]}, {response.status_code}')
        break
    else:
        print(f'Неверно введены данные, {response.status_code}')
        continue
