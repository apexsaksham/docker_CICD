FROM python:3.13.3

WORKDIR /app

COPY myproject/randompass.py .

CMD [ "python", "randompass.py" ]
