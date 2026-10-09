from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure

class LoginPage(Base):

    url = 'https://www.saucedemo.com/'

    #locators

    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'

    standard_user_name = "standard_user"
    standard_password = "secret_sauce"

    main_word = '//span[@data-test="title"]'

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_username(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("click login button")

    # Methods

    def authorization(self):
        with allure.step("authorization"):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.get_current_url()
            self.input_username(self.standard_user_name)
            self.input_password(self.standard_password)
            self.click_login_button()
            self.assert_word(self.get_main_word(), 'Products')
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

