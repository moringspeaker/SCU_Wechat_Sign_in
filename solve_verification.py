import sys
import json
import base64


import Config

IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    print('wrong_version,PY2 is needed')
    exit()
# 防止https证书校验不正确
import ssl


class Verify:
    def __init__(self):

        self.API_KEY=Config.read_api_key()
        self.SECRET_KEY=Config.read_secret_key()
        self.url=''
        self.img_path=''
        ssl._create_default_https_context = ssl._create_unverified_context
        self.OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
        #TOKEN start
        self.TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

    def set(self,img_path,url):
        self.url = url
        self.img_path = img_path
    """"
        读取token
    """
    def fetch_token(self):
        params = {'grant_type': 'client_credentials',
                  'client_id': self.API_KEY,
                  'client_secret': self.SECRET_KEY}
        post_data = urlencode(params)
        if (IS_PY3):
            post_data = post_data.encode('utf-8')
        req = Request(self.TOKEN_URL, post_data)
        try:
            f = urlopen(req, timeout=5)
            result_str = f.read()
        except URLError as err:
            print(err)
        if (IS_PY3):
            result_str = result_str.decode()

        result = json.loads(result_str)

        if ('access_token' in result.keys() and 'scope' in result.keys()):
            if not 'brain_all_scope' in result['scope'].split(' '):
                print('please ensure has check the  ability')
                exit()
            return result['access_token']
        else:
            print('please overwrite the correct API_KEY and SECRET_KEY')
            exit()

    """
        读取文件
    """
    def read_file(self):
        f = None
        try:
            f = open(self.img_path, 'rb')
            return f.read()
        except:
            print('read image file fail')
            return None
        finally:
            if f:
                f.close()

    """
        调用远程服务
    """
    def request(self, data):
        req = Request(self.url, data.encode('utf-8'))
        has_error = False
        try:
            f = urlopen(req)
            result_str = f.read()
            if (IS_PY3):
                result_str = result_str.decode()
            return result_str
        except  URLError as err:
            print(err)

def main_verify(imgpath):
    Ver=Verify()
    # 获取access token
    token = Ver.fetch_token()

    # 拼接通用文字识别高精度url
    image_url = Ver.OCR_URL + "?access_token=" + token
    Ver.set(imgpath,image_url)
    text = ""

    # 读取测试图片
    file_content = Ver.read_file()
    # 调用文字识别服务
    result = Ver.request(urlencode({'image': base64.b64encode(file_content)}))

    # 解析返回结果
    result_json = json.loads(result)
    for words_result in result_json["words_result"]:
        text = text + words_result["words"]

    # 打印文字
    return(text)
