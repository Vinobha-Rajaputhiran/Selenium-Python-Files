"""
test_rectangle_drag_and_drop.py - Pytest test-case for verifying & validating Python Selenium Automation codes
"""

from rectangle_drag_and_drop import Rectangle
import pytest

url = 'https://jqueryui.com/droppable/'
Box = Rectangle(url)

#Test case to lauch and open the webpage
def test_start_automation():
   assert Box.start_automation() == True

#Test case to drag and drop rectangular box
def test_drag_and_drop():
    assert Box.drag_and_drop() == True

#Test case to close the browser
def test_shutdown():
   assert Box.shutdown_automation() == None

