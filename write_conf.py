import configparser
# 生成ConfigParser对象
config = configparser.ConfigParser()
# 读取配置文件
filename = 'config.ini'
config.read('config.ini',encoding='utf-8')
# 添加section
if not config.has_section('api'):
    config.add_section('api')
    config.set('api','api_key','jBycg8wTstSk3d9As3LwGsNC')
    config.set('api','secret_key','XFTb8mB5mUgudDRcevotil5yArIEzwL2')
else:
    pass
if not config.has_section('usr'):
    config.add_section('usr')
    config.set('usr','username','2018141461169')
    config.set('usr','password','gcy@211139902')
else:
    pass
config.write(open(filename, 'w'))

