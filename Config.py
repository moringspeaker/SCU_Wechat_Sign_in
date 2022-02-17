import configparser

config=configparser.ConfigParser()
#读取配置文件
filenam='config.ini'
config.read(filenam,encoding='gb2312')
all_sections=config.sections()
def read_api_key():
    api_key= config.get('api', 'api_key')
    return api_key

def read_secret_key():
    secret_key=config.get('api','secret_key')
    return secret_key

# def read_username():
#     username= config.get('usr', 'username')
#     return username
#
# def read_passwd():
#     pasword= config.get('usr', 'password')
#     return pasword

def read_uid():
    uid= config.get('uid', 'UID')
    return uid

def read_id():
    id = config.get('uid', 'ID')
    return id

def read_campus():
    campus=config.get('location','szxqmc')
    return campus

def read_address():
    address=config.get('location','address')
    return address

def read_geo():
    geo=config.get('location','geo_api_info')
    return geo

def read_area():
    area=config.get('location','area')
    return area