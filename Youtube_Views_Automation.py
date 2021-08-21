import time, random
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"F:\VSCode Projects\Selenium\webdriver\chromedriver.exe")
driver.maximize_window()

for i in range(5):
    print("Playing video for {} time".format(i))
    driver.get("https://www.youtube.com/watch?v=PAKKdS5_SC4")
    sleep_time = random.randint(60, 240) 
    time.sleep(sleep_time)

driver.quit()