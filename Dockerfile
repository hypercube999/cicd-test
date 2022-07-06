FROM python:3.8-alpine

COPY app/app.py /
COPY app/main.py /

COPY requirements.txt /
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
EXPOSE 8000
