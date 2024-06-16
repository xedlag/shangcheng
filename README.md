项目描述
该项目是一个使用 Django 作为后端和 React 作为前端的在线商城 Web 应用程序。该应用程序允许用户浏览和购买产品，管理购物车，并查看订单历史。它还包括用户账户管理功能，如注册、登录和个人资料管理。

安装
先决条件
Python 3.8 或更高版本
Node.js 14 或更高版本
Docker（可选，用于容器化部署）

后端（Django）

1、克隆仓库：
git clone https://github.com/xedlag/shangcheng.git
cd shangcheng/backend

2、创建虚拟环境并激活：
python -m venv venv
source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`

3、安装所需的包：
pip install -r requirements.txt

4、应用迁移并启动开发服务器：
python manage.py migrate
python manage.py runserver

前端（React）

1、导航到前端目录：
cd ../frontend

2、安装所需的包：
npm install

3、启动开发服务器：
npm start

Docker（可选）

1、构建并启动 Docker 容器：
docker-compose up --build

使用
访问 Django 后端：http://localhost:8000
访问 React 前端：http://localhost:3000

项目结构

store/

├── backend/

│   ├── manage.py

│   ├── online_store/

│   │   ├── __init__.py

│   │   ├── settings.py

│   │   ├── urls.py

│   │   ├── wsgi.py

│   ├── store/

│   │   ├── __init__.py

│   │   ├── admin.py

│   │   ├── apps.py

│   │   ├── models.py

│   │   ├── serializers.py

│   │   ├── tests.py

│   │   ├── urls.py

│   │   ├── views.py

├── frontend/

│   ├── public/

│   │   ├── favicon.ico

│   │   ├── index.html

│   │   ├── logo192.png

│   │   ├── logo512.png

│   │   ├── manifest.json

│   │   ├── robots.txt

│   ├── src/

│   │   ├── components/

│   │   │   ├── App.js

│   │   │   ├── Cart.js

│   │   │   ├── OrderHistory.js

│   │   │   ├── ProductList.js

│   │   ├── App.js

│   │   ├── index.js

│   ├── package.json

├── README.md


贡献指南
1、Fork 该仓库。
2、创建一个新分支（git checkout -b feature/your-feature-name）。
3、进行更改并提交（git commit -m 'Add some feature'）。
4、推送到分支（git push origin feature/your-feature-name）。
5、打开一个 Pull Request。

许可证
该项目根据 MIT 许可证授权 - 有关详细信息，请参阅 LICENSE 文件。
