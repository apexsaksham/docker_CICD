FROM python:3.13.3

WORKDIR /app

COPY randompass.py .

CMD [ "python", "randompass.py" ]
