import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_chrome_drive(*,headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
    options.add_experimental_option('useAutomationExtension',False)
    browser = webdriver.Chrome(options=options)

    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source':'Object.defineProperty(navigator,"webdriver",{get: () => undefined})'}
    )
    return browser


def add_cookies(browser,cookie_file):
    with open(cookie_file,'r') as file:
        cookies_list = json.load(file)
        for cookie_dict in cookies_list:
            if cookie_dict['secure']:
                browser.add_cookie(cookie_dict)

