from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    LandingContainer = (By.CSS_SELECTOR,".landingContainer")
    OutsideModal = (By.CSS_SELECTOR, "div[data-cy = 'outsideModal']")
    LeftPersonalAccount = (By.CSS_SELECTOR, ".leftPersonalAccount")
    FlightMenu = (By.CSS_SELECTOR, ".menu_Flights")
    ClickFromCity = (By.CSS_SELECTOR, "#fromCity")
    ClickToCity = (By.CSS_SELECTOR, "#toCity")
    FromCity = (By.CSS_SELECTOR, "[placeholder='From']")
    ToCity = (By.CSS_SELECTOR, "[placeholder='To']")
    TextSuggested = (By.CSS_SELECTOR, ".calc60 p[class*='blackText']")
    DepartureDateSelector = (By.CSS_SELECTOR, "#departure")
    # DepartureDate = (By.CSS_SELECTOR, "[data-cy='departureDate']")
    ReturnDate = (By.CSS_SELECTOR, "#return")
    ReturnDateSelector = (By.CSS_SELECTOR, ".reDates")
    GrabDates = (By.CSS_SELECTOR, "[aria-disabled='false']") #aria-label="Sat May 29 2021"  DayPicker-Day
    Travellers = (By.CSS_SELECTOR, "[for = 'travellers']")
    NoOfAdults = (By.XPATH, "//div[@class='appendBottom20']/ul[1]/li")
    NoOfChild = (By.XPATH, "//div[@class='appendBottom20']/div/div[1]/ul/li")
    SelectClass = (By.XPATH, "//ul[contains(@class, 'classSelect')]/li")
    TravellersApplyButton = (By.CSS_SELECTOR, "[data-cy='travellerApplyBtn']")
    SeachButton = (By.CSS_SELECTOR, ".primaryBtn")
    FromBooking = (By.XPATH, "//div[@class='splitVw']/div[1]/div[2]/div/label")  #/div/div[2]/div[2]
    ToBooking = (By.XPATH, "//div[@class='splitVw']/div[2]/div[2]/div/label")
    BookButton = (By.CSS_SELECTOR, "[id*='bookbutton']")
    ContinueButton = (By.XPATH, "//button[text()='Continue']")
    TravellerNumber = (By.XPATH,"//span[@data-cy='travellerText']/span")
    CategorySelected = (By.XPATH,"//label[@for='travellers']/p[2]")



    def returnDriver(self):
        return self.driver

    def landingContainer(self):
        return self.driver.find_element(*HomePage.LandingContainer)

    def homeFlex(self):
        return self.driver.find_element(*HomePage.HomeFlex)

    def leftPersonalAccount(self):
        return self.driver.find_element(*HomePage.LeftPersonalAccount)

    def flightMenu(self):
        return self.driver.find_element(*HomePage.FlightMenu)

    def fromCity(self):
        return self.driver.find_element(*HomePage.FromCity)

    def toCity(self):
        return self.driver.find_element(*HomePage.ToCity)

    def textSuggested(self):
        return self.driver.find_elements(*HomePage.TextSuggested)

    def outsideModal(self):
        return self.driver.find_element(*HomePage.OutsideModal)

    def clickFromCity(self):
        return self.driver.find_element(*HomePage.ClickFromCity)

    def clickToCity(self):
        return self.driver.find_element(*HomePage.ClickToCity)

    def grabDates(self):
        return self.driver.find_elements(*HomePage.GrabDates)

    def departureDateSelector(self):
        return self.driver.find_element(*HomePage.DepartureDateSelector)

    def returnDateSelector(self):
        return self.driver.find_element(*HomePage.ReturnDateSelector)

    def chooseTravellers(self):
        return self.driver.find_element(*HomePage.Travellers)

    def noOfAdults(self):
        return self.driver.find_elements(*HomePage.NoOfAdults)

    def noOfChild(self):
        return self.driver.find_elements(*HomePage.NoOfChild)

    def selectClass(self):
        return self.driver.find_elements(*HomePage.SelectClass)

    def travellersApplyButton(self):
        return self.driver.find_element(*HomePage.TravellersApplyButton)

    def seachButton(self):
        return self.driver.find_element(*HomePage.SeachButton)

    def fromBooking(self):
        return self.driver.find_elements(*HomePage.FromBooking)

    def toBooking(self):
        return self.driver.find_elements(*HomePage.ToBooking)

    def bookButton(self):
        return self.driver.find_element(*HomePage.BookButton)

    def continueButton(self):
        return self.driver.find_element(*HomePage.ContinueButton)

    def departureDate(self):
        return self.driver.find_element(*HomePage.DepartureDate)

    def returnDate(self):
        return self.driver.find_element(*HomePage.ReturnDate)

    def travellerNumber(self):
        return self.driver.find_element(*HomePage.TravellerNumber)

    def categorySelected(self):
        return self.driver.find_element(*HomePage.CategorySelected)
