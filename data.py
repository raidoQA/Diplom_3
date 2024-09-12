import string
import random


class Urls:
    
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    USER_REGISTER_PAGE = f'{BASE_URL}api/auth/register'
    USER_AUTHORIZATION_PAGE = f'{BASE_URL}api/auth/user'
    PROFILE_PAGE = f'{BASE_URL}account/profile'
    ORDER_HISTORY_PAGE = f'{BASE_URL}account/order-history'
    LOGIN_PAGE = f'{BASE_URL}login'
    RECOVERY_INPUT_EMAIL_PAGE = f'{BASE_URL}forgot-password'
    RECOVERY_INPUT_PASSWORD_PAGE = f'{BASE_URL}reset-password'
    FEED_PAGE = f'{BASE_URL}feed'
    INGREDIENT_PAGE = f'{BASE_URL}ingredient/61c0c5a71d1f82001bdaaa6e'


class Credentials:

    EMAIL = 'andreytestovich@ya.ru'
    PASSWORD = 'qqAAqq12345'