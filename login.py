from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Lokasi ChromeDriver Di Lokall
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

# Submit formulir Enter 
password_input.send_keys(Keys.RETURN)

# Tunggu halaman beranda dimuat user menu
driver.implicitly_wait(10)
dashboard_element = driver.find_element(By.ID, 'user_menu')

if dashboard_element : 
    print("success login...")
    driver.get("https://app.jubelio.com/home/inventory")
    
     # Cari elemen berdasarkan teks "Penyesuaian Persediaan"
    button_element = driver.find_element(By.XPATH, '//span[text()="Penyesuaian Persediaan"]')

    # Klik tombol Penyesuaian Persediaan
    button_element.click()

     # Cari elemen input dengan placeholder "Scan"
    input_element = driver.find_element(By.XPATH, '//input[@placeholder="Scan"]')

    # Isi teks "IphoneGoldXS" ke dalam input
    input_element.send_keys("IphoneGoldXS")

      # Cari tombol "Scan"
    scan_button = driver.find_element(By.XPATH, '//button[contains(@class, "ladda-button")]//span[text()="Scan"]')

    # Klik tombol "Scan"
    scan_button.click()

    simpan_button = driver.find_element(By.XPATH, '//button[contains(@class, "ladda-button")]//span[text()="Simpan"]')

    # Klik tombol "Simpan"
    simpan_button.click()


# Tutup browser
driver.quit()
