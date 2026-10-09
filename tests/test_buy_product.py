from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from pages import payment_page
from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

@pytest.mark.order(1)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up, set_group):
    driver = set_up

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_1()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_information()

    pay = PaymentPage(driver)
    pay.payment()

    f = FinishPage(driver)
    f.finish()

@pytest.mark.order(2)
@allure.description("Test buy product 2")
def test_buy_product_2(set_up, set_group):
    driver = set_up

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_2()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_information()

    pay = PaymentPage(driver)
    pay.payment()

    f = FinishPage(driver)
    f.finish()

@pytest.mark.order(3)
@allure.description("Test buy product 3")
def test_buy_product_3(set_up, set_group):
    driver = set_up

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_3()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInformationPage(driver)
    cip.input_information()

    pay = PaymentPage(driver)
    pay.payment()

    f = FinishPage(driver)
    f.finish()

