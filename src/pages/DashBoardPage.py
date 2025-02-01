from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DashBoardPage:

    wellcome_message_xpath = "//h2[contains(text(),'Welcome to Lorem')]"
    menu_xpath = "//label[contains(@class, 'avatar')]"
    logout_option_xpath = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def verify_welcome_message(self, expected_message):
        message = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.wellcome_message_xpath))).text
        assert message.__eq__(expected_message)

    def click_menu(self):
        menu = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, self.menu_xpath)))
        menu.click()

    def click_logout_option(self):
        logout_option = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.LINK_TEXT, self.logout_option_xpath)))
        logout_option.click()