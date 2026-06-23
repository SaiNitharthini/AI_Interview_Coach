import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("API KEY FOUND:", api_key is not None)
print("API KEY VALUE:", api_key[:10] + "..." if api_key else "None")
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_questions(resume_text, skills):

    prompt = f"""
    Candidate Skills:
    {', '.join(skills)}

    Resume Summary:
    {resume_text[:2000]}

    Generate:

    5 Technical Interview Questions

    3 HR Interview Questions

    2 Project-Based Questions

    Format clearly with numbering.
    """

    response = model.generate_content(prompt)

    return response.text