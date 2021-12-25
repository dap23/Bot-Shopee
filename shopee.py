from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import datetime
import time

driver_location = "C:\chromedriver_win32"
binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

link_product = time_target=None
hariIni = datetime.datetime.now()

def SetUp():
    options = webdriver.ChromeOptions()
    options.binary_location = binary_location
    browser = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
    browser.delete_all_cookies()
    return browser

def InputData():
    global link_product, time_target, hariIni
    link_product = input("[+] Masukan Link Product: ")
    jam = int(input("[+] Jam Beli : "))
    menit = int(input("[+] Menit Beli : "))
    detik = int(input("[+] Detik Beli : "))
    time_target = datetime.datetime(hariIni.year, hariIni.month, hariIni.day, jam, menit, detik)


def click(browser, element_css):
    WebDriverWait(browser, 60).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    
    WebDriverWait(browser, 60).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    browser.find_element_by_css_selector(element_css).click()


InputData()
browser = SetUp()
wait = WebDriverWait(browser, 60)

# Login
browser.get("https://shopee.co.id/buyer/login")
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.shopee-avatar__img')))

# Menuju Link Product
browser.get(link_product)

# Timer
sl = time_target - datetime.datetime.now()
time.sleep(sl.seconds)
browser.refresh()

click(browser, '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div:nth-child(5) > div > div > button.btn.btn-solid-primary.btn--l._3Kiuzg')
wait.until(ec.invisibility_of_element((By.CSS_SELECTOR, '.action-toast')))

# Pilih Variasi
click(browser, '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div._2nr4HE > div > div.flex._3AHLrn._2XdAdB._1C5-TB > div > div:nth-child(1) > div > button:nth-child(1)')
click(browser, '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div._2nr4HE > div > div.flex._3AHLrn._2XdAdB._1C5-TB > div > div:nth-child(2) > div > button:nth-child(4)')

# Beli Sekarang
click(browser, '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div:nth-child(5) > div > div > button.btn.btn-solid-primary.btn--l._3Kiuzg')
wait.until(ec.invisibility_of_element((By.CSS_SELECTOR, '.action-toast')))

# Checkout
click(browser, '#main > div > div:nth-child(2) > div._164M6a > div > div:nth-child(3) > div._2jol0L > div.W2HjBQ.zzOmij > button.shopee-button-solid.shopee-button-solid--primary')
wait.until(ec.invisibility_of_element((By.CSS_SELECTOR, '.loading-spinner-popup')))


# Metode Pembayaran
click(browser, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(1) > button')


# Buat Pesanan
click(browser, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.PC1-mc > div._3swGZ9 > button')