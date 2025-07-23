import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

def get_login_data():
    wb = openpyxl.load_workbook("login_data.xlsx")
    sheet = wb["Sheet1"]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Sửa lại nếu dữ liệu bắt đầu từ dòng 2
        data.append(row)
    return data

@pytest.mark.parametrize("username,password,expected_result", get_login_data())
def test_login_excel(driver, username, password, expected_result):
    driver.get("http://10.15.12.134:8081")
    username_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "username"))
    )
    username_input.clear()
    username_input.send_keys(username)
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    if expected_result == "success":
        WebDriverWait(driver, 10).until(EC.url_contains("/devices"))
        assert "/devices" in driver.current_url or "devices" in driver.current_url
    else:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "invalid-feedback"))
        )
        assert "invalid" in driver.page_source.lower() or "sai" in driver.page_source.lower()