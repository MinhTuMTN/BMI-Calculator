from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to a URL
driver.get("https://www.google.com")

# Get page title
print(driver.title)

# Close browser
driver.quit()