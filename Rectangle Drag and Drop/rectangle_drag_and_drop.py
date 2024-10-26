"""
Using Python Selenium Automation and Action Chains vist the URL https://jqueryui.com/droppable/ and do a drag and drop operation of
the White Rectangular box into the Yellow Rectangular box.

"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class Rectangle:

    #Locators Data
    drag_locator = "//body//div[@id='draggable']"
    drop_locator = "//body//div[@id='droppable']"

    #Construtor for the class
    def __init__(self, url):
        self.url=url
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.action=ActionChains(self.driver)

    #Method to start the webpage automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            return True

        except Exception as _:
            print("Error: Unable to Start Python Automation")
            return False

    #Method to perform drag and drop operation
    def drag_and_drop(self):
        try:
            if self.start_automation():
                sleep(3)
                iframe_location = self.driver.find_element(by=By.TAG_NAME,value='iframe')
                self.driver.switch_to.frame(iframe_location)
                source = self.driver.find_element(by=By.XPATH, value=self.drag_locator)
                target = self.driver.find_element(by=By.XPATH, value=self.drop_locator)

                if source.is_displayed() and target.is_displayed():
                    if source.is_enabled() and target.is_enabled():
                        self.action.drag_and_drop(source, target).perform()
                        return True

            else:
                print("Error: Unable to access page")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print('Error: ', error)
            return False


    #Method to close the webpage
    def shutdown_automation(self):
        self.driver.quit()
        return None


if __name__ == '__main__':

    #Webpage URL
    url='https://jqueryui.com/droppable/'

    Box= Rectangle(url)
    Box.start_automation()
    Box.drag_and_drop()
    Box.shutdown_automation()







