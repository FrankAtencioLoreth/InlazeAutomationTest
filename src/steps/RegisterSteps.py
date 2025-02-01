from behave import when, then
from src.pages.LoginPage import LoginPage
from src.pages.RegisterPage import RegisterPage

@when(u'I click on the sign up link')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_register_link()

@when(u'click on the sign up button')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.click_register_button()

@when(u'I fill out the registration form using full name, email and a valid password for the system')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    print(f'LOG: {context.table}')
    for rows in context.table:
        register_page.enter_fullname(rows['full name'])
        register_page.enter_email(rows['email'])
        register_page.enter_password(rows['password'])
        register_page.enter_confirm_password(rows['confirm password'])

@then(u'the user is not registered')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.check_button_login_status()

@then(u'error message is displayed "{message}"')
def step_impl(context, message):
    register_page = RegisterPage(context.driver)
    register_page.check_error_message_check_password(message)

@then(u'the user is successfully registered in the system "{expected_message}"')
def step_impl(context, message):
   register_page = RegisterPage(context.driver)
   register_page.check_successful_registration_message(message)

@then(u'the sign up button is not enabled')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.check_button_login_status()