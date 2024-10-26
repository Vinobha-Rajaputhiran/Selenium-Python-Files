"""
imdb_locators.py
"""

class Locators:

    name_tab = "//li[2]//span[text()='NAMES']"
    name_selector = "//label//span[1]//div[text()='Name']"
    name_input_box = "//div//input[@name='name-text-input']"
    page_topics_selector = "//label//span[1]//div[text()='Page topics']"
    topic_selector = "//div[@class='sc-c8a95ade-1 fpeCwy']//section//button[2]"
    title_tab = "//ul//li[1]//span[text()='TITLES']"
    title_selector = "//label//span[1]//div[text()='Title name']"
    title_input_box = "//div//input[@name='title-name-input']"
    title_type_selector = "//label//span[1]//div[text()='Title type']"
    title_type_button = "//div[@id='accordion-item-titleTypeAccordion']//div//section//button[1]"
    results_selector = "//span[text()='See results']"