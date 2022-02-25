# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import solve_verification as sv
import Config as cg
import os

class LOG():
    def __init__(self):
        self.target = 'https://wfw.scu.edu.cn/ncov/wap/default/index'  # 微服务地址
        self.username = os.environ['USR_NAME']  # 用户名
        self.password = os.environ['PASSWD']  # 密码
        # self.username = '2018141461169'  # 用户名
        # self.password = 'gcy@211139902'  # 密码
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    def log(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        self.driver= webdriver.Chrome()
        self.driver.get(self.target)
        statue=0
        while True:
            try:  # 切换为账号密码登录
                self.driver.switch_to.frame('loginIframe')  # 切换frame
                switch_element = WebDriverWait(self.driver, 1).until(
                    ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div[3]'))
                )
                switch_element.click()
            except:
                # print("Fail")
                # return -1
                pass
            input_elements = self.driver.find_elements_by_tag_name('input')
            username_element, password_element, verification_element = input_elements
            username_element.send_keys(self.username)#填用户名
            time.sleep(0.5)
            password_element.send_keys(self.password)#填密码
            time.sleep(0.5)
            base_code=self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div/div/img') \
                .screenshot_as_base64
            verification_element.send_keys(sv.main_verify(base_code))
            time.sleep(0.5)
            log_element=self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/button')
            self.driver.execute_script("arguments[0].click();", log_element)
            # log_element.click()
            # 检测是否成功登录
            statue += 1
            if self.driver.current_url == self.target:
                print('correct')
                break
            else:
                print('wrong verification code' )
            if statue == 50:
                print('[%s] (%s) Please check the account and retry it later！' % eval(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                self.driver.quit()
                # return 1  # 超时返回值
                exit(0)
        orCookies=self.driver.get_cookies()
        self.driver.quit()
        cookies=[]
        for item in orCookies:
            cookies.append(item['name']+'='+item['value'])
        cookies.insert(0,cookies.pop())
        return cookies

def Cookie():
    l=LOG()
    raw_cookie=l.log()
    if raw_cookie!=1 and raw_cookie!=-1:
        cookie=raw_cookie[0]
    else:
        exit(0)
    for i in range(1,len(raw_cookie)):
        cookie=cookie+'; '+str(raw_cookie[i])
    with open('cookie.txt', 'w', encoding='utf8') as f:
        f.write(cookie)
    return cookie
if __name__=='__main__':
    Cookie()