<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_web_server/readme/README.zh-hant.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_web_server

- [简体中文](../README.md)
- [繁體中文](README.zh-hant.md)
- [English](README.en.md)

## 說明

xy-web-service服務模組。

## 程式碼庫

- <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-opensource/xy_web_server.git" target="_blank">Gitee位址</a>  
- <a href="https://gitcode.com/xy-opensource/xy_web_server.git" target="_blank">GitCode位址</a>  

## 安裝

```bash
# bash
pip install xy_web_server
```

## 使用

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

## Web服務開發

### 1. 創建專案
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

### 2. 接入Django服務和Django-ORM, Tornado

> 具體請參考 [Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py)

#### 1. 加載Django設定

> <b>注意: </b> 載入Django要在引入Tornado的RequestHandler早, 這樣才能夠在Tornado的RequestHandler中調用Django的模型
```python
# Runner.py
admin_path = Path.cwd().joinpath("source/Runner/Admin/").resolve().as_posix()
sys.path.insert(0, admin_path)
# 若需要使用Django-orm调用该函数
Django().load("xy_web_server_demo.settings")
```

#### 2. 接取manage.py管理

[Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py) 檔案中的django_manage方法等同於

```bash
# bash
# ../samples/xy_web_server_demo/source/Runner/Admin/manage.py
python manage.py 後續參數...
```


例如: 
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

#### 3. 啟動Django服務

> <b>注意: </b> 後台使用者名稱: root 密碼: 1

[Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py) 檔案中的 django_start 方法等同於
```bash
# ../samples/xy_web_server_demo/source/Runner/Admin/manage.py
python manage.py runserver 127.0.0.1:8401
```

例如: 
```bash
# bash
xy_web_server -w django start
#相当于

cd xy_web_server_demo/source/Runner/Admin

python manage.py runserver 127.0.0.1:8401
```

#### 4. 啟動Tornado服務

[Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py) 檔案中的 tornado_start 方法
```bash
# bash
xy_web_server -w tornado start
```

## 許可證
xy_web_server 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  
![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```