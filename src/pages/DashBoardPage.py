# Import necessary Selenium modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DashBoardPage:
    """
    This class represents the Dashboard Page and provides methods to interact with its elements.
    """

    # XPath locators for Dashboard elements
    wellcome_message_xpath = "//h2[contains(text(),'Welcome to Lorem')]"
    menu_xpath = "//label[contains(@class, 'avatar')]"
    username_xpath = "(//h2)[1]"
    logout_option_xpath = "Logout"

    def __init__(self, driver):
        """
        Initializes the DashBoardPage class with the WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver

    def verify_welcome_message_and_username(self, username, message):
        """
        Verifies that the welcome message is displayed correctly.
        :param message: Expected text of the welcome message
        :param username: Expected username
        """
        expected_message = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.wellcome_message_xpath))).text
        assert message.__eq__(expected_message)

        expected_username = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.username_xpath))).text
        assert username.__eq__(expected_username)

    def click_menu(self):
        """
       Clicks the menu button to open the navigation menu.
       """
        menu = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, self.menu_xpath)))
        menu.click()

    def click_logout_option(self):
        """
        Clicks the logout option to log out of the application.
        """
        logout_option = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.LINK_TEXT, self.logout_option_xpath)))
        logout_option.click()