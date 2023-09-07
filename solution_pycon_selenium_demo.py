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

# first, open the main page and click through cookie banner
# to be written live
elem = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "cookie-popup-with-overlay__button")))
elem.click()

driver.get(f"https://www.ryanair.com/us/en/trip/flights/"
           f"select?adults=1&teens=0&children=0&infants=0&dateOut={date_out}&"
           f"dateIn={date_in}&isConnectedFlight=false&isReturn=true&discount=0&"
           f"promoCode=&originIata=GDN&destinationIata=NAP&tpAdults=1&tpTeens=0&"
           f"tpChildren=0&tpInfants=0&tpStartDate={date_out}&tpEndDate={date_in}&"
           f"tpDiscount=0&tpPromoCode=&tpOriginIata=GDN&tpDestinationIata=NAP")

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
# as of 26.06.2022: 76.97, 70.07
# as of 07.09.2023: 52.36, 63.66

driver.close()

pass
