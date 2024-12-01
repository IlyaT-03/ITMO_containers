FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install tesseract-ocr -y
RUN pip install -r requirements.txt

VOLUME ["/app/logs"]

CMD ["python3", "src/bot.py"]