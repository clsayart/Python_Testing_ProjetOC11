from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions

url = 'http://127.0.0.1:5000/'


def test_open_firefox_window():
    service = Service(GeckoDriverManager().install(), log_path='tests/functional_tests/geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    driver.get(url)
    sleep(2)
    print("2-driver")
    return driver


def test_login():
    driver = test_open_firefox_window()
    form = driver.find_element(By.NAME, "email")
    form.send_keys("kate@shelifts.co.uk")
    form.submit()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(url + 'showSummary'))
    sleep(5)
    print("5-login")
    assert driver.find_element(By.LINK_TEXT, 'Logout')
    driver.quit()


def test_display_points():
    driver = test_open_firefox_window()
    driver.get(url + 'displayPoints')
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, 'points_table')
    sleep(5)
    print("5-points")
    driver.quit()


def test_purchase_places():
    driver = test_open_firefox_window()
    form = driver.find_element(By.NAME, "email")
    form.send_keys("kate@shelifts.co.uk")
    form.submit()
    driver.implicitly_wait(5)
    link = driver.find_element(By.LINK_TEXT, 'Book Places')
    link.click()
    driver.implicitly_wait(5)
    form = driver.find_element(By.NAME, 'places')
    form.send_keys("6")
    form.submit()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(url + 'purchasePlaces'))
    assert driver.find_element(By.LINK_TEXT, 'Logout')
    sleep(5)
    print("5-purchase")
    driver.quit()


def main():
    test_open_firefox_window()
    test_display_points()
    test_login()
    test_purchase_places()



if __name__ == "__main__":
    main()
