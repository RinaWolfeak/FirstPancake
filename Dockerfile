FROM python:3
WORKDIR /source
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD config.py microblog.py .
ADD migrations ./migrations
ADD app ./app
CMD flask run -h 0.0.0.0