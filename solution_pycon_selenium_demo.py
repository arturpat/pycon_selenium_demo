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
# to be written live
elem = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "cookie-popup-with-overlay__button")))
elem.click()

driver.get(f"https://www.ryanair.com/us/en/trip/flights/"
           f"select?adults=1&teens=0&children=0&infants=0&"
           f"dateOut={date_out}&dateIn={date_in}&isConnectedFlight=false&"
           f"isReturn=true&discount=0&promoCode=&"
           f"originIata=WMI&destinationIata=MLA&tpAdults=1&"
           f"tpTeens=0&tpChildren=0&tpInfants=0&tpStartDate=2022-10-25&"
           f"tpEndDate=2022-10-30&tpDiscount=0&tpPromoCode=&tpOriginIata=WMI&"
           f"tpDestinationIata=MLA")

# go straight for the price:
elem = wait.until(ec.visibility_of_element_located((By.TAG_NAME, "flights-price-simple")))
# note: read exceptions

# to be written live
# Get prices, make sure there are just two. It takes a moment to load.
sleep(2)
price_elements = driver.find_elements(By.TAG_NAME, "flights-price-simple")
assert len(price_elements) == 2, f"Expected 2 prices, got {[e.text for e in price_elements]}"  # possible issue: promo
# present stop at any exception
print(f"Outbound price: {price_elements[0].text}")
print(f"Inbound price: {price_elements[1].text}")
# as of 02.09.2022: 22.93, 61.75
# as of 04.09.2022: 18.52, 86.67
# as of 07.09.2022: 35.55, 99.03
pass

# destination
# elem = driver.find_element(by=By.ID, value="input-button__destination")
# sleep(1)
# elem.send_keys("Malta")
# sleep(2)
# elem = driver.find_element(by=By.CLASS_NAME, value="b2 airport-item")
# elem.click()
# sleep(3)
# pass


# # AIRFRANCE
# # to be written live
# wait.until(ec.visibility_of_element_located((By.ID, 'accept_cookies_btn')))
# elem = driver.find_element(by=By.ID, value="accept_cookies_btn")
# elem.click()
# ############
#
# departure_textbox = driver.find_element(by=By.ID, value="mat-input-1")
# departure_textbox.click()
# departure_textbox.send_keys("WWA")
