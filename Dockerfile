from python:3.7.4

RUN mkdir /home/istheremilk/
COPY ./istheremilk/ /home/istheremilk/istheremilk/
COPY ./deploy/start.sh /

RUN python3.7 -m pip install uwsgi

RUN python3.7 -m pip install -r /home/istheremilk/istheremilk/requirements.txt

CMD ["/start.sh"]
