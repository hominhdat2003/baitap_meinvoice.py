import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from type import MEINVOICE_URL, Ma_Hoa_Don
import time

from logger_config import setup_logger
from chrome_config import create_chrome_driver

logging = setup_logger()
driver = create_chrome_driver()
wait = WebDriverWait(driver, 20)

logging.info("Truy cập trang web")
driver.get(MEINVOICE_URL)

logging.info(f"Nhập mã hóa đơn: {Ma_Hoa_Don}")
input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Nhập mã tra cứu hóa đơn']")))
input_box.send_keys(Ma_Hoa_Don)

search_button = wait.until(EC.element_to_be_clickable((By.ID, "btnSearchInvoice")))
search_button.click()
time.sleep(3)  
try:
    invoice_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.download-invoice")))
    invoice_button.click()

    download_pdf_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.dm-item.pdf.txt-download-pdf")))
    download_pdf_button.click()

    logging.info(f"Mã hóa đơn {Ma_Hoa_Don} hợp lệ. Đã tải PDF.")

except Exception:
    logging.warning(f"Mã hóa đơn {Ma_Hoa_Don} không hợp lệ hoặc không tồn tại.")
