# -*- coding:utf-8 -*-
from util.load_phantomjs import load_phantomjs
from util.login import login

phantomjs = load_phantomjs()
login_url = 'http://campus.chinaunicom.cn/ilearn/en/learner/jsp/login.jsp'
    
    
print(login(phantomjs,login_url))
