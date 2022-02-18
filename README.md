# SCU_Wechat_Sign_in
川大自动微信打卡程序
=========
注意：本项目只是用于交流学习爬虫，只设置了特定的校区作为打卡的地点信息作为测试，如果要修改打卡位置或者隐瞒真实的地理位置等，需要使用者自己修改程序配置，造成的后果与本程序无关

**快速开始**：  
----
>**首先**
>
>我采用的方法：使用Fiddler抓包，获得POST报文内容,修改你的uid    
>
>[你可以在这里下载安装最新版的Fiddler](https://www.telerik.com/fiddler)  
>
>然后就是使用Fiddler抓包，获取你的uid和id  
>
>之后就是在post.py里找到uid和id，修改成你的对应id即可  
>
>同样地：  
>
>你也可以使用浏览器做到这一点，使用Chrome或其他浏览器的Network查看发送包的信息  
>
>>**第二步**设置github repository secret：  
>>
你一共需要设置四个secret key,如果你不需要每天在打卡后通过邮件得知自己的打卡状况的话可以不设置mail开头的两个secret  

并且删除_TEST.yml_文件后面关于发邮件的Action  

注意设置一个**_WECHAT_USR_NAME_**的secret,这是你的微信小程序登录帐户名也就是你的**学号**，另一个设置**WECHAT_PASSWD**的  

secret,这是你的**微信小程序登录密码**  

###接下来就可以快速开始打卡了（只支持江安校区的打卡模板，需要的可以自行修改，因为一些众所周知的原因，这里不提供其他的打卡模板）  

**开发原理**： 
---
>本爬虫采用了python的**selenium**库和**requests**库进行开发，其中采用**selenium**库自动获取打卡的cookies，采用**requests**库来构建报文并自动发送  
>
其中使用selenium获取cookie的做法采用了百度的验证码识别API,原则上来讲我的token是不能直接写到代码中的，但是我为了方便大家直接快速上手，所以保留在了代码中，  

希望如果有人使用的话可以去自己申请并更换，在config.ini中就可以进行更换  

其中用selenium获取Cookie的做法参考了[somenothing](https://github.com/somenothing/SCU-ncov_checkpoint)这位大佬的代码  

大佬的代码功能齐全可以实现自动登录，获取Cookie并且自己写了发送邮件的代码，但是由于我感觉后面进行登录的操作较为繁琐，所以自己重新用request构造报文提交  

我感觉更方便简洁，同时使用别人写好的发送邮件的Action，如果你要使用发送邮件的功能，你需要自己去选择自己的邮箱，打开**POP3/SMTP服务**,并且将自己邮箱的  

邮箱登录账号和开启**POP3/SMTP服务**后获得的密码分别设置为**MAIL_USERNAME**和**MAIL_PASSWORD**，设置方法同上。

>>本项目采用GitAction实现自动打卡功能，在_TEST.yml_文件里设置了详细的自动运行的actions工作流，如果感兴趣可以自行了解（顺便吐槽一下GitAction真的太难debug了，以后还是不用了）  
>>

**详细配置**：  
>你可以在_TSET.yml_中的：  

    schedule:
        - cron: '0 1 * * *'
  
这里修改详细的时间段，注意Github的官方时间比北京时间慢了8小时，所以我设置的一点就是北京时间的九点  

同样地，你也可以自行配置_config.ini_中的_geo_api_info_,这里可以参考[somenothing](https://github.com/somenothing/SCU-ncov_checkpoint)大佬使用的方法获取虚拟的地理位置，  

也可以自行使用高德地图的api获取信息并直接填到_config.ini_中
