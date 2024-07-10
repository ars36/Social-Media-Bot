from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Get the absolute path to the HTML file
html_file_path = os.path.abspath("index.html")

# Initialize the WebDriver
driver = webdriver.Chrome()

def visit_page(file_path):
    driver.get("file://" + file_path)
    time.sleep(2)  # Wait for the page to load

def click_all_follow_buttons():
    try:
        follow_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Follow')]")
        for button in follow_buttons:
            button.click()
            time.sleep(1)  # Wait for the action to complete
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Visit the local HTML page
    visit_page(html_file_path)

    # Click all follow buttons
    while True:
        click_all_follow_buttons()
        time.sleep(5)  # Wait for a while before repeating the action

    # The script will keep running until interrupted manually
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        driver.quit()
