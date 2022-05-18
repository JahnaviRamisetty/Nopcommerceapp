import time
import pytest
from pageobjects.loginpage import Login
from pageobjects.addcustomerpage import AddCustomer
from pageobjects.searchcustomerpage import SearchCustomer
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 ****** ****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** ********** Login succesful **********")

        self.logger.info("*** **** Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("**** ********* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***** **********  TC_SearchCustomerByName_005 Finished  *********** ")


