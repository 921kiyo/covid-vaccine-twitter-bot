FROM python:3.7-stretch

RUN pip3 install -U pip setuptools wheel
# copy all source code
COPY . .
RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]