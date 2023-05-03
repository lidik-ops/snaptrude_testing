# pylint: disable=trailing-whitespace
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    #Run tests in chrome
    options.headless = False
    chrome_prefs = {}
    options.experimental_options["prefs"] = chrome_prefs
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    driver.maximize_window() 
    return driver
