import os
from PIL import Image
import pytesseract as pt
import pyperclip

class Text:
    def __init__(self):
        pass

    @staticmethod
    def extract_text():
        # Get the directory where get_text.py lives
        current_dir = os.path.dirname(__file__)
        # Build the path to screenshot.png (one level up)
        image_path = os.path.join(current_dir, "..", "screenshot.png")
        
        # Now open that image
        img = Image.open(image_path)
        
        # Extract text via OCR
        text = pt.image_to_string(img)
        pyperclip.copy(text)
        print("Extracted text copied to clipboard.")
