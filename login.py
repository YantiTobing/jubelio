from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Lokasi ChromeDriver
driver_path = 'C:/chromedriver/chromedriver.exe'

# Inisialisasi Chrome WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Buka halaman login Jubelio
driver.get('https://app.jubelio.com/login')

# Isi formulir login
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('qa.rakamin.jubelio@gmail.com')

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('Jubelio123!')

# Submit formulir
password_input.send_keys(Keys.RETURN)

# Tunggu halaman beranda dimuat (misalnya, dengan menunggu elemen tertentu muncul)
# contoh, menunggu elemen dengan ID 'dashboard' muncul
driver.implicitly_wait(10)
dashboard_element = driver.find_element('id', 'user_menu')

# Lakukan tindakan lain setelah login
# ...

# Tutup browser
driver.quit()
