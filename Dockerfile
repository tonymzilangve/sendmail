FROM python:2.7
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /usr/src/app

COPY .requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./emailp2

CMD [ "python",  "manage.py", "runserver", "0.0.0.0:8000"]