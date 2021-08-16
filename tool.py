import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import shutil
def wait(times):
    time.sleep(times)

def login(account, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    b = webdriver.Chrome(r'C:\Users\Anchovy\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    b.set_window_size(1920, 1080)
    b.implicitly_wait(10)
    url = 'http://yqdj.zucc.edu.cn/feiyan_api/h5/html/daka/daka.html'
    b.get(url)
    b.find_element_by_xpath("//input[@id='username']").send_keys(account)
    b.find_element_by_xpath("//input[@id='password']").send_keys(password)
    b.find_element(By.XPATH, '//*[@id="main"]/div/div/div[5]/div/input[1]').click()
    wait(1)
    return b



