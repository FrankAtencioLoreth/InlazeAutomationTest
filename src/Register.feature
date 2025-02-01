Feature: User registration

  As a new user
  I want to register for an account
  So that I can access the platform and its features

  Background:
    Given I got navigated to home page

  @TC-RU-001 @BUG-TC-RU-001 @REGISTER
  Scenario: Valid user registration
    When I click on the sign up link
    And I fill out the registration form using full name, email and a valid password for the system
      | full name     | email           | password | confirm password |
      | Frank Atencio | random@test.com | Test123. | Test123.         |
    And click on the sign up button
    Then the user is successfully registered in the system "Successful registration!"

  @TC-RU-002 @REGISTER
  Scenario: Registration with only the users name
    When I click on the Sign up link
    And I fill out the registration form using full name, email and a valid password for the system
      | full name | email           | password | confirm password |
      | Frank     | random@test.com | Test123. | Test123.         |
    And in the full name field I only enter a single word
    And click on the sign up button
    Then the user is not registered

  @TC-RU-003 @BUG-TC-RU-003 @REGISTER
  Scenario: Registration with invalid email address
    When I click on the Sign up link
    And I fill out the registration form using full name, email and a valid password for the system
      | full name | email          | password | confirm password |
      | Frank     | randomtest.com | Test123. | Test123.         |
    And click on the button Sing up
    Then the user is not registered

  @TC-RU-004 @REGISTER
  Scenario: Registration with invalid password
    When I click on the Sign up link
    And I fill out the registration form using full name, email and a valid password for the system
      | full name | email          | password | confirm password |
      | Frank     | randomtest.com | Test     | Test             |
    And click on the sign up button
    Then the sign up button is not enabled

  @TC-RU-005 @REGISTER
  Scenario:  Registration with empty form
    When I click on the sign up link
    And I fill out the registration form using full name, email and a valid password for the system
      | full name | email | password | confirm password |
      |           |       |          |                  |
    And I click on the button sign up
    Then the sign up button is not enabled

  @TC-RU-006 @REGISTER
  Scenario:  Registration with wrong password
    When I click on the sign up link
    And I fill out the registration form using full name, email and a valid password for the system
      | full name | email           | password | confirm password |
      | Frank     | random@test.com | Test123. | Test             |
    Then the sign up button is not enabled
    And error message is displayed "Passwords do not match"