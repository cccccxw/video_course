#!/usr/bin/python3
# -*- coding: utf-8 -*-
#主函数入口

from module.do_run import do_run

try_time = 5
title_url = str(input("请复制专区网址："))
user_name = str(input("请输入账号："))
user_pwd = str(input("请输入密码："))
delay = float(input("网络延迟情况，数字越小延迟越低，默认为1，可以小数："))

while do_run(title_url,user_name,user_pwd,delay):
    print("登录失败了...")
    title_url = str(input("请复制专区网址："))
    user_name = str(input("请输入账号："))
    user_pwd = str(input("请输入密码："))
    delay = float(input("网络延迟情况，数字越小延迟越低，默认为1，可以小数："))
    try_time = try_time - 1
    if try_time:
        print("尝试次数过多...")
        break
