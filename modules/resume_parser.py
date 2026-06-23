import fitz  # PyMuPDF

# Skills Database
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


def extract_text(pdf_path):
    """
    Extract text from PDF using PyMuPDF.
    Works on Streamlit Cloud and local machine.
    """

    text = ""

    try:
        pdf = fitz.open(pdf_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except Exception as e:
        print("PDF Extraction Error:", e)

    return text


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    detected = []

    text = text.lower()

    for skill in SKILLS_DB:

        if skill.lower() in text:
            detected.append(skill)

    return sorted(list(set(detected)))