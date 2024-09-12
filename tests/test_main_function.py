import allure
from conftest import *
from page_objects.main_page import MainPage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from data import Urls


class TestMainFuncrion:

    @allure.title("Клик на Конструктор")
    @allure.description("Открыть страницу авторизации. Клик по кнопке Конструктор. Проверить, что url изменился и соответсвует главной странице")
    def test_main_page_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.page_open_constructor()
        assert main_page.get_url() == Urls.BASE_URL

    @allure.title("Клик на Лента заказов")
    @allure.description("Клик по Лента заказов. Проверить, что url изменился и соответствует странице с лентой заказов")
    def test_main_page_open_feed(self, driver):
        main_page = MainPage(driver)
        main_page.page_open_feed()
        assert main_page.get_url() == Urls.FEED_PAGE

    @allure.title("Клик по ингредиентам, появится модальное окно")
    @allure.description("Кликнуть по карточке ингредиента. Проверить, что изменился url страницы и в нем добавился id ингредиента")
    def test_main_page_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.page_ingredient_details_modal()
        assert main_page.get_url() == Urls.INGREDIENT_PAGE

    @allure.title("Модальное окно с ифнормацией по ингредиенту закрывается по крестику")
    @allure.description("Кликнуть по карточке ингредиента, в модальном окне кликнуть крестик. Проверить, что модальное окно закрылось отсутствием локатора указывающего на открытую секцию в модальном окне")
    def test_main_page_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.page_ingredient_modal_close()
        assert not main_page.check_page_ingredient_modal_close()

    @allure.title("При добавлении ингредиента в заказ его счетчик увеличивается")
    @allure.description("Запомнить счетчик ингредиента до добавления в заказ. Добавить ингредиент в заказ. Проверить, что счетчик ингредиента увеличился")
    def test_main_page_basket_counter_growth(self, driver):
        main_page = MainPage(driver)
        counter_before, counter_after =  main_page.page_basket_counter_growth()
        assert counter_before < counter_after

    @allure.title("Авторизованный пользователь может оформить заказ")
    @allure.description("Запомнить значение номера заказа в невидимом модальном окне. Добавить несколько ингредиентов в заказ. Кликнуть кнопку оформления заказа. Проверить, что модальное окно стало видимым и номер заказа изменился")
    def test_main_page_place_order_authorized_success(self, driver, random_user_data, random_user_register, random_user_login, random_user_delete):
        main_page = MainPage(driver)
        order_id_before, order_id_after = main_page.page_place_order_authorized_success()
        assert order_id_after != order_id_before and main_page.check_page_ingredient_modal_close()