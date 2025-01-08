import logging
import yaml

from BaseApp import BasePage
from selenium.webdriver.common.by import By

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class SearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
        for locator in locators["xpath"].keys():
            ids[locator] = (By.XPATH, locators["xpath"][locator])
        for locator in locators["css"].keys():
            ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=5)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def get_value_from_field(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        try:
            value = self.get_element_property(locator, testdata["find_value"])
            if value is None:
                logging.error(f"Value not found for {element_name}")
            else:
                logging.debug(f"Found value {value} for {element_name}")
            return value
        except:
            logging.exception(f"Exception while getting value for {element_name}")
            return None

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(SearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login field")

    def enter_password(self, word):
        self.enter_text_into_field(SearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password field")

    # CLICK
    def click_login_button(self):
        self.click_button(SearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    # GET
    def get_user_name(self):
        return self.get_text_from_element(SearchLocators.ids["LOCATOR_HELLO_FIELD"], description="username")

    def get_about_title(self):
        return self.get_text_from_element(SearchLocators.ids["LOCATOR_ABOUT_TITLE"], description="about title")

    def get_about_value(self):
        return self.get_value_from_field(SearchLocators.ids["LOCATOR_ABOUT_TITLE"], description="value")
