import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def evaluate_answer(question, answer):

    prompt = f"""
    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate:

    1. Technical Accuracy (0-10)
    2. Completeness (0-10)
    3. Communication (0-10)

    Also provide:
    - Strengths
    - Missing Points
    - Improved Answer

    Format clearly.
    """

    response = model.generate_content(prompt)

    return response.text