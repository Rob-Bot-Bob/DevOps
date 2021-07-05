#there is an issue if you get the driver to run in windows whiel useing wsl it will not work, you have to use powershell I couldn't figure why, the path was set but still didn't work
from types import coroutine
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options=Options()

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--no-gpu')
# chrome_options.add_argument('--disable-setuid-sandbox')
# chrome_options.add_argument('--single-process')
# chrome_options.add_argument('--windo-size=1920,1080')

# chrome_options.binary_location = "/usr/bin/chrome-linux/chrom"

driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")#powershell funciona
#driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('12')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()

