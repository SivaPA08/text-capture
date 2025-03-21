import os
from PIL import Image
import pytesseract as pt
import pyperclip

class Text:
    def __init__(self):
        pass

    @staticmethod
    def extract_text():
        
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, "..", "screenshot.png")
        
        img = Image.open(path)
    
        text = pt.image_to_string(img)
        pyperclip.copy(text)
        print("Extracted text copied to clipboard.")
