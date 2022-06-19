from selenium import webdriver
import unittest
class LewisTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/ilu/Downloads/chromedriver")
        cls.driver.get("https://www.lewisu.edu/index.htm")
    def test_Check_title(self):
        self.driver.title
    def test_check_span(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'About Us')]")
        self.driver.find_element_by_xpath("//span[contains(text(),'Academics')]")
        self.driver.find_element_by_xpath("//span[contains(text(),'Admission & Aid')]")
        self.driver.find_element_by_xpath("//span[contains(text(),'Athletics')]")
        self.driver.find_element_by_xpath("//span[contains(text(),'Student Life')]")
        self.driver.find_element_by_xpath("//span[contains(text(),'Locations')]")
    def test_searchOmari(self):
        self.driver.get("https://www.lewisu.edu/portals/facultystaffportal.htm")
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[3]/a/i').click()
        self.driver.find_element_by_xpath('//*[@id="MobsearchInput"]').send_keys("Omari")
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[3]/a/i').click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Testing complete")