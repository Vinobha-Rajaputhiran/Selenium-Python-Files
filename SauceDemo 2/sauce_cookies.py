"""
1. Using Python Selenium Automation and the URL https://www.saucedemo.com/ display the cookie created before and after login in the console.
   After you login into the dashboard of the portal kindly lout also.

2. Verify that the cookies are being generated during the login process.

"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class Sauce:

    # Locators Data
    username_locator = 'user-name'
    password_locator = "password"
    button_locator = "//input[@id='login-button']"
    login_status=False

    #Construtor for the class
    def __init__(self, url,username,password):
        self.url=url
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    #Method to start the webpage automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True

        except Exception as _:
            print("Error: Unable to Start Python Automation")
            return False

    #Method to login into the webpage
    def webpage_login(self):
        if self.start_automation():
            global login_status
            self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
            sleep(2)
            self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=self.button_locator).click()
            if self.driver.current_url!=self.url:
                self.login_status = True
                return True
            else:
                print("Invalid Login")
                return False
        else:
            print("Error: Unable to Login to the webpage")

    #Method to fetch the cookies before login
    def before_login_cookies(self):
        if self.start_automation():
            all_cookies= self.driver.get_cookies()
            print("The total number of cookies present in the webpage before login: ", len(all_cookies))
            if len(all_cookies)==0:
                print('Cookies Status: Not Generated')
            else:
                print('Cookies Status: Generated')
                for cookie in all_cookies:
                    print(cookie)
            return True
        else:
            return False

    #Method to fetch the cookies after login
    def after_login_cookies(self):
        if self.login_status == True:
            all_cookies= self.driver.get_cookies()
            print("The total number of cookies present in the webpage after login: ", len(all_cookies))
            if len(all_cookies)==0:
                print('Cookies Status: Not Generated')
            else:
                print('Cookies Status: Generated')
                for cookie in all_cookies:
                    print(cookie)
            return True
        else:
            print("Can't fetch cookies: Invalid Login")
            return False

    #Method to fetch the cookies after logout
    def after_logout_cookies(self):
        if self.login_status == True:
            all_cookies= self.driver.get_cookies()
            print("The total number of cookies present in the webpage after logout: ", len(all_cookies))
            if len(all_cookies)==0:
                print('Cookies Status: Not Generated')
            else:
                print('Cookies Status: Generated')
                for cookie in all_cookies:
                    print(cookie)
            return True
        else:
            print("Can't fetch cookies: Invalid Login")
            return False

    #Method to add cookies to the webpage
    def add_my_cookies(self):
        if self.login_status == True:
            my_cookies= {'name': 'Chilli', 'value': 'bar', 'path': '/', 'secure': True}
            self.driver.add_cookie(my_cookies)
            return True
        else:
            print("Can't add cookies: Invalid Login")
            return False

    #Method to delete cookies from the webpage
    def delete_my_cookies(self):
        if self.login_status == True:
            self.driver.delete_cookie('Chilli')
            return True
        else:
            print("Can't delete cookies: Invalid Login")
            return False


    #Method to logout of the webpage
    def webpage_logout(self):
        if self.login_status == True:
            self.driver.find_element(by=By.ID, value='react-burger-menu-btn').click()
            sleep(2)
            self.driver.find_element(by=By.ID, value='logout_sidebar_link').click()
            sleep(2)
            return True
        else:
            print("Unable to Logout : Invalid Login")
            return False

    #Method to close the webpage
    def shutdown_automation(self):
        self.driver.quit()
        return None


if __name__ == '__main__':

    url='https://www.saucedemo.com/'

    #Valid UserData
    ketchup=Sauce(url,'standard_user','secret_sauce')
    ketchup.start_automation()
    ketchup.before_login_cookies()
    ketchup.webpage_login()
    ketchup.add_my_cookies()
    ketchup.after_login_cookies()
    ketchup.delete_my_cookies()
    ketchup.webpage_logout()
    ketchup.after_logout_cookies()
    ketchup.shutdown_automation()

    #Invalid UserData
    # mayo=Sauce(url,'locked_out_user','secret_sauce')
    # mayo.start_automation()
    # mayo.before_login_cookies()
    # mayo.webpage_login()
    # mayo.add_my_cookies()
    # mayo.after_login_cookies()
    # mayo.delete_my_cookies()
    # mayo.webpage_logout()
    # mayo.after_logout_cookies()
    # mayo.shutdown_automation()



