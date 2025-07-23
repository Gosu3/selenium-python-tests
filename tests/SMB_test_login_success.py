import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Hoặc webdriver.Firefox() nếu bạn dùng Firefox
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("http://10.15.12.134:8081")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("ump")
    driver.find_element(By.NAME, "password").send_keys("ump@2016")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/devices"))
    assert "/devices" in driver.current_url or "devices" in driver.current_url

def test_login_fail(driver):
    driver.get("http://10.15.12.134:8081")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("wronguser")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Chờ thông báo lỗi xuất hiện (giả sử có thẻ div với class 'invalid-feedback')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "invalid-feedback"))
    )
    assert "invalid" in driver.page_source.lower() or "sai" in driver.page_source.lower()