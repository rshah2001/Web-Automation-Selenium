from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # Define Chrome options to disable search engine choice screen
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Set up download path to current working directory
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        # Initialize the Chrome service with absolute path to chromedriver
        service = Service("/Users/rishilshah/Desktop/UDEMY/Web_automation Tool(GUI) with Selenium/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load the login page
        self.driver.get('https://demoqa.com/login')

        # Wait for username and password fields to be visible
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Enter credentials and log in
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, perm_address):
        # Locate and click the elements dropdown and the Text Box
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()

        # Select the Text Box form option
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="item-0"]')))
        text_box.click()

        # Locate form fields by ID and find the submit button
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        curr_add = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        perm_add = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in form fields and submit
        full_name_field.send_keys(fullname)
        email_field.send_keys(email)
        curr_add.send_keys(current_address)
        perm_add.send_keys(perm_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Navigate to the upload and download section
        upload_download = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-7"]')))
        upload_download.click()

        # Wait for download button to be clickable and click to download
        download_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'downloadButton')))
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    # Instantiate the automation class and perform actions
    webautomation = WebAutomation()
    webautomation.login('rs1211', 'Asdfghjkl@13123')
    webautomation.fill_form('Rishil Shah', 'rishil13123@gmail.com', '3618 jefferson commons dr, 102, Tampa, Fl, 33613',
                            'D-2405 Omkar Alta Monte, Mumbai, Maharashtra, India')
    webautomation.download()
    webautomation.close()
