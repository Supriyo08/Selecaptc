# from selenium_recaptcha_solver import RecaptchaSolver
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# import random

# # Use a realistic user-agent
# test_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

# options = Options()

# # Remove headless for more human-like behavior
# # options.add_argument("--headless")  # Comment out or remove this line

# options.add_argument("--window-size=1920,1080")
# options.add_argument(f'--user-agent={test_ua}')
# options.add_argument('--no-sandbox')
# options.add_argument("--disable-extensions")

# # Initialize WebDriver
# driver = webdriver.Chrome(options=options)

# # Instantiate the solver
# solver = RecaptchaSolver(driver=driver)

# # Visit the page
# driver.get('https://www.google.com/recaptcha/api2/demo')

# # Random delay to mimic human behavior
# time.sleep(random.uniform(2, 4))

# # Find the reCAPTCHA iframe
# recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

# # Click reCAPTCHA
# solver.click_recaptcha_v2(iframe=recaptcha_iframe)

# # Wait a bit after clicking
# time.sleep(random.uniform(5, 10))

# # Keep the browser open for 1 minute
# time.sleep(0.1)

# # Close the browser
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytesseract
from PIL import Image
import time
import io
import base64

# Setup driver
driver = webdriver.Chrome()

# Open page
driver.get("https://www.google.com/recaptcha/api2/demo")

# Get captcha image as base64
captcha_img = driver.find_element(By.ID, "captchaImage")
captcha_base64 = captcha_img.screenshot_as_base64

# Decode and process
start = time.time()
captcha_bytes = base64.b64decode(captcha_base64)
captcha_img = Image.open(io.BytesIO(captcha_bytes))

# OCR using pytesseract
captcha_text = pytesseract.image_to_string(captcha_img, config='--psm 7 digits')
print("Detected CAPTCHA:", captcha_text.strip())

# Fill in fields
driver.find_element(By.ID, "username").send_keys("your_username")
driver.find_element(By.ID, "password").send_keys("your_password")
driver.find_element(By.ID, "captcha").send_keys(captcha_text.strip())

# Submit
driver.find_element(By.ID, "loginBtn").click()
end = time.time()

print(f"Process completed in {int((end-start)*1000)} ms")
