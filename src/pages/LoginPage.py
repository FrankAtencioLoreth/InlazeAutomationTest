from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:

    # XPath locators for the login elements
    page_title_xpath = "//h1[text()='Sign in']"
    input_email_xpath = "//input[@type='email' and @id='email']"
    input_password_xpath = "//input[@type='password' and @id='password']"
    button_login_xpath = "//button[@type='submit']"
    user_not_found_message_xpath = "//div[text()='User not found']"
    url_register_xpath = "Sign up"

    def __init__(self, driver):
        """
       Initializes the LoginPage class with the WebDriver instance.
       :param driver: WebDriver instance
       """
        self.driver = driver

    def enter_email(self, email):
        """
       Enters the provided email into the email input field.
       :param email: Email address to be entered
       """
        input_email = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, self.input_email_xpath)))
        input_email.clear()
        input_email.send_keys(email)

    def enter_password(self, password):
        """
        Enters the provided password into the password input field.
        :param password: Password to be entered
        """
        input_password = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, self.input_password_xpath)))
        input_password.clear()
        input_password.send_keys(password)

    def click_login_button(self):
        """
        Clicks the login button if it is enabled.
        """
        login_button = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.button_login_xpath))
        )
        if login_button.is_enabled():
            login_button.click()
        else:
            print("Login button is not enabled")


    def click_register_link(self):
        """
       Clicks the register link to navigate to the sign-up page.
       """
        url = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, self.url_register_xpath)))
        url.click()


    def check_button_login_status(self):
        """
        Checks if the login button is enabled or disabled and asserts its state.
        """
        login_button = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.button_login_xpath))
        )
        if login_button.is_enabled():
            assert login_button.is_enabled() == True
        else:
            assert login_button.is_enabled() == False

    def check_login_title(self, expected_message):
        """
        Verifies that the login page title matches the expected message.
        :param expected_message: Expected title text
        """
        title = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.page_title_xpath))).text
        assert title.__eq__(expected_message)

    def check_user_not_found_message(self, expected_message):
        """
        Verifies that the "User not found" message is displayed correctly.
        :param expected_message: Expected error message text
       """
        message = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.user_not_found_message_xpath))).text
        assert message.__eq__(expected_message)