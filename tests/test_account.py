import allure
from conftest import *
from page_objects.account_page import AccountPage
from locators.base_page_locators import BasePageLocators
from locators.account_page_locators import AccountPageLocators
from data import Urls


class TestAccount:

    @allure.title("Переход по клику на Личный кабинет без авторизации")
    @allure.description("Нажать кнопку Личный кабинет. Проверить, что текущая страница это страница авторизации")
    def test_account_page_open_not_authorized(self, driver):
        account_page = AccountPage(driver)
        account_page.page_open_not_authorized()
        assert account_page.get_url() == Urls.LOGIN_PAGE

    @allure.title("Переход по клику на Личный кабинет с авторизацей")
    @allure.description("Нажать кнопку Личный кабинет. Проверить, что текущая страница это профиль пользователя")
    def test_account_page_open_authorized(self, driver, random_user_data, random_user_register, random_user_login, random_user_delete):
        account_page = AccountPage(driver)
        account_page.page_open_authorized()
        assert account_page.get_url() == Urls.PROFILE_PAGE

    @allure.title("Переход в раздел История заказов")
    @allure.description("Кликнуть кнопку Личный кабинет, кликнуть на История заказов. Проверить, что текущая страница это страница исотрии заказов")
    def test_account_open_order_history(self, driver, random_user_data, random_user_register, random_user_login, random_user_delete):
        account_page = AccountPage(driver)
        account_page.page_open_order_history()
        assert account_page.get_url() == Urls.ORDER_HISTORY_PAGE

    @allure.title("Выход из аккаунта")
    @allure.description("Кликнуть кнопку Личный кабинет, кликнуть Выход. Проверить, что текщая страница это страница авторизации")
    def test_account_logout(self, driver, random_user_data, random_user_register, random_user_login, random_user_delete):
        account_page = AccountPage(driver)
        account_page.page_logout()
        assert account_page.get_url() == Urls.LOGIN_PAGE