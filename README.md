# FirstPancake
docker run -it --name my-mysql -e MYSQL_ROOT_PASSWORD=123 -e MYSQL_DATABASE=my_flask_app mysql:5
docker run -it --rm --link my-mysql -e 'DATABASE_URL=mysql+pymysql://root:123@my-mysql:3306/my_flask_app' -p 5000:5000 flask
docker build . -t flask && docker run -it --rm flask ls
