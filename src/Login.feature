Feature: User login

  As a registered user
  I want to log in to my account
  So that I can access my personalized dashboard

  Background:
    Given I got navigated to home page

  @TC-LG-001 @LOGIN
  Scenario: Successful Login
    When I enter my login credentials
      | email           | password |
      | inlaze@test.com | Test123. |
    And I click on the sign in button
    Then the user is redirected to the welcome screen where the user can see his or her user name
      | username    | welcome message  |
      | inlaze test | Welcome to Lorem |

  @TC-LG-002 @LOGIN
  Scenario: Incomplete form
    When I enter my email address
      | email           |
      | inlaze@test.com |
    And I click on the sign in button
    Then the sign in button is not enabled

  @TC-LG-003 @LOGIN
  Scenario: Logout
    When I enter my login credentials
      | email           | password |
      | inlaze@test.com | Test123. |
    And I click on the sign in button
    Then the user is redirected to the welcome screen where the user can see his or her user name
      | username    | welcome message  |
      | inlaze test | Welcome to Lorem |
    When the user clicks on the profile icon
    And clicks on the logout option
    Then the user is redirected to the login screen "Sign in"

  @TC-LG-004 @LOGIN
  Scenario: Login unsuccessful
    When I enter my login credentials for a user that doesn't exist
      | email            | password |
      | inlaze@test1.com | Test123. |
    And I click on the sign in button
    Then an informative message is displayed "User not found"
