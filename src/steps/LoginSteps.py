import time
from behave import given, when, then
from src.pages.LoginPage import LoginPage
from src.pages.DashBoardPage import DashBoardPage

@given(u'I got navigated to home page')
def step_impl(context):
    print('STEP: Given I got navigated to home page')

@when(u'I enter my login credentials')
def step_impl(context):
    login_page = LoginPage(context.driver)
    for rows in context.table:
        login_page.enter_email(rows['email'])
        login_page.enter_password(rows['password'])

@when(u'I click on the sign in button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()

@then(u'the user is redirected to the welcome screen where the user can see his or her user name')
def step_impl(context):
    dashboard_page = DashBoardPage(context.driver)
    for rows in context.table:
        dashboard_page.verify_welcome_message_and_username(rows['username'], rows['welcome message'])

@when(u'I enter my email address')
def step_impl(context):
    login_page = LoginPage(context.driver)
    for rows in context.table:
        login_page.enter_email(rows['email'])

@then(u'the sign in button is not enabled')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.check_button_login_status()

@when(u'the user clicks on the profile icon')
def step_impl(context):
    dashboard_page = DashBoardPage(context.driver)
    dashboard_page.click_menu()

@when(u'clicks on the logout option')
def step_impl(context):
    dashboard_page = DashBoardPage(context.driver)
    dashboard_page.click_logout_option()

@then(u'the user is redirected to the login screen "{message}"')
def step_impl(context, message):
    login_page = LoginPage(context.driver)
    login_page.check_login_title(message)

@when(u'I enter my login credentials for a user that doesn\'t exist')
def step_impl(context):
    login_page = LoginPage(context.driver)
    for rows in context.table:
        login_page.enter_email(rows['email'])
        login_page.enter_password(rows['password'])

@then(u'an informative message is displayed "{message}"')
def step_impl(context, message):
    login_page = LoginPage(context.driver)
    login_page.check_user_not_found_message(message)