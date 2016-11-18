Django-Nginx-Dotmap 流量展示
====

[![versions](https://img.shields.io/pypi/pyversions/Django.svg)](https://www.python.org/)
[![versions](https://img.shields.io/badge/Django-v1.10-green.svg)](https://www.djangoproject.com/)
[![versions](https://img.shields.io/badge/Echarts%20-v3.0-brightgreen.svg)](http://echarts.baidu.com/)


- 通过collection.py采集分析Nginx的日志文件，转换为JSON接口....
  - 采用百度Echarts图标插件生成地图.
  - 采用百度IP查询接口（IP转城市）
  - 采集程序定期分析数据并入库
  - 后台API接口（JSON）
  - 前端采用Ajax异步调用（刷新数据）


## 安装部署

1. 通过pip进行需求环境的安装

   ```
   pip install -r requirement.txt
   ``` 
   
2. 采集程序采集数据

   ```
   python collection.py
   ```
   
3. 数据接口

   ```
   http://127.0.0.1/data/20161118/
   ```

   
4. 启动测试Web服务

   ```
   python manage.py runserver
   ```
   
5. 浏览器

   ```
   http://127.0.0.1:8000
   ```


   
## 效果图
![promisechains](https://raw.githubusercontent.com/Leon2018/dotmap/master/%E6%95%88%E6%9E%9C%E5%9B%BE.png)

