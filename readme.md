# Automation Testing Project with Behave and Allure

This project is designed for automated testing using **Behave**, a Behavior Driven Development (BDD) framework, and **Allure** for generating detailed test reports.

## Installation Requirements

Before getting started, ensure you meet the following requirements and install the necessary tools:

### Prerequisites

1. **Python**: Ensure Python >= 3.7 is installed on your machine.
2. **pip**: Install pip, Python's package installer.
3. **Supported Browser**: The project is configured to execute on the `Edge`,`Chrome` or `Firefox`  browser.
4. **Allure v2.32.0**:  Is a popular open source tool for visualizing the results of a test run. It can be added to your testing workflow with little to zero configuration [here](https://allurereport.org/docs/install-for-windows/)
5. **Scoop**: For install allure in windows [here](https://github.com/ScoopInstaller/Install#readme)
6. **Node v22.12.0**: It's required for execute allure reports [here](https://nodejs.org/en/blog/release/v22.11.0)
7. **Java JDK v17 and JAVA_HOME**: It's required for execute allure reports [here](https://openjdk.org/projects/jdk/17/)
8. **Selenium v4.28.1**: For automation testing [here](https://www.selenium.dev/documentation/)
9. **Behave v1.2.6**: For bdd style [here](https://behave.readthedocs.io/en/latest/)

### Dependency installation

Run the following commands to install the required dependencies:

1. Install necessary libraries in this project:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up **Allure** (optional):

   - Download and install Scoop (Windows PowerShell):
    ```bash
   irm get.scoop.sh | iex
   ```
   - Download and install Allure:
   ```bash
   scoop install allure
   ```

## How to execute tests with Behave

To execute tests using **Behave**, run these commands from the project root directory:

1. Run all tests:
   ```bash
   behave -f allure_behave.formatter:AllureFormatter -o reports/ .\src\
   ```

2. Run specific tests based on tags:
   ```bash
   behave --tags=@tag_name -f allure_behave.formatter:AllureFormatter -o reports/ .\src\
   ```
   
## Generate reports with Allure

This project is configured to generate reports using **Allure**. Follow the steps below to generate the test report:

1. Run the automated tests
2. Open the cmd console and type the following command
  ```bash
    allure serve reports
   ```

## Project structure

The project follows a standard structure for tests using **Behave**:
  ```
├───.venv
│   ├───Lib
│   └───Scripts
├───configurations
│   ├───config.ini
├───docs
├───reports
└───src
    ├───pages
	 ├───DashBoardPage.py
	 ├───LoginPage.py
	 ├───RegisterPage.py
    ├───steps
	 ├───RegisterSteps.py
	 ├───LoginSteps.py
    ├───utilities
	 ├───ConfigReader.py
    ├───environment.py
    ├───Login.feature
├───requirements.txt

   ```
