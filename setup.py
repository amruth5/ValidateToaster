from selenium.webdriver.chrome.service import Service


def before_all(context):
    # Initialize WebDriver
    context.driver_service = Service('./chromedriver') # Provide path to chromedriver executable
    context.driver_service.start()

def after_all(context):
    context.driver_service.stop()