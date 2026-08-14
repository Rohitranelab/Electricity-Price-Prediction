FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP app.py

CMD ["flask", "run", "--port=0.0.0.0", "--port=5000"]