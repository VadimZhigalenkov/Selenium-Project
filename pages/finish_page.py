from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class FinishPage(Base):


    # Methods

    def finish(self):
        with allure.step("finish"):
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")


