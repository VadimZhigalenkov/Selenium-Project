from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure

class ClientInformationPage(Base):

    #locators

    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    faker = Faker()

    fake_first_name = faker.first_name()
    fake_last_name = faker.last_name()
    fake_postal_code = faker.postcode()

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name(). send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("input postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue")

    # Methods

    def input_information(self):
        with allure.step("input information"):
            Logger.add_start_step(method='input_information')
            self.get_current_url()
            self.input_first_name(self.fake_first_name)
            self.input_last_name(self.fake_last_name)
            self.input_postal_code(self.fake_postal_code)
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_information")


