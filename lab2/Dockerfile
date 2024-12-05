FROM python:3.10.0

WORKDIR /app

COPY requirements.txt .

# Установка библиотек
RUN apt-get update && apt-get install tesseract-ocr -y
RUN pip install --no-cache-dir -r requirements.txt

# Копирование папки с кодом
COPY src src

CMD ["python3", "src/bot.py"]
