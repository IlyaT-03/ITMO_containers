FROM python:3.10.0

# Создание группы и пользователя для запуска приложения
RUN addgroup --system app && adduser --system --group app

WORKDIR /app

COPY requirements.txt .

# Установка библиотек
RUN apt-get update && apt-get install tesseract-ocr -y
RUN pip install --no-cache-dir -r requirements.txt

# Копирование папки с кодом
COPY src src

# Переключение на юзера
USER app

# volume (для логов)
VOLUME ["/app/logs"]

CMD ["python3", "src/bot.py"]