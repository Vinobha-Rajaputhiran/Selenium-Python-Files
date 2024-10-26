"""
Using Python Selenium, Explicit Wait, Expected Conditions and Chrome Webdriver kindly to the following tasks.

    1. Go to https://www.imdb.com/search/name/
    2. Fill the data in the Input Boxes, Select Boxes and Drop Down menu on the webpage and do a search.
    3. Do not use the sleep() method for this task.

"""

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


class IMDB:
    firefox_options = Options()
    firefox_options.add_argument('--incognito')
    driver = webdriver.Chrome(service=Service(GeckoDriverManager().install()), options=firefox_options)
    wait = WebDriverWait(driver, 10)

    def __init__(self,url):
        self.url=url

    #Method to start the webpage automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True

        except [NoSuchWindowException, WebDriverException] as _:
            print("Error: Unable to Start Python Automation")
            return False

    #Method to search by the artist name
    def search_by_artist(self):
        try:
            self.driver.find_element(By.XPATH, "//li[2]//span[text()='NAMES']").click()
            name_selector=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label//span[1]//div[text()='Name']")))
            name_input_box= self.wait.until(EC.presence_of_element_located((By.XPATH,"//div//input[@name='name-text-input']")))
            page_topics_selector = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label//span[1]//div[text()='Page topics']")))
            topic_selector = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='sc-c8a95ade-1 fpeCwy']//section//button[2]")))
            results_selector= self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='See results']")))

            name_selector.click()
            name_input_box.send_keys('Ryan Reynolds')
            page_topics_selector.click()
            topic_selector.click()
            results_selector.click()
            return True

        except [NoSuchElementException,TimeoutException,ElementClickInterceptedException,ElementNotVisibleException] as error:
            print('Error: ', error)
            return False

    ##Method to search by the movie name
    def search_by_titles(self):
        try:
            self.driver.find_element(By.XPATH, "//ul//li[1]//span[text()='TITLES']").click()
            title_selector= self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label//span[1]//div[text()='Title name']")))
            title_input_box= self.wait.until(EC.presence_of_element_located((By.XPATH,"//div//input[@name='title-name-input']")))
            title_type_selector= self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label//span[1]//div[text()='Title type']")))
            title_type_button= self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='accordion-item-titleTypeAccordion']//div//section//button[1]")))
            results_selector = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='See results']")))

            title_selector.click()
            title_input_box.send_keys('Deadpool')
            title_type_selector.click()
            title_type_button.click()
            results_selector.click()
            return True


        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException] as error:
            print('Error: ', error)
            return False

    #Method to close the webpage
    def shutdown_automation(self):
        self.driver.quit()
        return None

if __name__ == '__main__':
    #WebPage URL
    url='https://www.imdb.com/search/name/'

    deadpool=IMDB(url)
    deadpool.start_automation()
    deadpool.search_by_artist()
    deadpool.search_by_titles()
    deadpool.shutdown_automation()
