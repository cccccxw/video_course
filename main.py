# -*- coding:utf-8 -*-
from util.load_phantomjs import load_phantomjs
from module.login import login
from module.run import run
from url.url import *

phantomjs = load_phantomjs()
login_url = 'http://campus.chinaunicom.cn/ilearn/en/learner/jsp/login.jsp'
search_url = url_6  #分段开了，可合并  url_1,url_2,url_3,url_4,url_5,url_6

ps = login(phantomjs,login_url)

print(search_url)
try:
    for i in range(len(search_url)):
        if search_url[i]:
            print(run(ps,search_url[-i]))
            print("完成第"+str(i)+"个")
except:
    print("error3!")
    exit(0)
finally:
    ps.close()
