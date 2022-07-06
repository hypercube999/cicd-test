FROM python:3.8-alpine

COPY app/app.py /
COPY app/main.py /

COPY requirements.txt /
RUN pip install -r requirements.txt

EXPOSE 8000
ENV HOST="0.0.0.0"
ENTRYPOINT ["python", "./main.py"]
