from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    LandingContainer = (By.CSS_SELECTOR,".landingContainer")
    OutsideModal = (By.CSS_SELECTOR, "div[data-cy = 'outsideModal']")
    LoginOrCreateButton = (By.CSS_SELECTOR, ".lhUser")
    UserID = (By.CSS_SELECTOR, "#username")
    ContinueButton = (By.CSS_SELECTOR, "[data-cy = 'continueBtn']")
    Password = (By.CSS_SELECTOR, "#password")
    LoginButton = (By.CSS_SELECTOR, "[data-cy = 'login']")
    LoginSignUpText = (By.XPATH, "//span[text()='Login/Signup']")
    SignInText = (By.XPATH, "//*[text()='OTP has been sent to EMAIL']")
    IncorrectSignInText = (By.XPATH, "//span[text()= 'Either Username or Password is incorrect.']")
    #



    def returnDriver(self):
        return self.driver

    def loginOrCreateButton(self):
        return self.driver.find_element(*LoginPage.LoginOrCreateButton)

    def userID(self):
        return self.driver.find_element(*LoginPage.UserID)

    def continueButton(self):
        return self.driver.find_element(*LoginPage.ContinueButton)

    def password(self):
        return self.driver.find_element(*LoginPage.Password)

    def loginButton(self):
        return self.driver.find_element(*LoginPage.LoginButton)

    def landingContainer(self):
        return self.driver.find_element(*LoginPage.LandingContainer)

    def outsideModal(self):
        return self.driver.find_element(*LoginPage.OutsideModal)

    def loginSignUp(self):
        return self.driver.find_element(*LoginPage.LoginSignUpText)

    def signInText(self):
        return self.driver.find_element(*LoginPage.SignInText)

    def incorrectSignIn(self):
        return self.driver.find_element(*LoginPage.IncorrectSignInText)





