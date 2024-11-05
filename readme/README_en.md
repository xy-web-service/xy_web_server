<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_web_server/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_web_server

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

xy-web-service Server module.

## Source Code Repositories

- <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-opensource/xy_web_server.git" target="_blank">Gitee</a>  
- <a href="https://gitcode.com/xy-opensource/xy_web_server.git" target="_blank">GitCode</a>  

## Installation

```bash
# bash
pip install xy_web_server
```

## How to use

```bash
# bash
xy_web_server -c project -n xy_web_server_demo
# 创建项目 [ xy_web_server_demo ] 成功!!!
# 项目路径 ==>>> /mnt/bs-media/Workspace/project/opensource/xy-web-service/xy_web_server/test/xy_web_server_demo

cd xy_web_server_demo
xy_web_server
# >>>>>>>>>>>> xy_web_server - v1.0.1 <<<<<<<<<<<<<
#
# xy_web_server_demo Hello World!!!
```


> <b>提示: </b> 运行Tornado与Django web服务请参考 [案例](../samples/xy_web_server_demo)

## Web Service Development

### 1. Create Project
```bash
# bash
xy_web_server -c project -n xy_web_server_demo
# 创建项目 [ xy_web_server_demo ] 成功!!!
# 项目路径 ==>>> /mnt/bs-media/Workspace/project/opensource/xy-web-service/xy_web_server/test/xy_web_server_demo

cd xy_web_server_demo
xy_web_server
# >>>>>>>>>>>> xy_web_server_demo - v1.0.1 <<<<<<<<<<<<<
#
# xy_web_server_demo Hello World!!!
```

### 2. Import Django service and Django-ORM, Tornado

> For details, please refer to [Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py)

#### 1. Load Django settings

> <b>Tip: </b>  Load Django before importing Tornado's RequestHandler, so that you can call Django's model in Tornado's RequestHandler

```python
# Runner.py
admin_path = Path.cwd().joinpath("source/Runner/Admin/").resolve().as_posix()
sys.path.insert(0, admin_path)
# 若需要使用Django-orm调用该函数
Django().load("xy_web_server_demo.settings")
```

#### 2. Access manage.py management

The django_manage method in the [Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py) file is equivalent to
```bash
# bash
# ../samples/xy_web_server_demo/source/Runner/Admin/manage.py
python manage.py Subsequent parameters ...
```

For example:
```bash
# bash
xy_web_server -w django shell
#相当于

cd xy_web_server_demo/source/Runner/Admin

python manage.py shell

#############################################################################
# 同步数据表, 在每次启动服务之前需要同步数据表
xy_web_server -w django makemigrations
xy_web_server -w django migrate

```

#### 3. Start the Django service

> <b>Tip: </b> Admin Username: root  Password: 1

The django_start method in the [Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py) file is equivalent to
```bash
# bash
python manage.py runserver 127.0.0.1:8401
```

For example:
```bash
# bash
xy_web_server -w django start
#相当于

cd xy_web_server_demo/source/Runner/Admin

python manage.py runserver 127.0.0.1:8401
```

#### 4. Start Tornado service

The tornado_start method in the [Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py) file is equivalent to
```bash
# bash
xy_web_server -w tornado start
```


## License
xy_web_server is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  
![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```