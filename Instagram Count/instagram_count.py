"""
Using Python Selenium Automation and the URL https://www.instagram.com/guviofficial/ kindly do the following tasks.

    1. Use either Relative or Absolute XPATH only for this task.
    2. Extract the total number of followers and following from the URL mentioned above.

"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class Instagram:

    # Locators Data - using Relative XPATH
    followers_locator = "//li//div//button//span[@class='_ac2a']//span[text()='165K']"
    following_locator = "//li//div//button//span[@class='_ac2a']//span[text()='6']"
    button_locator = "//div//div//button[@class='_abn5 _abn6 _aa5h']"

    #Construtor for the class
    def __init__(self, url):
        self.url=url
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    #Method to start the webpage automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            return True

        except Exception as _:
            print("Error: Unable to Start Python Automation")
            return False

    #Method to fetch the total number of following
    def fetch_following_count(self):
        try:
            sleep(2)
            following = self.driver.find_element(by=By.XPATH, value=self.following_locator)
            print("The Total Number of Instagram following are: ", following.text)
            return True

        except Exception as error:
            print('Error: ', error)
            return False

    #Method to fetch the total number of followers
    def fetch_followers_count(self):
        try:
            sleep(2)
            followers = self.driver.find_element(by=By.XPATH, value=self.followers_locator)
            print("The Total Number of Instagram followers are: ", followers.text)
            return True

        except Exception as error:
            print('Error: ', error)
            return False

    #Method to close the button on instagram window
    def close_button(self):
        try:
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=self.button_locator).click()
            return True

        except Exception as error:
            print("Error: ",error)
            return False


    #Method to close the webpage
    def shutdown_automation(self):
        self.driver.quit()
        return None


if __name__ == '__main__':

    #Webpage URL
    url='https://www.instagram.com/guviofficial/'

    Guvi = Instagram(url)
    Guvi.start_automation()
    Guvi.close_button()
    Guvi.fetch_following_count()
    Guvi.fetch_followers_count()
    Guvi.shutdown_automation()





