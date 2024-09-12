import allure
import pytest
from selenium import webdriver
from page_objects.account_page import AccountPage
import helpers
import data

@allure.step("Запустить браузер. Перейти на главную страницу Stellar Burgers. Вернуть тип браузера. Закрыть браузер по завершении теста")
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
def random_user_delete(random_user_register):
    yield
    helpers.delete_user(random_user_register['token'])

@allure.step("Генерация рандомных данных для регистрации нового пользователя")
@pytest.fixture(scope='function')
def random_user_data():
    return helpers.generate_random_user_data()

@allure.step("Зарегистрировать нового рандомного пользователя. Вернуть учетные данные и токен авторизации")
@pytest.fixture(scope='function')
def random_user_register(random_user_data):
    return helpers.register_user(random_user_data)
