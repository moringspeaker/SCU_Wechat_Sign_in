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
if not config.has_section('location'):
    config.add_section('location')
    config.set('location','szxqmc','望江校区')
    config.set('location','address','四川省成都市武侯区望江路街道四川大学四川大学望江校区')
    config.set('location', 'area', '四川省 成都市 武侯区')
    config.set('location', 'geo_api_info', '{"type":"complete","info":"SUCCESS","status":1,"$Da":"jsonp_303061_","position":{"Q":30.63073,"R":104.08733000000001,"lng":104.08733,"lat":30.63073},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"028","adcode":"510107","businessAreas":[{"name":"小天竺","id":"510107","location":{"Q":30.639354,"R":104.06894199999999,"lng":104.068942,"lat":30.639354}}],"neighborhoodType":"科教文化服务;学校;高等院校","neighborhood":"四川大学","building":"","buildingType":"","street":"望江路","streetNumber":"29号","country":"中国","province":"四川省","city":"成都市","district":"武侯区","township":"望江路街道"},"formattedAddress":"四川省成都市武侯区望江路街道四川大学四川大学望江校区","roads":[],"crosses":[],"pois":[]}')
config.write(open(filename, 'w'))

