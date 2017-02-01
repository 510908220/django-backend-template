# django开发模板



## 启动django
#### 设置数据库容器
```
docker run --name db -v /var/lib/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=asheashe -d -p 3306:3306 mysql
```
#### 开发模式
- 创建数据库:`/config/mysql/app.sql`
- 在`docker-compose.yml`目录下执行:`docker-compose up -d`

#### 线上部署

- 创建数据库:`/config/mysql/app.sql`
- 在`docker-compose.prod.yml`目录下执行:`docker-compose -f docker-compose.prod.yml up -d`