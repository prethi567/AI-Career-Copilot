import pytesseract
from PIL import Image
import pdf2image
import os

# Tell pytesseract where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\prethi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def extract_resume_text(resume_file):
    text = ""

    # Get file extension
    file_extension = os.path.splitext(resume_file.name)[1].lower()

    # If PDF file
    if file_extension == ".pdf":
        images = pdf2image.convert_from_bytes(resume_file.read())

        for image in images:
            text += pytesseract.image_to_string(image)

    # If image file
    elif file_extension in [".png", ".jpg", ".jpeg"]:
        image = Image.open(resume_file)
        text = pytesseract.image_to_string(image)

    return text
