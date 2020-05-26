FROM python:3
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install mysql-connector-python
WORKDIR /app/source

ENV FLASK_APP=app.py
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]