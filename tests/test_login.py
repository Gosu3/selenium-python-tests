import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver, login_data):
    email, password, expected = login_data

    driver.get("http://stagingapionehome.vnpt-technology.vn:6789/#/login/")

    # Đợi và điền thông tin
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys(email us or "")
    driver.find_element(By.ID, "password").send_keys(password or "")
    login_button = driver.find_element(By.XPATH, "//button/span[text()='Đăng Nhập']")
    login_button.click()

    time.sleep(2)
    driver.save_screenshot("screen_debug.png")
    if expected == "success":
        assert "6789/#/customers" in driver.current_url, f"Đăng nhập thất bại! URL hiện tại: {driver.current_url}"
    else:
        error_elements = driver.find_elements(By.CLASS_NAME, "MuiAlert-message")
        assert error_elements and any(el.text.strip() for el in error_elements), "Không thấy thông báo lỗi!"
