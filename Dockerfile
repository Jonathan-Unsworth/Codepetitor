FROM python:3

WORKDIR /usr/src/codepetitor

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=codepetitor.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0



CMD [ "flask", "run" ]