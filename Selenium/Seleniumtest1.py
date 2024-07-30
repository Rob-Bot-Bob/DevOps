from selenium import webdriver

# PATH = "C:\\Users\\ferna\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe"
# driver = webdriver.Chrome(PATH) 


driver = webdriver.Chrome()
driver.get("https://www.icg3d.com/")
print(driver.title)
driver.quit()