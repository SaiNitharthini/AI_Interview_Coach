import fitz
import pytesseract
from PIL import Image
import io

# Update this if your path differs
pytesseract.pytesseract.tesseract_cmd = (
    r"D:\Tesseract-OCR\tesseract.exe"
)

def extract_text(pdf_path):

    text = ""

    pdf = fitz.open(pdf_path)

    for page in pdf:

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        img_bytes = pix.tobytes("png")

        image = Image.open(io.BytesIO(img_bytes))

        page_text = pytesseract.image_to_string(image)

        text += page_text + "\n"

    pdf.close()

    return text
SKILLS_DB = [
    "python",
    "java",
    "c",
    "c++",
    "mysql",
    "milvus",
    "html",
    "css",
    "javascript",
    "flask",
    "git",
    "github",
    "figma",
    "blender",
    "canva",
    "gimp",
    "computer vision",
    "machine learning",
    "deep learning",
    "data structures",
    "algorithms",
    "operating systems",
    "computer networks",
    "cybersecurity"
]

def extract_skills(text):

    detected = []

    text = text.lower()

    for skill in SKILLS_DB:

        if skill.lower() in text:

            detected.append(skill)

    return list(set(detected))