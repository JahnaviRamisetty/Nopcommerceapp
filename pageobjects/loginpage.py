import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login:
    usernametxt = "//*[@id='Email']"
    textbox_password_id="Password"
    button_next_XPATH="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    logout = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.XPATH, self.usernametxt).clear()
        self.driver.find_element(By.XPATH,self.usernametxt).send_keys(username)
    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_next_XPATH).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout).click()


