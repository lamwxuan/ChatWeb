# 包管理
## 生成requirements.txt文件
1. 安装pipreqs库:  pip install pipreqs
2. 在项目目录使用生成 pipreqs ./ --encoding=utf8 --force
# 通过requirements.txt 导入包
pip3 install -r requirements.txt

# Web application Run and Deploy

<!-- deploy and run in server-->
this webApp is successfully use in pytyon3.10, windows10
1. 在服务器上安装pyinstaller -- pip install pyinstaller
2. pyi-makespec -D manage.py
3. 在.spec文件，中的hiddenimports加入项目的settings的INSTALLED_APPS
4. pyinstaller manage.spec 
5. ./manage runserver 0.0.0.0:6788 --noreload ---run application locally


# User Guide
1.firstly use this webApp need to amend the config.json to input your own apiKey
2.in the chatbox, you can input '###' to clear all msg history


## Django study
[//]: # (create django project -- 在目标目录下运行)
D:\0NotInstall\python3.10\Scripts\django-admin startproject financialWeb
![img.png](img.png)

D:\0NotInstall/python3.10/python.exe manage.py startapp app01

[//]: # (add app01 to djson project)
add app01 to ./settings.py -> INSTALLED_APPS = ['app01.apps.App01Config']

[//]: # (run django project CMD)
python manage.py runserver 0.0.0.0:80
nohup python3 manage.py runserver 0.0.0.0:8081 > /home/code/python/djangoWeb.log  2&>1 &

## 查看防火墙设置
sudo ufw status
ufw allow 8081


Referrence:
websocket Setup : https://channels.readthedocs.io/en/stable/installation.html
LayIM: http://layui.org.cn/fly/docs/7.html#tool