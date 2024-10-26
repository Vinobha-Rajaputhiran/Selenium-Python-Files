"""
Using Page Object Model (POM), Explicit Wait, Expected Conditions and Pytest kindly to the following tasks.

    1. Go to https://www.imdb.com/search/name/
    2. Fill the data in the Input Boxes, Select Boxes and Drop Down menu on the webpage and do a search.
    3. Do not use the sleep() method for this task.

"""

from TestLocators.imdb_locators import Locators
from TestData.imdb_data import Data
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
import pytest

class Test_IMDB:

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

    # Test case to IMDB browse by actor name
    def test_search_by_artist(self, booting_function):
        try:
            self.driver.get(Data().url)
            self.driver.find_element(By.XPATH, Locators.name_tab).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().name_selector))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().name_input_box))).send_keys(Data().artist_data)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().page_topics_selector))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().topic_selector))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().results_selector))).click()
            assert self.driver.current_url == Data().artist_dashboard_url
            print("TEST CASE: SUCCESS")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error: ', error)

    # Test case to IMDB browse by movie name
    def test_search_by_titles(self, booting_function):
        try:
            self.driver.get(Data().url)
            self.driver.find_element(By.XPATH, Locators().title_tab).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().title_selector))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().title_input_box))).send_keys(Data().title_data)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().title_type_selector))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().title_type_button))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().results_selector))).click()
            assert self.driver.current_url == Data().title_dashboard_url
            print("TEST CASE: SUCCESS")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error: ', error)

