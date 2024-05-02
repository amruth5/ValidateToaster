from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

@given('I launch Chrome browser and navigate to "{url}"')
def launch_browser(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)

@then('I validate title as "{pageTitle}"')
def verify_title(context, pageTitle):
    assert pageTitle in context.driver.title

@then('I click and navigate to "{link}" on same tab')
def click_and_navigate_sametab(context, link):
    link = context.driver.find_element(By.PARTIAL_LINK_TEXT, link)
    link.click()

@then('I click and navigate to "{link}" on new tab')
def click_and_navigate_newtab(context, link):
    link = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, link)))
    link.click()

    # Wait for the new tab to open
    WebDriverWait(context.driver, 10).until(EC.number_of_windows_to_be(2))
    # Switch control of context.driver to the new tab
    context.driver.switch_to.window(context.driver.window_handles[-1])

@then('I expect "{text}" to be present')
def expect_text_present(context, text):
    # Wait for the text to be present in the page
    visibleTest = context.driver.find_element(By.TAG_NAME, 'body').text
    assert text in visibleTest, f"The text '" + text + "' is not visible on the webpage."

@then('I click on select file and upload "{filename}" and verify file is uploaded')
def upload_and_verify(context, filename):
    element = context.driver.find_element(By.CSS_SELECTOR, '[data-test-id="upload-resume-browse-button"]')
    context.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Find the file input element
    file_input = context.driver.find_element(By.XPATH, "//input[@type='file']")

    # Upload the file (replace 'file_path' with the path to your file)
    file_path = os.getcwd() + "/" + filename 
    file_input.send_keys(file_path)
    time.sleep(3)

    context.driver.find_element(By.CSS_SELECTOR, '[data-test-id="confirm-upload-resume"]').click();
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="drop-resume-text"]')))
    
    #validate file is uploaded
    expect_text_present(context, filename)

@then('I search for "{searchString}" and select "{selectString}" from dropdown')
def search_and_select_text(context, searchString, selectString):
    context.driver.find_element(By.ID, "main-search-box").send_keys(searchString)
    time.sleep(5)
    #validate filename is visible
    expect_text_present(context, selectString)
    context.driver.find_element(By.XPATH, f"//*[contains(text(), '" + selectString + "')]").click()
    context.driver.find_element(By.XPATH, f"//*[contains(text(), 'Search')]").click();


@then('I click on job title {cardName} and verify job Id contains "{searchString}"')
def click_and_verify(context, cardName, searchString):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test-id=' + cardName + ']')))
    context.driver.find_element(By.CSS_SELECTOR, '[data-test-id=' + cardName + ']').click();
    time.sleep(5)
    expect_text_present(context, searchString)

@then('I apply for job and verify the toast message')
def apply_for_job(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test-id="apply-button"]').click()
    button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "position-apply-button")))
    context.driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    time.sleep(5)

@then('I capture screenshot of toast message')
def take_screenshot(context):
    context.driver.save_screenshot("toast_screenshot.png")
