FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/project

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD sh -c "python3 manage.py collectstatic --noinput && python3 manage.py migrate; gunicorn --bind 0.0.0.0:8080 project.wsgi"
