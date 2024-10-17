from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up Selenium WebDriver (using Chrome in this example)
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
driver.maximize_window()

# Navigate to the CoWIN website
driver.get("https://www.cowin.gov.in/")

# Click on the "FAQ" link to open in a new window
faq_link = driver.find_element(By.LINK_TEXT, "FAQ").click()
ActionChains(driver).key_down(Keys.CONTROL).click(faq_link).key_up(Keys.CONTROL).perform()
print("Opened_Window: FAQ")
time.sleep(5)  

# in a new window click on the "Partners" link to open 
partners_link = driver.find_element(By.LINK_TEXT, 'PARTNERS').click()
ActionChains(driver).key_down(Keys.CONTROL).click(partners_link).key_up(Keys.CONTROL).perform()
print("Opened_Window: Partners")
time.sleep(5)  

# Fetch the opened window handles
window_ids = driver.window_handles
print("Opened Windows/Frames IDs:", window_ids)

# Close the new windows (skip the original window)
for window_id in window_ids[1:]:  # Skip the first window (home page)
    driver.switch_to.window(window_id)
    driver.close()
    print("Closed window:", window_id)

# Switch back to the original window (Home page)
driver.switch_to.window(window_ids[0])
print("Switched back to Home Page")

# Optional: Wait for a while before closing the original window
time.sleep(5)  # You can adjust this as needed

# Close the original browser window
driver.quit()
