# PlateIQ Task

**Abstract**

The goal of this project was to make automation framework for automation of 2 scenarios (Flight Booking and Login)

**Background**

Website Tested
1. https://www.makemytrip.com/

**Test Cases:**

All the below test cases are according to the criteria mentioned in the task.

Following are the test cases that are implemented in the automation script:

1. **Functional Automation Testing of Flight Booking Scenario** 
* Tests whether the website opened is correct or not
* Tests whether flight menu opened or not
* Tests whether selected city name is correctly displayed or not
* Tests whether selected date is correctly displayed or not
* Tests whether details like count and class selected is correct
* Tests whether passenger count and class selected is correctly visible or not
* Tests whether correct flight is selected or not
* Tests whether book button is working correctly on not

2. **Functional Automation Testing of Login Scenario**
* Tests whether the website opened is correct or not
* Tests whether Login Pop coming after clicking Login
* Test whether correct ID and Password lets log in
* Tests whether Incorrect ID lets you Login
* Tests wether Correct ID and wrong Passwords lets you login

**Environment**
* Language- Python
* Framework - Pytest
* Model - Selenium Python automation
* Report - pytest-html

**Pre requisites:** Test System should have python 3.6.2+ on it

**Steps to run automation script -**
1. Go to Automation Project https://github.com/himanshuchoudhary94/PlateIQ_MMT.git
2. Clone it
3. cd projectname/
4. pip install -r requirements.txt
3. Install all the tools mentioned in requirements.txt
4. Run file startTest.sh (sh startTest.bat)
5. HTML Report is generated in the same project in Reports Folder along with logs after running startTest.sh.

**HTML Report**

HTML report contains all the test cases with their status .You can check the sample report in the same repo.  

**Further Scope**

For Login, few more scenarios that could be covered:
1. After Password reset, old Password should not work, new one should work fine
2. Password should be masked; it must not reveal characters 
3. Password must be stored in DB in encrypted format
4. Blank username and Blank password  should not work
5. SQL injection attacks & XSS should be verified for login


**HTML Report**

HTML report contains all the test cases with their status .You can check the sample report in the same repo.  
