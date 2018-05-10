# 项目名称
video_course
<p>
 自动挂联通网络学院网课

# 项目目标
 自动获取课程列表，读取课程进度，跳过100%的课程，计算课程剩余时间（时间会多算一些）
 
 根据输入数量自动开启相应数量phantomJS浏览器同时挂网课，并自动保存进度，当课程完毕时先关闭对应的浏览器

<p>


# 使用方法
 由主程序入口调用程序，按提示操作
 
 需要输入账号密码，主题专栏的网址，以及根据弹出的验证码图片输入验证码，根据网络情况输入延迟信息，登录失败重新输入，失败五次结束程序
 
 根据搜索得到的课程数量，选择并行开启的数量，然后就可以挂机了...
 
 phantomJS开启过程可根据main所在目录下star.png查看开启的课程截图，进度保存过程可查看ing.png查看进度


# 请求方法

 Selenium模拟登录、在线计时
 
 requests抓取网页信息
 

# 其他方法

 BeautifulSoup网页解析
 
 PIL图片处理

# 作者信息
- cccccxw
- 2018-05-11 00:02:50

# 环境配置
## Ubuntu
### Python3的安装
```sh
# Python3 安装
sudo apt-get install python3
sudo apt-get intsall python3-pip

```

### 所需库
```sh

pip3 install requests
pip3 install selenium
pip3 install pillow
pip3 install bs4
pip3 install lxml

```
### chromdriver、phantomJS
安装可参考
https://blog.csdn.net/atwood_song/article/details/78764746


