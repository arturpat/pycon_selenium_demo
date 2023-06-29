from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


date_out = "2023-12-03"
date_in = "2023-12-10"


# Leave comments!
driver = webdriver.Firefox()
driver.get("https://www.ryanair.com/en/en/")  # skyscanner, wizzair

# just a waiter object for use later
wait = WebDriverWait(driver, 20)

driver.close()  # a breakpoint here will make the execution stop *before* closing Firefox
