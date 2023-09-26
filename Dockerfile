FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app/

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
