# FirstPancake
docker run -it --name my-mysql -e MYSQL_ROOT_PASSWORD=123 -e MYSQL_DATABASE=my_flask_app mysql:5
docker run --name redis -p 6379:6379 redis:3-alpine
docker run -it --rm --link my-mysql -e 'DATABASE_URL=mysql+pymysql://root:123@my-mysql:3306/my_flask_app' -p 5000:5000 flask
                                     -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog
docker build . -t flask && docker run -it --rm flask ls
docker run -it --rm --link my-mysql --link redis:redis-server -e 'DATABASE_URL=mysql+pymysql://root:123@my-mysql:3306/my_flask_app' -e REDIS_URL=redis://redis-server:6379/0 -p 5000:5000 flask
docker run -it --name rq-worker --rm --link my-mysql --link redis:redis-server -e 'DATABASE_URL=mysql+pymysql://root:123@my-mysql:3306/my_flask_app' -e REDIS_URL=redis://redis-server:6379/0 flask rq worker -u redis://redis-server:6379/0 microblog-tasks
docker run -it --rm --link my-mysql -e 'DATABASE_URL=mysql+pymysql://root:123@my-mysql:3306/my_flask_app' flask flask db upgrade #миграция баз данных с добавлением переменной среды
(venv) $ flask db migrate -m "tasks"
(venv) $ flask db upgrade
docker run --name rq-worker -d --rm --link my-mysql --link redis:redis-server -e 'DATABASE_URL=mysql+pymysql://root:123@my-mysql:3306/my_flask_app' -e REDIS_URL=redis://redis-server:6379/0 flask worker -u redis://redis-server:6379/0 flask-tasks
Чтобы избежать проблем с кодировкой в 2.7
# -*- coding: utf-8 -*-
from __future__ import unicode_literals