from datetime import date, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_date_selection():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:8000/hotel.html")

        check_in = date.today() + timedelta(days=7)
        check_out = check_in + timedelta(days=3)

        checkin = driver.find_element(By.ID, "checkin")
        checkout = driver.find_element(By.ID, "checkout")

        checkin.send_keys(check_in.isoformat())
        checkout.send_keys(check_out.isoformat())

        assert checkin.get_attribute("value") == check_in.isoformat()
        assert checkout.get_attribute("value") == check_out.isoformat()
    finally:
        driver.quit()


def test_guest_selection():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:8000/hotel.html")

        driver.find_element(By.ID, "adult-plus").click()
        driver.find_element(By.ID, "child-plus").click()
        driver.find_element(By.ID, "room-plus").click()

        assert driver.find_element(By.ID, "adults").get_attribute("value") == "2"
        assert driver.find_element(By.ID, "children").get_attribute("value") == "1"
        assert driver.find_element(By.ID, "rooms").get_attribute("value") == "2"
    finally:
        driver.quit()


def test_hotel_search():
    driver = webdriver.Chrome()
    try:
        driver.get("http://localhost:8000/hotel.html")

        driver.find_element(By.ID, "search-button").click()

        results = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search-results"))
        )

        assert results.is_displayed()
        assert "Hotel search completed successfully." in results.text
    finally:
        driver.quit()

