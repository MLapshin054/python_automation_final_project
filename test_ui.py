import yaml
import time
import logging

from testpage import OperationsHelper

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]
password = testdata["password"]

class TestUI:

    def test_step01(self, browser):
        logging.info("Test 1 Starting...")
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.enter_login(name)
        testpage.enter_password(password)
        testpage.click_login_button()
        assert testpage.get_user_name() == f'Hello, {name}'
        logging.info("Test 1 completed")

