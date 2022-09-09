from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


date_out = "2022-10-25"
date_in = "2022-10-30"


# Leave comments!
driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("https://www.ryanair.com/en/en/")  # skyscanner, wizzair

# just a waiter object for use later
wait = WebDriverWait(driver, 20)

# first, open the main page and click through cookie banner
