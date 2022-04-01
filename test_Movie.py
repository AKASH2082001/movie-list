from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def setUp():
    global Movie_name,Year_of_Release,Director_Name,Distributor,Producer,driver
    Movie_name = input("Enter the Movie name: ")
    Year_of_Release = input("Enter the year of Release: ")
    Director_Name = input("Enter the Director name: ")
    Distributor = input("Enter the distributor: ")
    Producer = input("Enter the Producer name: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    yield
    time.sleep(5)
    driver.close()

def test_movies(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(2)
    driver.find_element_by_name("mname").send_keys(Movie_name)
    time.sleep(2)
    driver.find_element_by_name("myear").send_keys(Year_of_Release)
    time.sleep(3)
    driver.find_element_by_name("mdirector").send_keys(Director_Name)
    time.sleep(2)
    driver.find_element_by_name("mdist").send_keys(Distributor)
    time.sleep(2)
    driver.find_element_by_name("mproducer").send_keys(Producer)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[1]").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").click()
    time.sleep(10)




