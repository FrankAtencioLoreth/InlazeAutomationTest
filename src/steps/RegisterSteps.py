from behave import given, when, then

@when(u'I click on the sign up link')
def step_impl(context):
    print('STEP: When I click on the sign up link')


@when(u'fill out the registration form using full name, email and a valid password for the system')
def step_impl(context):
    print('STEP: When fill out the registration form using full name, email and a valid password for the system')


@when(u'click on the sign up button')
def step_impl(context):
    print('STEP: When click on the sign up button')


@then(u'the user is successfully registered in the system')
def step_impl(context):
    print('STEP: Then the user is successfully registered in the system')


@when(u'I fill out the registration form using full name, email and a valid password for the system')
def step_impl(context):
    print('STEP: When I fill out the registration form using full name, email and a valid password for the system')


@when(u'in the full name field I only enter a single word')
def step_impl(context):
    print('STEP: When in the full name field I only enter a single word')


@when(u'I click on the sign up button')
def step_impl(context):
    print('STEP: When I click on the sign up button')


@then(u'the sign up button is not enabled')
def step_impl(context):
    print('STEP: Then the sign up button is not enabled')


@when(u'fill in the registration form with an email with standard format')
def step_impl(context):
    print('STEP: When fill in the registration form with an email with standard format')


@when(u'click on the button Sing up')
def step_impl(context):
    print('STEP: When click on the button Sing up')


@when(u'I click on the link Sign up')
def step_impl(context):
    print('STEP: When I click on the link Sign up')


@when(u'fill in the registration form with an invalid password for the system')
def step_impl(context):
    print('STEP: When fill in the registration form with an invalid password for the system')


@when(u'I click on the button sign up')
def step_impl(context):
    print('STEP: When I click on the button sign up')


@when(u'I don\'t fill out the form')
def step_impl(context):
    print('STEP: When I don\'t fill out the form')


@when(u'fill in the form')
def step_impl(context):
    print('STEP: When fill in the form')


@when(u'the password in the field Password does not match the password in the field Repeat your password')
def step_impl(context):
    print('STEP: When the password in the field Password does not match the password in the field Repeat your password')


@then(u'the sign up button is not enabled and an erroneous validation message “Passwords do not match” is displayed')
def step_impl(context):
    print('STEP: Then the sign up button is not enabled and an erroneous validation message “Passwords do not match” is displayed')