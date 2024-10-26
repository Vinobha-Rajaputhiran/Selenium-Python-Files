"""
test_sauce_cookies.py
"""

from sauce_cookies import Sauce
import pytest

url = 'https://www.saucedemo.com/'

#Postive UserData
#sauce = Sauce(url, 'standard_user', 'secret_sauce')

#Negative UserData
sauce = Sauce(url,'locked_out_user', 'secret_sauce')

#Test case to lauch the webpage
def test_start_automation():
   assert sauce.start_automation() == True

#Test Case to generate cookies before login
def test_before_login_cookies():
    assert sauce.before_login_cookies() == True

#Test case for webpage login
def test_login():
   assert sauce.webpage_login() == True

#Test Case to add cookies to webpage
def test_add_my_cookies():
   assert sauce.add_my_cookies() == True

#Test Case to generate cookies after login
def test_after_login_cookies():
   assert sauce.after_login_cookies() == True

#Test Case to delete cookies from webpage
def test_delete_my_cookies():
   assert sauce.delete_my_cookies() == True

#Test case to logout
def test_logout():
   assert sauce.webpage_logout() == True

#Test Case to generate cookies after logout
def test_after_logout_cookies():
    assert sauce.after_logout_cookies()

#Test Case to close the browser
def test_shutdown():
   assert sauce.shutdown_automation() == None