import cv2
import asyncio
from io import BytesIO
from aiogram import types
import numpy as np
import hashlib
import OCR
import db



def process_image(img_stream, message):

    image = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)

    hash_value = hashlib.sha256(image.view(np.uint8)).hexdigest()
    in_db, text = db.search(hash_value)

    if in_db:
        return text

    text = OCR.image_to_string(image).strip()

    db.add(message.from_user.id, hash_value, text, message.date)

    if text != "":
        return text
    return "No text found"

