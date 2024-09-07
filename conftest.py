import allure
import string
import random
import pytest
import requests
import data
from selenium import webdriver
from page_objects.account_page import AccountPage

@allure.step("Запустить браузер. Перейти на главную страницу Stellar Burgers. "
             " Вернуть тип браузера. Закрыть браузер по завершении теста")
@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.get(data.Urls.BASE_URL)
    yield browser
    browser.quit()

@allure.step("Авторизоваться. Дождаться перехода на главную страницу")
@pytest.fixture(scope='function')
def random_user_login(driver, random_user_register):
    page = AccountPage(driver)
    page.page_authorized(random_user_register['email'], random_user_register['password'])

@allure.step("Удалить рандомного пользователя по завершении теста")
@pytest.fixture(scope='function')
def random_user_delete(driver, random_user_register):
    yield
    headers = dict(Authorization=random_user_register['token'])
    wait_ten = 0
    while wait_ten != 10:
        response = requests.delete(data.Urls.USER_AUTHORIZATION_PAGE, headers=headers)
        wait_ten += 1 if response.status_code != 202 else 10

@allure.step("Генерация рандомных данных для регистрации нового пользователя, Вернуть данные")
@pytest.fixture(scope='function')
def random_user_data():
    letters = string.ascii_lowercase + '1234567890'
    email = ''.join(random.choice(letters) for i in range(15))
    password = ''.join(random.choice(letters) for i in range(15))
    random_body = dict(email=f'{email}@stellarburgers.com', password=password, name='Username')
    return random_body

@allure.step("Зарегистрировать нового рандомного пользователя. Вернуть учетные данные и токен авторизации")
@pytest.fixture(scope='function')
def random_user_register(random_user_data):
    wait_ten = 0
    while wait_ten != 10:
        response = requests.post(data.Urls.USER_REGISTER_PAGE, json=random_user_data)
        wait_ten += 1 if response.status_code != 200 else 10
    random_user_data['token'] = response.json()["accessToken"]
    return random_user_data