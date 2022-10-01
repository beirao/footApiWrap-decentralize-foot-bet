FROM python:3.8-slim

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
