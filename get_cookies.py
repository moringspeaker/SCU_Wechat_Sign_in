from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import solve_verification as sv
import Config as cg

class LOG():
    def __init__(self):
        self.target = 'https://wfw.scu.edu.cn/ncov/wap/default/index'  # 微服务地址
        self.username = cg.read_username()  # 用户名
        self.password = cg.read_passwd()  # 密码
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    def log(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        self.driver= webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe", chrome_options=chrome_options)
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
                print("失败")
                return -1
            self.driver.find_element_by_xpath('//input[@placeholder="请输入学号/工号"]').send_keys(self.username)
            time.sleep(0.5)
            self.driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys(self.password)
            time.sleep(0.5)
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div/div/img') \
                .screenshot(u"D:\自动打卡\Wechat sign_in\catcha.png")
            self.driver.find_element_by_xpath('//input[@placeholder="请输入验证码"]').send_keys(sv.main_verify('catcha.png'))
            time.sleep(0.5)
            log_element=self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/button')
            self.driver.execute_script("arguments[0].click();",log_element)# 点击登录
            # 检测是否成功登录
            statue += 1
            if self.driver.current_url == self.target:
                print('correct')
                break
            else:
                print('wrong verification code' )
            if statue == 50:
                print('[%s] (%s) 请检查账号密码，或稍后再试！' % eval(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                self.driver.quit()
                return 1  # 超时返回值
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
    cookie=raw_cookie[0]
    for i in range(1,len(raw_cookie)):
        cookie=cookie+'; '+str(raw_cookie[i])
    print(cookie)
    return cookie
# if __name__=='__main__':
#     Cookie()