FROM ubuntu

RUN apt-get update && apt-get -y install python3-dev\
                    python3-pip
					

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./app /app


CMD [ "python3", "./app/main.py" ]
