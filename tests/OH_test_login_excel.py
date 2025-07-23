import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

def get_login_data():
    wb = openpyxl.load_workbook("login_data_onehome.xlsx")
    sheet = wb["Sheet1"]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Bỏ qua dòng tiêu đề
        data.append(row)
    return data

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("email,password,expected_result", get_login_data())
def test_login_excel(driver, email, password, expected_result):
    driver.get("http://stagingapionehome.vnpt-technology.vn:6789/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "md-btn-primary").click()
    if expected_result == "success":
        WebDriverWait(driver, 20).until(EC.url_contains("/customers"))
        assert "/customers" in driver.current_url
    else:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "invalid-feedback"))
        )
        page_source = driver.page_source.lower()
        assert (
            "invalid" in page_source
            or "sai" in page_source
            or "đăng nhập không thành công" in page_source
        )