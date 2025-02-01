Feature: User registration

  As a new user
  I want to register for an account
  So that I can access the platform and its features

  Background:
    Given I got navigated to home page

  @TC-RU-001
  Scenario: Valid user registration
    When I click on the sign up link
    And fill out the registration form using full name, email and a valid password for the system
    And click on the sign up button
    Then the user is successfully registered in the system

  @TC-RU-002
  Scenario: Registration with only the users name
    When I click on the Sign up link
    And I fill out the registration form using full name, email and a valid password for the system
    And in the full name field I only enter a single word
    And I click on the sign up button
    Then the sign up button is not enabled

  @TC-RU-003
  Scenario: Registration with valid email address
    When I click on the Sign up link
    And fill in the registration form with an email with standard format
    And click on the button Sing up
    Then the user is successfully registered in the system

  @TC-RU-004
  Scenario: Registration with invalid email address
    When I click on the Sign up link
    And fill in the registration form with an email with standard format
    And click on the button Sing up
    Then the user is successfully registered in the system

  @TC-RU-005
  Scenario: Registration with invalid password
    When I click on the link Sign up
    And fill in the registration form with an invalid password for the system
    And I click on the button sign up
    Then the sign up button is not enabled

  @TC-RU-006
  Scenario:  Registration with empty form
    When I click on the sign up link
    And I don't fill out the form
    And I click on the button sign up
    Then the sign up button is not enabled

  @TC-RU-007
  Scenario:  Registration with wrong password verification
    When I click on the sign up link
    And fill in the form
    And the password in the field Password does not match the password in the field Repeat your password
    And I click on the button sign up
    Then the sign up button is not enabled and an erroneous validation message “Passwords do not match” is displayed