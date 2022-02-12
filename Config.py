import configparser

config=configparser.ConfigParser()
#读取配置文件
filenam='config.ini'
config.read(filenam,encoding='utf-8')
all_sections=config.sections()
print('sections:',all_sections)

def read_api_key():
    api_key= config.get('api', 'api_key')
    return api_key

def read_secret_key():
    secret_key=config.get('api','secret_key')
    return secret_key

def read_username():
    username= config.get('usr', 'username')
    return username

def read_passwd():
    pasword= config.get('usr', 'password')
    return pasword

