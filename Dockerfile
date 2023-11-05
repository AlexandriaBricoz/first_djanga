FROM python:3.10

WORKDIR /usr/src/my_blog

COPY ./requirements.txt /usr/src/my_blog/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/my_blog

EXPOSE 8001

CMD [ "python", "manage.py","runserver","0.0.0.0:8001" ]