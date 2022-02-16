# -*- coding: utf-8 -*-
import json
import requests
import datetime
import time
import Config
import get_cookies as gc

today = datetime.date.today()
date = "%4d%02d%02d" % (today.year, today.month, today.day)
createTime = round(time.time())
now = datetime.time()
class Auto:
    def __init__(self):
        self.url="https://wfw.scu.edu.cn/ncov/wap/default/save"
    def set_headers(self):
        cookie=gc.Cookie()
        self.headers = {
            "Accept": "application / json, text / javascript, * / *; q = 0.01",
            "Accept - Encoding": "gzip, deflate, br",
            "Accept - Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "User - Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)",
            "X - Requested - With": "XMLHttpRequest",
            "Cookie": cookie,
            "Content - Length": "2910",
            "Content - Type": "application / x - www - form - urlencoded; charset = UTF - 8",
            "Referer": "https: // wfw.scu.edu.cn / ncov / wap / default / index",
            "Origin": "https: // wfw.scu.edu.cn",
            "Sec - Fetch - Dest": "empty",
            "Sec - Fetch - Mode": "cors",
            "Sec - Fetch - Site": "same - origin",
            "Connection": "keep - alive",
            "Host": "wfw.scu.edu.cn",
        }
    def set_data(self):
        id=Config.read_id()
        uid = Config.read_uid()
        campus=Config.read_campus()
        address=Config.read_address()
        geo=Config.read_geo()
        area=Config.read_area()
        self.data = {
            'date': date,
            'uid': uid,
            'created': createTime,
            'sfzx': '1',  # 是否在校
            'szxqmc': campus,  # 所在校区 （华西校区， 江安校区， 望江校区）
            'bzxyy': '',  # 不在校原因 （1-6）
            'address': address,
            'geo_api_info': geo,
            'area': area,  # 位置
            'province': '四川省',
            'city': '成都市',
            'zgfxdq': '0',  # 今日是否在中高风险地区？（中高风险地区信息可通过国务院客户端小程序实时查询）
            'tw': '3',  # 体温 （1-9， 1：35℃以下， 2：35℃-36.5℃， 3：36.6℃-36.9℃， 4： 37℃-37.3℃）
            'sfcxtz': '0',  # 今日是否出现发热、乏力、干咳、呼吸困难等症状？
            'sfyyjc': '0',  # 是否到相关医院或门诊检查？
            'sfjcbh': '0',  # 今日是否接触无症状感染/疑似/确诊人群？
            'jcbhlx': '',  # （疑似， 确诊）
            'jcbhrq': '',  # 接触时间
            'mjry': '0',  # 今日是否接触密接人员
            'csmjry': '0',  # 近14日内本人/共同居住者是否去过疫情发生场所（市场、单位、小区等）或与场所人员有过密切接触？
            'sfcyglq': '0',  # 是否处于观察期？
            'gllx': '',  # 观察场所 （1—4）
            'glksrq': '',  # 观察开始时间
            'sfjxhsjc': '0',  # 2020年9月1日（含）后是否进行过新冠肺炎核酸检测？
            'hsjcrq': '',  # 核酸检测时间
            'hsjcdd': '',  # 核酸检测地点
            'hsjcjg': '0',  # 核酸检测结果 （0-2）
            'sfcxzysx': '0',  # 是否有任何与疫情相关的， 值得注意的情况？
            'qksm': '',  # 情况说明
            'jcjgqr': '0',
            'remark': '',
            'sfjcwhry': '0',
            'sfjchbry': '0',
            'bztcyy': '',
            'sftjhb': '0',
            'sftjwh': '0',
            'szcs': '',
            'szgj': '',
            'jcjg': '',
            'jcqzrq': '',
            'sfjcqz': '',
            'szsqsfybl': '0',
            'sfsqhzjkk': '0',
            'sfjzdszxgym':'',
            'sfjzxgym':'',
            'sqhzjkkys': '',
            'sfygtjzzfj': '0',
            'gtjzzfjsj': '',
            'id': id,
            'gwszdd': '',
            'sfyqjzgc': '',
            'jrsfqzys': '',
            'jrsfqzfy': '',
            'szgjcs': '',
            'ismoved': '0'
        }

    def run(self):
        # print (json.dumps(self.data, encoding='UTF-8', ensure_ascii=False))
        res = requests.post(self.url,headers=self.headers,data=self.data)
        print(res.json())
        if res.status_code==200:
            try:
                res.encoding = 'utf-8'
                print(res.json()['m'])
            except:
                print('unkown error')
        else:
            print("connection error:",res.status_code)
def main():
    #print(time.strftime("%Y%m%d"))
    uses = Auto()
    uses.set_headers()
    uses.set_data()
    uses.run()

if __name__=='__main__':
    main()