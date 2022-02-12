import requests
import datetime
import time
from selenium import webdriver

now = datetime.time()
class Auto:
    def __init__(self):
        self.url="https://wfw.scu.edu.cn/ncov/wap/default/save"
        self.headers={
            "Accept": "application / json, text / javascript, * / *; q = 0.01",
            "Accept - Encoding": "gzip, deflate, br",
            "Accept - Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "User - Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)",
            "X - Requested - With": "XMLHttpRequest",
            "Cookie": "eai-sess=3bpau43ev8ehb5ikir0m22otq4; UUkey=ca156130eb489acc3c29addcd08ebd6f; Hm_lvt_48b682d4885d22a90111e46b972e3268=1642522672,1643213781,1643559301,1644163012; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1644163389",
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
        self.body = "{}"
        self.data={
            "address":"四川省成都市武侯区浆洗街街道香月楠岸",
            "area":"四川省 成都市 武侯区",
            "bztcyy":"",
            "bzxyy":"",
            "city":"成都市",
            "created":"1644076922",
            "csmjry":"0",
            "date":time.strftime("%H%M%S"),
            "geo_api_info":'{"type":"complete","info":"SUCCESS","status":1,"fEa":"jsonp_248583_","position":{"Q":30.64968,"R":104.03769999999997,"lng":104.0377,"lat":30.64968},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"028","adcode":"510107","businessAreas":[{"name":"双楠","id":"510107","location":{"Q":30.641757,"R":104.02139899999997,"lng":104.021399,"lat":30.641757}},{"name":"草堂","id":"510105","location":{"Q":30.661496,"R":104.02935100000002,"lng":104.029351,"lat":30.661496}},{"name":"高升桥","id":"510107","location":{"Q":30.633603,"R":104.04211599999996,"lng":104.042116,"lat":30.633603}}],"neighborhoodType":"商务住宅;住宅区;住宅小区","neighborhood":"香月楠岸","building":"","buildingType":"","street":"大石南路","streetNumber":"39-5号","country":"中国","province":"四川省","city":"成都市","district":"武侯区","towncode":"510107001000","township":"浆洗街街道"},"formattedAddress":"四川省成都市武侯区浆洗街街道香月楠岸","roads":[],"crosses":[],"pois":[]}',
            "glksrq":"",
            "gllx":"",
            "gtjzzfjsj":"",
            "gwszdd":"",
            "hsjcdd":"",
            "hsjcjg":"",
            "hsjcrq":"0",
            "id":"52281172",
            "ismoved":"0",
            "jcbhlx":"",
            "jcbhrq":"",
            "jcjg":"",
            "jcjgqr":"0",
            "jcqzrq":"",
            "jrsfqzfy":"",
            "jrsfqzys":"",
            "jzdezxgymrq":"",
            "jzxgymrq":"2021-07-11",
            "mjry":"0",
            "province":"四川省",
            "qksm":"",
            "remark":"",
            "sfcxtz":"0",
            "sfcxzysx":"0",
            "sfcyglq":"0",
            "sfjcbh":"0",
            "sfjchbry":"0",
            "sfjcqz":"",
            "sfjcwhry":"0",
            "sfjzdezxgym":"0",
            "sfjzxgym":"1",
            "sfsqhzjkk":"0",
            "sftjhb":"0",
            "sftjwh":"0",
            "sfygtjzzfj":"0",
            "sfyqjzgc"
            "sfyyjc":"0",
            "sfzx":"1",
            "sqhzjkkys"
            "szcs":"",
            "szgj":"",
            "szgjcs":"",
            "szsqsfybl":"0",
            "szxqmc":"江安校区",
            "tw":"2",
            "uid":"31703",
            "zgfxdq":"0",
        }

    def get_cookie(self,url,user):
        driver = webdriver.Chrome()
        driver.get(url)

    def loggin(self):
        driver=webdriver.chrome()
        driver.get('https://wfw.scu.edu.cn/ncov/wap/default/index')
        time.sleep(5)
        driver.quit
    def run(self):
        print(self.data)
        res = requests.post(self.url, headers=self.headers,data=self.data)
        try:
            res.encoding='utf-8'
            pattern1 = '成功'
            pattern2='今天已经填报了'
            if pattern2 in res.text:
                print("今天已经填报了")
            elif pattern1 in res.text:
                print("填报完成")
            else:
                pass

        except:
         pass
if __name__ == "__main__":
    #print(time.strftime("%Y%m%d"))
    uses = Auto()
    uses.run()
