# Import necessary Selenium modules
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class RegisterPage:
    """
    This class represents the Register Page and provides methods to interact with its elements.
    """

    # XPath locators for Dashboard elements
    page_title_xpath = "//h1[text()='Sign up']"
    input_fullname_xpath = "//input[@id='full-name']"
    input_email_xpath = "//input[@id='email']"
    input_password_xpath = "//input[@id='password' and @type='password']"
    input_confirm_password_xpath = "//input[@id='confirm-password']"
    button_register_xpath = "//button[@type='submit']"
    error_message_check_password = "//span[text()=' Passwords do not match ']"
    successful_registration_message = "//div[text()='Successful registration!']"

    def __init__(self, driver):
        """
        Initializes the RegisterPage class with the WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver

    def enter_fullname(self, fullname):
        """
        Enters the provided full name into the full name input field.
        :param fullname: Full name to be entered
        """
        input_fullname = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.input_fullname_xpath)))
        input_fullname.clear()
        input_fullname.send_keys(fullname)

    def enter_email(self, email):
        """
        Enters the provided email into the email input field.
        :param email: Email address to be entered
        """
        input_email = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.input_email_xpath)))
        input_email.clear()
        input_email.send_keys(email)

    def enter_password(self, password):
        """
        Enters the provided password into the password input field.
        :param password: Password to be entered
        """
        input_password = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.input_password_xpath)))
        input_password.clear()
        input_password.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        """
        Enters the provided confirmation password into the confirm password input field.
        :param confirm_password: Confirmation password to be entered
        """
        input_confirm_password = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.input_confirm_password_xpath)))
        input_confirm_password.clear()
        input_confirm_password.send_keys(confirm_password)

    def click_register_button(self):
        """
        Clicks the register button if it is enabled.
        """
        time.sleep(5)  # Adding a delay before clicking the button
        register_button = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.button_register_xpath)))

        if register_button.is_enabled():
            register_button.click()
        else:
            print("Register button is not enabled")

    def check_successful_registration_message(self, message):
        """
        Verifies that the success message after registration is displayed correctly.
        :param message: Expected success message text
        """
        expected_message = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.successful_registration_message))).text
        assert expected_message.__eq__(message)

    def check_button_login_status(self):
        """
        Checks if the register button is enabled or disabled and asserts its state.
        """
        login_button = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.button_register_xpath))
        )
        if login_button.get_attribute("disabled").__contains__("disabled"):
            assert login_button.is_enabled() == True  # Assert if the button is enabled
        else:
            assert login_button.is_enabled() == False  # Assert if the button is disabled

    def check_error_message_check_password(self, message):
        """
        Verifies that the password mismatch error message is displayed correctly.
        :param message: Expected error message text
        """
        expected_message = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.error_message_check_password))
        ).text.lstrip().rstrip()
        assert expected_message.__eq__(message)