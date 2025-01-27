FROM python:3.9-slim

ENV TZ=Asia/Tokyo

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/app.py"]