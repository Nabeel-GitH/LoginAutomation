import pytest  # importing pytest for the  test
from selenium import webdriver  # importing the webdriver for chrome
from selenium.webdriver.common.by import By  # importing the By for using it in By.
from selenium.webdriver.common.keys import Keys

# Constants
BASE_URL = "https://practicetestautomation.com/practice-test-login/"  # base url where we will be navigated
# below is the test data for testing
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"
INVALID_USERNAME = "STUDENT1"
INVALID_PASSWORD = "PASSWORD1234"


@pytest.fixture  # Fixture to set up  the WebDriver instance
def setup():
    driver = webdriver.Chrome()  # creating webdriver instance
    driver.maximize_window()  # for maximization of the window
    yield driver
    ''' divides this block in 2 parts the part above yield statement will be 
    executed first and the below part after each test funtion has finished runnning'''
    driver.quit()  # closes the all Chrome window and closes webdriver session


# Helper function for logging in
def login(driver, username, password):
    driver.get(BASE_URL)  # navigate to the base url
    username_field = driver.find_element(By.ID, "username")     # finds the element by ID
    password_field = driver.find_element(By.ID, "password")     # finds the element by ID
    submit_button = driver.find_element(By.ID, "submit")         # finds the element by ID

    username_field.send_keys(username)  # entering data in the username text field using send_keys(data)
    password_field.send_keys(password)  # entering data in the password text field using send_keys(data)
    submit_button.click()     # clicks on the submit button


# Test cases
def test_successful_login(setup):
    driver = setup  # gets the instance of the webdriver
    login(driver, VALID_USERNAME, VALID_PASSWORD)  # passing the values to the login function

    # assertions to verify successful login
    login_success = driver.find_element(By.XPATH, "//h1[contains(text(),'Logged In Successfully')]").is_displayed()
    assert login_success


def test_failed_login(setup):
    driver = setup   # gets the instance of the webdriver
    login(driver, INVALID_USERNAME, INVALID_PASSWORD)   # passing the values to the login function

    # assertions to verify failed login
    error_message = driver.find_element(By.ID, "error").is_displayed()
    assert error_message
