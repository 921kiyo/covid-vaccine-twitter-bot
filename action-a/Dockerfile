FROM python:3.7-stretch
WORKDIR /app

RUN pip3 install -U pip setuptools wheel


COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# copy all source code
COPY . .
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]