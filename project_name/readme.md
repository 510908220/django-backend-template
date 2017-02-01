# django开发模板



## 启动django
#### 设置数据库容器
```
docker run --name db -v /var/lib/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=asheashe -d -p 3306:3306 mysql
```
#### 开发模式
- 创建数据库:`/config/mysql/app.sql`
- http://stackoverflow.com/questions/8940230/how-can-i-run-a-sql-text-file-on-a-mysql-database
- 在`docker-compose.yml`目录下执行:`docker-compose up -d`

#### 线上部署

