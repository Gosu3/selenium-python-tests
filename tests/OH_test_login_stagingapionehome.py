import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("http://stagingapionehome.vnpt-technology.vn:6789/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys("admin@mailinator.com")
    driver.find_element(By.ID, "password").send_keys("ssdc@123")
    driver.find_element(By.CLASS_NAME, "md-btn-primary").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/customers"))
    assert "/customers" in driver.current_url

def test_login_fail(driver):
    driver.get("http://stagingapionehome.vnpt-technology.vn:6789/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys("saiuser")
    driver.find_element(By.ID, "password").send_keys("saipass")
    driver.find_element(By.CLASS_NAME, "md-btn-primary").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "invalid-feedback"))
    )
    assert "invalid" in driver.page_source.lower() or "sai" in driver.page_source.lower()