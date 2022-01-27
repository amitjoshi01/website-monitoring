FROM python:3.7.5-buster
COPY requirements.txt /opt/requirements.txt
COPY request.py /opt/request.py
WORKDIR /opt
RUN apt-get update && python -m pip install -r requirements.txt 
CMD ["python", "./request.py"]
