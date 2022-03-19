# pylint: disable=missing-class-docstring
import time
from read_properties import ReadConfig
from snaptrude_functionality_checks import SnapTrudeFunctionality

base_url = ReadConfig.get_application_url()
class TestSnaptrudechecks:

    def test_successful_snaptrude_functionality(self, setup):
        """This method performs successful redirect to snaptrude"""
        self.driver = setup

        #Get the base url
        self.driver.get(base_url)
        
        time.sleep(3)
        #Instantiate class
        snaptrude = SnapTrudeFunctionality(self.driver)
        snaptrude.click_signup_btn()
        self.driver.close()
