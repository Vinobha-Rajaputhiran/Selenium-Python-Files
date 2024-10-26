"""
Using Data Driven Testing Framework (DDTF), Page Object Model (POM), Explicit wait, Expected Conditions and Pytest kindly do the following tests:_

    1. Create an Excel file which will comprise of Test ID, Username, Password, Date, Time of Test, Name of Tester, Test Result for login into the portal.
    2. Go to the URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    3. Login into the page using the username and password provided in the Excel file. Try to use five username and password.
    4. If the login is successful your Python Code will write in the Excel file whether your Test Passed or Failed.
    5. Do not use sleep() method.

"""

"""
test_orange.py

Program : DDTF main executing file
"""

from TestLocators.orange_locators import OrangeHRM_Locators
from Utilities.orange_excel_functions import OrangeExcelFunctions
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
import pytest

class Test_OrangeHRM:

    @pytest.fixture
    # Booting function for running all the Python tests
    def booting_function(self):
        firefox_options = Options()
        firefox_options.add_argument('--incognito')
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    #Method to test excel login data in the webpage
    def test_Orange_HRM(self, booting_function):
        try:
            self.driver.get(OrangeHRM_Locators().url)

            excel_file = OrangeHRM_Locators().excel_file
            sheet_number = OrangeHRM_Locators().sheet_number

            # create object for the Excel Utility Class
            orange = OrangeExcelFunctions(excel_file, sheet_number)

            # row count from the Excel file
            row = orange.row_count()

            for row in range(2, row + 1):
                username = orange.read_data(row, 6)
                password = orange.read_data(row, 7)

                username_box = self.wait.until(EC.presence_of_element_located((By.NAME,OrangeHRM_Locators().username)))
                username_box.send_keys(username)

                password_box = self.wait.until(EC.presence_of_element_located((By.NAME,OrangeHRM_Locators().password)))
                password_box.send_keys(password)

                submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,OrangeHRM_Locators().submit_button)))
                submit_button.click()

                # validate the login and generate the Test-Case results in excel sheet
                if OrangeHRM_Locators().dashboard_url == self.driver.current_url:
                    print("SUCCESS : Login with Username {a} & Password {b}".format(a=username, b=password))
                    orange.write_data(row, 8, OrangeHRM_Locators().pass_data)
                    profile_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,OrangeHRM_Locators().profile_button)))
                    profile_button.click()

                    logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,OrangeHRM_Locators().logout_button)))
                    logout_button.click()

                elif OrangeHRM_Locators().url == self.driver.current_url:
                    print("ERROR : Login unsuccessful with username {a} & Password {b}".format(a=username, b=password))
                    orange.write_data(row, 8, OrangeHRM_Locators().fail_data)
                    self.driver.refresh()


        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)

