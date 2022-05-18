import pytest
from selenium import webdriver
from pageobjects.loginpage import Login
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert False
'''import time

from selenium.webdriver.common.by import By

from utilites import XLutilites
from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\edgedriver_win64\msedgedriver.exe")
time.sleep(5)
driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()



path="C:\Jahnavi\login.xlsx"

rows=XLutilites.getRowCount(path,'Sheet1')

for r in range(2,rows+1): #starts from 2 row
    #extract data from each column
    username=XLutilites.readData(path,'Sheet1',r,1)
    password=XLutilites.readData(path,'Sheet1',r,2)
    time.sleep(3)
    driver.find_element(By.XPATH, value="//span[@class='ico-caret sprite-image']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//a[@class='ico-login']").click()
    driver.find_element(by=By.NAME, value="Username").clear()

    driver.find_element(by=By.NAME, value="Username").send_keys(username)
    driver.find_element(by=By.NAME, value="Password").clear()
    driver.find_element(by=By.NAME, value="Password").send_keys(password)

    driver.find_element(by=By.XPATH, value="//input[@class='btn blue-button' and @type='submit']").click()

    if driver.title== "Free and open-source eCommerce platform. ASP.NET based shopping cart. - nopCommerce" :
        print("test is passed")
        XLutilites.writeData(path,'Sheet1',r,3,"test passed")
        driver.find_element(by=By.XPATH, value="//span[@class='ico-caret sprite-image']").click()
        driver.find_element(by=By.XPATH, value="//a[@class='ico-logout']").click()
    else:
        print("test failed")
        XLutilites.writeData(path,'Sheet1',r,3,"test failed")
    time.sleep(3)
    #driver.find_element(by=By.XPATH, value="//a[@class='desktop-logo']").click()
    driver.refresh()




driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import selenium.common.exceptions
from selenium.webdriver.support import expected_conditions as EC
import traceback
    
class NoSuchElementException:
    pass


def test_sample():
    driver = webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
    driver.get("https://qavbox.github.io/demo/signup/")
    #el = driver.find_element_by_id("lblname")
    #assert "Full Name" in el.text
    try:
        name = driver.find_element(By.ID,"username1")
        name.send_keys("aaaa")
        assert "aaa" in name.text
    except NoSuchElementException:
        print(traceback.format_exc())

    mail = driver.find_element(By.ID,"email")
    mail.send_keys("qavbox@gmail.com")
    time.sleep(10)
    driver.close()'''
