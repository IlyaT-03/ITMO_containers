import cv2
import pytesseract
import numpy as np


def image_to_string(img_stream):
    image = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb).strip()
    if text != "":
        return text
    return "No text found"

