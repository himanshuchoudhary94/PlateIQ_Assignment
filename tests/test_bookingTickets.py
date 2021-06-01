import time
import datetime
import pytest
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestBooking(BaseClass):

    def test_correctWebsiteOpened(self):
        """This function tests whether the website opened is correct or not"""

        log = self.getlogger()
        homePage = HomePage(self.driver)
        try:
            homePage.outsideModal().click()
            log.info("Inside Modal")

        except NoSuchElementException:
            log.info("NoSuchElementException")
            pass

        action = ActionChains(homePage.returnDriver())
        action.double_click(homePage.landingContainer()).perform()
        title = "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
        assert self.driver.title == title, "Incorrect Website Opened"

    def test_clickFlightMenu(self, getBookingData):
        """This function tests whether flight menu opened or not"""

        homePage = HomePage(self.driver)
        homePage.flightMenu().click()
        FlightUrl = self.driver.current_url
        assert "flight" in FlightUrl, "Incorrect URL Opened"

    def test_checkSourceDestination(self, getBookingData):
        """This function checks whether selected city name is correctly displayed or not"""
        log = self.getlogger()
        homePage = HomePage(self.driver)
        homePage.clickFromCity().click()
        homePage.fromCity().send_keys(getBookingData['fromCity'])
        time.sleep(1)
        options = homePage.textSuggested()
        for option in options:
            if getBookingData['fromCity'] in option.text:
                log.info(option.text)
                option.click()
                break

        FromCitySelected = homePage.clickFromCity().get_attribute("value")
        assert FromCitySelected == getBookingData['fromCity'], "Incorrect City Name Reflecting"
        homePage.toCity().send_keys(getBookingData['toCity'])
        time.sleep(1)
        options = homePage.textSuggested()
        for option in options:
            if getBookingData['toCity'] in option.text:
                log.info(option.text)
                option.click()
                break

        ToCitySelected = homePage.clickToCity().get_attribute("value")
        assert ToCitySelected == getBookingData['toCity'], "Incorrect City Name Reflecting"

    def test_checkDateSelected(self, getBookingData):
        """This function checks whether selected date is correctly displayed or not"""

        log = self.getlogger()
        homePage = HomePage(self.driver)
        time.sleep(1)
        depDate = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%b %d %Y")
        dep_dates = homePage.grabDates()
        log.info(depDate)

        for date in dep_dates:
            if depDate in date.get_attribute("aria-label"):
                date.click()
                break

        time.sleep(1)

        homePage.returnDateSelector().click()
        arvDate = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%b %d %Y")
        arv_dates = homePage.grabDates()
        log.info(arvDate)

        for date in arv_dates:
            if arvDate in date.get_attribute("aria-label"):
                date.click()
                break

        time.sleep(1)

        DepDateSelected = homePage.departureDateSelector().get_attribute("value")
        CheckDepDateSelected = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%d %b %Y")
        assert DepDateSelected.split(", ")[1] in CheckDepDateSelected, "Incorrect Date Selected"

        ReturnDateSelected = homePage.returnDate().get_attribute("value")
        CheckReturnDateSelected = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%d %b %Y")
        assert ReturnDateSelected.split(", ")[1] in CheckReturnDateSelected, "Incorrect Date Selected"

    def test_checkTravellerInfo(self, getBookingData):
        """This function checks whether details like count of adult, children, infants is correct or not.
        It also checks the class selection is correct or not"""

        log = self.getlogger()
        homePage = HomePage(self.driver)
        homePage.chooseTravellers().click()
        adults = homePage.noOfAdults()
        bookAdults = "adults-" + getBookingData['adults']
        print(bookAdults)
        for adultCount in adults:
            if bookAdults == adultCount.get_attribute("data-cy"):
                adultCount.click()
                assert adultCount.get_attribute("class") == 'selected', "Incorrect Adult Count Selected"
                break

        children = homePage.noOfChild()
        bookChild = "children-" + getBookingData['children']
        log.info(bookChild)
        for childCount in children:
            if bookChild == childCount.get_attribute("data-cy"):
                childCount.click()
                assert childCount.get_attribute("class") == 'selected', "Incorrect Children Count Selected"
                break

        categoryList = homePage.selectClass()

        for category in categoryList:
            if getBookingData['class'] == category.text:
                category.click()
                assert category.get_attribute("class") == 'selected', "Incorrect Category Selected"
                break

    def test_checkAppliedSettings(self, getBookingData):
        """This function tests whether passenger count and class selected is correctly visible or not"""

        log = self.getlogger()
        homePage = HomePage(self.driver)
        homePage.travellersApplyButton().click()
        totalTravellers = int(getBookingData['children']) + int(getBookingData['adults']) + int(getBookingData['infants'])
        log.info(totalTravellers)
        log.info(homePage.travellerNumber().text)
        assert int(homePage.travellerNumber().text) == totalTravellers, "Incorrect total Count reflected"
        assert homePage.categorySelected().text == "Economy/Premium Economy", "Incorrect Category Selected"

    def test_checkSelectedFlights(self, getBookingData):
        """This function checks correct flight is selected or not"""

        homePage = HomePage(self.driver)
        homePage.seachButton().click()
        self.explicit_wait(HomePage.FromBooking)
        homePage.returnDriver().execute_script("window.scrollTo(0, 150)")
        homePage.fromBooking()[getBookingData['fromFlightPositionSelect']].click()
        self.explicit_wait(HomePage.ToBooking)
        time.sleep(2)
        assert "checked" in homePage.fromBooking()[getBookingData['fromFlightPositionSelect']].get_attribute(
            "class"), "Incorrect Flight Selected"
        homePage.toBooking()[getBookingData['toFlightPositionSelect']].click()
        self.explicit_wait(HomePage.ToBooking)
        time.sleep(2)
        assert "checked" in homePage.toBooking()[getBookingData['toFlightPositionSelect']].get_attribute(
            "class"), "Incorrect Flight Selected"

    def test_checkBookButton(self):
        """This function tests whether book button is working correctly on not"""

        homePage = HomePage(self.driver)
        self.explicit_wait(HomePage.FromBooking)
        homePage.bookButton().click()
        self.explicit_wait(HomePage.ContinueButton)
        assert homePage.continueButton().is_displayed(), "Book Button didn't work correctly"

    @pytest.fixture(params=HomePageData.homePageData)
    def getBookingData(self, request):
        return request.param
