# -*- coding:utf-8 -*-
#cookie from phantomjs to requests
def set_cookie_str(cookie_list = []):
    #print(cookie_list)
    cookie_dict = {}
    for i in range(len(cookie_list)):
        cookie_dict[cookie_list[i]['name']] = cookie_list[i]['value'] 
    cookie_str = ''
    cookie_str = 'SESSIONID=' +cookie_dict['SESSIONID'] + '; site=' +cookie_dict['site'] + '; uid=' +cookie_dict['uid'] + '; ug=' +cookie_dict['ug'] +'; un=' +cookie_dict['un'] 
    #print(cookie_str)
    return cookie_str

