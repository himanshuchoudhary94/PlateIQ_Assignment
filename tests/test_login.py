import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from TestData.LoginPageData import LoginPageData
from pageObjects.loginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):
    """This function tests whether the website opened is correct or not"""
    def test_checkCorrectWebsiteOpened(self, getLoginData):

        log = self.getlogger()
        loginPage = LoginPage(self.driver)
        try:
            loginPage.outsideModal().click()
            log.info("Inside Modal")

        except NoSuchElementException:
            log.info("NoSuchElementException")
            pass

        action = ActionChains(loginPage.returnDriver())
        action.double_click(loginPage.landingContainer()).perform()
        assert self.driver.title == getLoginData["title"], "Incorrect Website Opened"

    def test_checkLoginPopOnClickingLogin(self):
        """This function tests whether Login Pop coming after clicking Login"""

        log = self.getlogger()
        loginPage = LoginPage(self.driver)
        loginPage.loginOrCreateButton().click()
        assert loginPage.loginSignUp().is_displayed(), "Pop-up didn't occur"

    def test_correctIDCorrectPassword(self, getLoginData):
        """This function test whether correct ID and Password lets log in"""

        loginPage = LoginPage(self.driver)
        loginPage.userID().send_keys(getLoginData["correctID"])
        loginPage.continueButton().click()
        loginPage.password().send_keys(getLoginData["correctPassword"])
        loginPage.loginButton().click()
        assert loginPage.signInText().is_displayed(), "Couldn't Login with Correct ID/Password"

    def test_incorrectID(self, getLoginData):
        """This function tests whether Incorrect ID lets you Login"""
        loginPage = LoginPage(self.driver)
        self.driver.refresh()
        loginPage.loginOrCreateButton().click()
        loginPage.userID().send_keys(getLoginData["IncorrectID"])
        loginPage.continueButton().click()
        assert loginPage.signInText().is_displayed(), "Couldn't Login incorrectID"

    def test_correctIDIncorrectPassword(self, getLoginData):
        """This function tests wether Correct ID and wrong Passwords lets you login"""

        loginPage = LoginPage(self.driver)
        self.driver.refresh()
        loginPage.loginOrCreateButton().click()
        loginPage.userID().send_keys(getLoginData["correctID"])
        loginPage.continueButton().click()
        loginPage.password().send_keys(getLoginData["IncorrectPassword"])
        loginPage.loginButton().click()
        assert loginPage.incorrectSignIn().is_displayed(), "Couldn't Login incorrectID"

    @pytest.fixture(params=LoginPageData.loginPageData)
    def getLoginData(self, request):
        return request.param

