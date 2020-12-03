FROM python:3.7.9-stretch
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY . /app
CMD [ "python", "app.py" ]
