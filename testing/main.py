from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Bước 1: Truy cập https://online.hcmute.edu.vn/
url = 'https://online.hcmute.edu.vn/'
driver.get(url)

#Bước 2: Đăng nhập
mssv = 'mssv'
pasword = 'password'
btnLogin = driver.find_element(By.CSS_SELECTOR, '#ctl00_lbtDangnhap')
btnLogin.click()

#Bước 3: Điền thông tin đăng nhập
txtMSSV = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ctl00_ctl00_txtUserName')
txtMSSV.send_keys(mssv)

txtPassword = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ctl00_ctl00_txtPassword')
txtPassword.send_keys(pasword)

btnLogin = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ctl00_ctl00_btLogin')
btnLogin.click()

#Bước 4: Truy cập trang thời khóa biểu
btnTKB = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ctl00_ctl00_lnkThoiKhoaBieu')
btnTKB.click()

#Bước 5: Lấy thông tin thời khóa biểu
cell = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ctl00_ctl00_ctl00_tblThoiKhoaBieu > tbody > tr:nth-child(3) > td:nth-child(2)')
print(cell.text)

driver.close()