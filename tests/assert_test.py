from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# Kiểm tra tiêu đề có chứa từ 'Google'
assert "Google" in driver.title, "Tiêu đề không chứa 'Google'"

driver.quit()
