from http.server import executable
from selenium import webdriver

base_url = "https://amazon.in"
driver = webdriver.Chrome(
    executable_path="E:\#Universitas Muhammadiyah Pontianak\#TUGAS SEMESTER\SEMESTER 1-8\#SEMESTER 5-6\SEMESTER 6\ASRUL ABDULLAH\selenium\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(base_url)
assert "Amazon" in driver.title
driver.close()