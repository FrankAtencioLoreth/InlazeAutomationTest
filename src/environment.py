import allure
from selenium import webdriver
from src.utilities import ConfigReader


def before_scenario(context, driver):
    """
    This function is executed before each scenario.
    It reads the browser type from the configuration file and initializes the WebDriver accordingly.
    """

    browser_name = ConfigReader.read_config("config", "browser")
    url = ConfigReader.read_config("config", "url")

    match browser_name:
        case "chrome":
            context.driver = webdriver.Chrome()
        case "edge":
            context.driver = webdriver.Edge()
        case "firefox":
            context.driver = webdriver.Firefox()
        case _:
            print("Error to select browser. Please set one browser")

    context.driver.implicitly_wait(20)
    context.driver.maximize_window()
    context.driver.get(url)

def after_scenario(context, driver):
    """
    This function is executed after each scenario.
    It closes the WebDriver to clean up resources.
    """
    context.driver.quit()

def after_step(context, step):
    """
    This function is executed after each step.
    It's take screenshot if the step failed.
    """
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="failed_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )