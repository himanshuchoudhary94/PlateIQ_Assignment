from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from pageObjects.loginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):
    def test_checkCorrectWebsiteOpened(self):

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
        title = "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
        assert self.driver.title == title, "Incorrect Website Opened"

    def test_checkLoginPopOnClickingLogin(self):
        log = self.getlogger()
        loginPage = LoginPage(self.driver)
        loginPage.loginOrCreateButton().click()
        assert loginPage.loginSignUp().is_displayed(), "Pop-up didn't occur"

    def test_correctIDCorrectPassword(self):
        loginPage = LoginPage(self.driver)
        loginPage.userID().send_keys("testplateiq@gmail.com")
        loginPage.continueButton().click()
        loginPage.password().send_keys("test@123")
        loginPage.loginButton().click()
        assert loginPage.signInText().is_displayed(), "Couldn't Login with Correct ID/Password"

    def test_incorrectID(self):
        loginPage = LoginPage(self.driver)
        self.driver.refresh()
        loginPage.loginOrCreateButton().click()
        loginPage.userID().send_keys("tskvfjn@gmail.com")
        loginPage.continueButton().click()
        assert loginPage.signInText().is_displayed(), "Couldn't Login incorrectID"

    def test_correctIDIncorrectPassword(self):
        loginPage = LoginPage(self.driver)
        self.driver.refresh()
        loginPage.loginOrCreateButton().click()
        loginPage.userID().send_keys("testplateiq@gmail.com")
        loginPage.continueButton().click()
        loginPage.password().send_keys("test@123123")
        loginPage.loginButton().click()
        assert loginPage.incorrectSignIn().is_displayed(), "Couldn't Login incorrectID"

