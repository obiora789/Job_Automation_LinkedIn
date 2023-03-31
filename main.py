import os
import random
import time
import dotenv
# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

new_file = dotenv.find_dotenv()
dotenv.load_dotenv(new_file)
# LINKEDIN_URL = os.environ.get("LINKEDIN_ASIA_URL")
LINKEDIN_URL = os.environ.get("LINKEDIN_EUROPE_URL")
CHROME_DRIVER = os.environ.get("CHROME_PATH")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.getenv("PASSWORD")
MOBILE_NUMBER = os.environ.get("MOBILE")
ORIGIN = 0
EXPERIENCE_LEVEL = 1
LONG = 2
SHORT = 3
DELAY = 5
BUFFER = 100
SERVICE = Service(executable_path=CHROME_DRIVER)
able_to_proceed = True


def knowledge(experience_labels):
    """Checks the labels and determines whether to proceed with the application or not"""
    global able_to_proceed
    able_to_proceed = True
    print(f"Length of labels: {len(experience_labels)}")
    for num in range(len(experience_labels)):
        if "experience" in experience_labels[num].text: # checking whether the labels contain the word "experience"
            input_experience = driver.find_elements(By.CLASS_NAME, "artdeco-text-input--input")
            if input_experience[num].get_attribute("value") != EXPERIENCE_LEVEL:    # your work experience goes here
                input_experience[num].click()
                input_experience[num].clear()
                input_experience[num].send_keys(f"{EXPERIENCE_LEVEL}")
            time.sleep(DELAY - generate_random_time(SHORT))
        else:
            able_to_proceed = False
            break
    return able_to_proceed


def close_application():
    """This function closes the particular application so that the next job process can start"""
    close_button = driver.find_element(By.CSS_SELECTOR, ".mercado-match path")
    close_button.click()
    time.sleep(DELAY - generate_random_time(LONG))
    discard_application = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--secondary span")
    discard_application.click()


def submit_application():
    """Submit the application"""
    time.sleep(DELAY - generate_random_time(SHORT))
    check_box = driver.find_element(By.CLASS_NAME, "ember-checkbox")
    if check_box.get_attribute("checked"):  # to determine if the checkbox is checked or not
        driver.execute_script("arguments[0].click();", check_box)
    submit_app = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
    driver.execute_script("arguments[0].click()", submit_app) # Submits the application
    time.sleep(DELAY)
    close_ = driver.find_element(By.CSS_SELECTOR, ".mercado-match") # Closes the alert that confirms submission
    WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable(close_)).click()
    time.sleep(DELAY - generate_random_time(SHORT))


def generate_random_time(number_of_secs):
    """Generates a random time between 1 and 5 seconds once it receives the number of seconds"""
    return round(random.randint(6, 9)/10, 1) * number_of_secs


def select_cv():
    """Selects the Resumé to be attached to the application"""
    choose_cv = driver.find_element(By.CSS_SELECTOR,
                                    ".jobs-resume-picker__resume-btn-container .artdeco-button--tertiary")
    driver.execute_script("arguments[0].click()", choose_cv)
    time.sleep(DELAY - generate_random_time(SHORT))


options = webdriver.ChromeOptions()
#options.add_argument("window-size=1200x600")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
with webdriver.Chrome(service=SERVICE, options=options) as driver:
    driver.get(url=LINKEDIN_URL)
    time.sleep(DELAY)
    sign_in = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
    driver.execute_script("arguments[0].click()", sign_in)  # Clicks the sign-in button
    time.sleep(DELAY)
    driver.find_element(By.NAME, "session_key").send_keys(EMAIL)    # Inputs the email
    time.sleep(DELAY - generate_random_time(LONG))
    driver.find_element(By.NAME, "session_password").send_keys(PASSWORD)    # Inputs the password
    time.sleep(DELAY - generate_random_time(LONG))
    submit = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    driver.execute_script("arguments[0].click()", submit) # clicks the sign-in button
    time.sleep(DELAY * 2 - generate_random_time(LONG))
    jobs_to_apply = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")   # gets the list of jobs
    print(len(jobs_to_apply))
    count = 0
    for job in jobs_to_apply:
        # to find the clickable portion of each job element in the list
        new_job = job.find_element(By.CLASS_NAME, "artdeco-entity-lockup__title")
        actions = ActionChains(driver)
        actions.move_to_element(job).perform()  # scrolls to the job in view and rests the mouse pointer on it
        driver.execute_script("arguments[0].click()", new_job)  # clicks the new job
        count += 1
        if count > 2:   # Begins to scroll after this point
            scroll_from = ScrollOrigin.from_element(job)
            actions.scroll_from_origin(scroll_from, ORIGIN, BUFFER).perform()   # Scroll action
        time.sleep(DELAY - generate_random_time(LONG))
        try:
            easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button span")
            # Waits until Easy apply button is clickable
            WebDriverWait(driver, DELAY*2).until(EC.element_to_be_clickable(easy_apply))
            driver.execute_script("arguments[0].click()", easy_apply)   # clicks easy apply
            time.sleep(DELAY)
        except NoSuchElementException or ElementClickInterceptedException or ElementNotInteractableException:
            continue
        else:
            time.sleep(DELAY - generate_random_time(LONG))
            try:
                options = driver.find_elements(By.TAG_NAME, 'select')   # to access list of country codes
                num_options = len(options)
                for index in range(num_options):
                    if index == 1:
                        dropdown = Select(options[1])
                        dropdown.select_by_visible_text("United States (+1)")   # selects United States country code
                driver.implicitly_wait(DELAY - generate_random_time(SHORT))
                mobile_phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
                if mobile_phone.get_attribute("value") != MOBILE_NUMBER:    # confirms the mobile number to be entered
                    mobile_phone.send_keys(MOBILE_NUMBER)   # if true, it sends the phone number
                next_step = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
            except NoSuchElementException:
                close_application()
                continue
            if "Submit" in next_step.text:  # checks for the submit button
                select_cv()
                submit_application()
            else:
                driver.execute_script("arguments[0].click()", next_step)    # clicks next button
                time.sleep(DELAY - generate_random_time(SHORT)) # short delay
                select_cv()
                next_one = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                driver.execute_script("arguments[0].click()", next_one)
                time.sleep(DELAY - generate_random_time(SHORT))
                labels = driver.find_elements(By.CSS_SELECTOR,  # gets the input labels and returns them as a list
                                              '.artdeco-text-input--container .artdeco-text-input--label')
                try:
                    radios = driver.find_element(By.CLASS_NAME, "t-14")
                except NoSuchElementException:
                    pass
                review = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
            if review.text != "Review":     # tests for the other buttons except the review button
                try:
                    knowledge(labels)
                    pry_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                    if pry_button.text == "Next":   # close the application in case of further ambiguity
                        able_to_proceed = False     # code can be advanced to check for labels when Next is clicked
                except NoSuchElementException:  # exception clause
                    able_to_proceed = False
                    break
                if able_to_proceed:     # closes the app once False is returned
                    driver.implicitly_wait(DELAY * 2)
                    submit_application()    # Submits the application once True is returned
                else:
                    close_application()
            elif review.text == "Review" and radios.text == "Yes":  # closes the app once radio buttons are detected
                close_application()
            else:
                knowledge(labels)
                if not able_to_proceed:     # closes the app once False is returned
                    close_application()
                else:       # otherwise the application is submitted
                    review = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                    driver.execute_script("arguments[0].click()", review)
                    submit_application()
            time.sleep(DELAY - generate_random_time(LONG))
    print("Done.")
