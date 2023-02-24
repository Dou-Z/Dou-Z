import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Get_Cookies import create_chrome_drive

browser = create_chrome_drive()
browser.get('https://login.taobao.com')
# 隐式等待
browser.implicitly_wait(10)
# 获取页面元素模拟用户输入和点击行为
username_input = browser.find_element_by_xpath('//*[@id="fm-login-id"]')
username_input.send_keys('*********')  # 输入账号
time.sleep(2) 
password_input = browser.find_element_by_xpath('//*[@id="fm-login-password"]')
password_input.send_keys('***********') # 输入密码
login_button = browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button')
login_button.click()
# 显示等待
wait_obj = WebDriverWait(browser,10)
wait_obj.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "#J_SiteNavLogin > div.site-nav-menu-hd > div > a")))

with open('taobao1.json','w') as file:
    json.dump(browser.get_cookies(),file)
