import string
import random
import requests
import data

def generate_random_user_data():
    letters = string.ascii_lowercase + '1234567890'
    email = ''.join(random.choice(letters) for i in range(15))
    password = ''.join(random.choice(letters) for i in range(15))
    return dict(email=f'{email}@stellarburgers.com', password=password, name='Username')

def register_user(user_data):
    for _ in range(10):
        response = requests.post(data.Urls.USER_REGISTER_PAGE, json=user_data)
        if response.status_code == 200:
            user_data['token'] = response.json()["accessToken"]
            return user_data
    raise Exception("User registration failed after 10 attempts")

def delete_user(token):
    headers = dict(Authorization=token)
    for _ in range(10):
        response = requests.delete(data.Urls.USER_AUTHORIZATION_PAGE, headers=headers)
        if response.status_code == 202:
            break