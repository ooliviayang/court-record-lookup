from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime
from selenium.common.exceptions import WebDriverException

def search_ccap(first, last, middle=None, dob=None):
    service = Service('./chromedriver')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://wcca.wicourts.gov")

        # click the "I agree" button
        button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='I agree']"))
        )
        driver.execute_script("arguments[0].click();", button)

        # fill out last name
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        ).send_keys(last)

        # fill out first name
        driver.find_element(By.NAME, "firstName").send_keys(first)

        # middle name (if provided)
        if middle:
            driver.find_element(By.NAME, "middleName").send_keys(middle)

        # dob (if provided)
        if dob:
            try:
                dob_field = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.NAME, "dateOfBirth"))
                )
                dob_field.send_keys(dob)
            except TimeoutException:
                print("⚠️ DOB field not found — skipping DOB input.")

        # click search button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "search"))
        ).click()

        print("✅ Search complete. Browser will remain open for inspection. Hit Enter to quit out.")
        time.sleep(2)  # small delay to ensure page loads
        # return driver so window doesn't close
        return driver

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")
        return driver

def get_valid_dob():
    while True:
        dob_input = input("Enter date of birth (MM-DD-YYYY) or leave blank: ").strip()
        if dob_input == "":
            return None
        try:
            datetime.strptime(dob_input, "%m-%d-%Y")
            return dob_input
        except ValueError:
            print("⚠️ Invalid format. Please enter DOB as MM-DD-YYYY.")

if __name__ == "__main__":
    # Prompt for full name
    first_last = input("Enter first and last name (e.g., John Smith): ").strip()
    if ' ' not in first_last:
        print("⚠️ Please enter both first and last name.")
    else:
        parts = first_last.split(' ')
        first = parts[0]
        last = parts[-1]
        middle = ' '.join(parts[1:-1]) if len(parts) > 2 else None

        # Prompt separately for DOB
        dob = get_valid_dob()

        driver = search_ccap(first, last, middle, dob)
        input()  # waits for you to press Enter
        driver.quit()