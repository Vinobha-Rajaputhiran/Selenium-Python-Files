"""
test_instagram_count.py - Pytest test-case for verifying & validating Python Selenium Automation codes
"""

from instagram_count import Instagram
import pytest

url='https://www.instagram.com/guviofficial/'
Guvi = Instagram(url)

#Test case to lauch the webpage
def test_start_automation():
   assert Guvi.start_automation() == True

#Test case to close the window button
def test_close_button():
    assert Guvi.close_button() == True

#Test case to count the number of followers
def test_followers_count():
    assert Guvi.fetch_followers_count() == True

#Test case to count the number of following
def test_following_count():
    assert Guvi.fetch_following_count() == True

#Test Case to close the browser
def test_shutdown():
   assert Guvi.shutdown_automation() == None

