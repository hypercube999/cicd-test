FROM python:3.8

ADD app/app.py /
ADD app/main.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
EXPOSE 80:80