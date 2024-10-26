"""
test_imdb_search.py
"""
from imdb_search import IMDB
import pytest

#WebPage URL under test
url='https://www.imdb.com/search/name/'
deadpool = IMDB(url)

#Test case to lauch the webpage
def test_start_automation():
   assert deadpool.start_automation() == True

#Test case to IMDB browse by actor name
def test_search_by_artist():
    assert deadpool.search_by_artist() == True

#Test case to IMDB browse by movie name
def test_search_by_titles():
    assert deadpool.search_by_titles() == True

#Test Case to close the browser
def test_shutdown():
   assert deadpool.shutdown_automation() == None