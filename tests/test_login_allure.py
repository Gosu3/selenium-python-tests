import allure
import time
from selenium.webdriver.common.by import By

@allure.title("Test đăng nhập với dữ liệu từ Excel")
@allure.step("Thực hiện login với username: {username}, password: {password}")
def test_login_from_excel(driver, login_data):
    username, password, expected = login_data

    driver.get("http://stagingapionehome.vnpt-technology.vn:6789/#/login")

    # Điền dữ liệu
    driver.find_element(By.ID, "email").send_keys(username or "")
    driver.find_element(By.ID, "password").send_keys(password or "")
    driver.find_element(By.XPATH, "//button[contains(text(),'Đăng Nhập')]").click()

    time.sleep(2)  # đợi phản hồi

    # Kiểm tra kết quả
    if expected == "success":
        assert "6789/#/customers" in driver.current_url, f"Đăng nhập thất bại! URL hiện tại: {driver.current_url}"
    else:
        error_elements = driver.find_elements(By.CLASS_NAME, "MuiAlert-message")
        assert any("sai" in el.text.lower() or el.text for el in error_elements), "Không hiện lỗi khi đăng nhập sai"
