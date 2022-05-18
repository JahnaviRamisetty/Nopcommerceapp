import time
#import unittest
import pytest
from selenium import webdriver
from pageobjects.loginpage import Login
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen
from utilites import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//testdata/Logindata.xlsx"
    logger=LogGen.loggen()

   # @pytest.mark.regression

    #@pytest.mark.sanity
    #@pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******Test_002_DDT_Login*******")

        self.logger.info("****Started Login DDT Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'sheet1')
        print("number of rows in a excel ",self.rows)
        time.sleep(4)
        lst_status=[]
        for r in range(2,self.row+1):
           self.user=XLUtils.readData(self.path,'sheet',r,1)
           self.password = XLUtils.readData(self.path, 'sheet', r, 2)
           self.exp = XLUtils.readData(self.path, 'sheet', r, 3)
        self.lp.setusername(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(4)
        self.lp.click_logout()
        act_title = self.driver.title
        exp_title="Dashboard / nopCommerce administration"

        if act_title == exp_title:
            if self.exp=="pass":
             self.logger.info("****Login test passed ****")
             self.lp.click_logout();
             lst_status.append('pass')
            elif self.exp =='fail':
              self.logger.error("****Login test failed ****")
              self.lp.click_logout();
            lst_status.append('fail')

        elif act_title != exp_title:
            if self.exp=="pass":
             self.logger.info("****Login test failed ****")

             lst_status.append('fail')
            elif self.exp =='fail':
              self.logger.error("****Login test passed ****")

            lst_status.append('pass')

        if'fail' not in lst_status:
            self.logger.info("login DDT test case is pass")
            self.driver.close()
            assert True
        else:
            self.logger.info("login DDT test case is fail")
            self.driver.close()
            assert False

        self.logger.info("end of DDT")
        self.logger.info("end of Test_002_DDT_Login ")
