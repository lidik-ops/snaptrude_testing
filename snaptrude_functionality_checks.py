
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from snaptrude_page_elements import SnapTrudePageElements
from test_data import SnapTrudeTestData

snaptrude_elements = SnapTrudePageElements
test_data = SnapTrudeTestData()

class SnapTrudeFunctionality():
    def click_signup_btn(self):
        element = snaptrude_elements.signup_xpath
        signup_btn = self.driver.find_element(By.XPATH, element)
        self.driver.execute_script("arguments[0].click();",
                                   signup_btn)

    def input_search_bar(self):
        element = snaptrude_elements.fullname_xpath
        name = test_data.fullname
        self.driver.find_element(By.XPATH,
                                 element).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, element).send_keys(name)

