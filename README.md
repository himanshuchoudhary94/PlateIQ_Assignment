# PlateIQ_MMT_UIAutomation
Assignment for UI Automation on MMT website 


PlateIQ Assignment
Write an automation framework with following tests:
1. Selenium tests to automation a roundtrip booking till Review page. Include validations as
much as possible.
■ Go to https://www.makemytrip.com/
■ Go to Flights Search
■ Search for Goa-> Mumbai as source & destination
■ Departure: 2 days from today
■ Return: 3 days from today
■ Travelers: 1 Adult, 1 Child
■ Class: Economy
■ Select the 2nd Flight in both Departure & Return
■ Click on Book now
2. Selenium tests for Personal Login in https://www.makemytrip.com/.
■ Username: testplateiq@gmail.com, Password: test@123
■ Close the mobile number verification popup if occurs
■ Verify successful & failure cases.
■ Come up with as many login related tests you can think of.
Out of scope:
● Ignore Create New Account, Reset password
● Ignore Facebook & Google login & sign up.
Do let me know in case of any doubts/clarifications.


Approach:

A Page Object Model framework implemented with separte packages for Locators, ultilies, tests cases and test data.

I Automated basic functional test cases on 'flight booking' and 'login' scenario with corresponding assertions. 

For Login, few more scenarios that could be covered:
1. After Password reset, old Password should not work, new one should work fine
2. Password should be masked; it must not reveal characters 
3. Password must be stored in DB in encrypted format
4. Blank username and Blank password  should not work
5. SQL injection attacks & XSS should be verified for login

Many more such scenarios could be figured and tested. 
