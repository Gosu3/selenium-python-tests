from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Mở trang web
driver.get("https://www.google.com")

# In tiêu đề
print("Tiêu đề trang:", driver.title)

# Đóng trình duyệt
driver.quit()
