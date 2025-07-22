import fitz  # PyMuPDF
import requests
import json
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
API_KEY = os.getenv("GROQ_API_KEY")

# Constants
PDF_PATH = "IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

# Function to get questions from text using Groq
def generate_questions_from_text(text, page_num):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": f"Generate 5 multiple choice questions (with options and correct answer) from this Olympiad material:\n\n{text}"
                }
            ],
            "temperature": 0.7
        }

        response = requests.post(GROQ_ENDPOINT, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            print(f"[Page {page_num}] Error {response.status_code}: {response.text}")
            return None

    except Exception as e:
        print(f"[Page {page_num}] Exception: {e}")
        return None

# Open PDF and loop through pages
def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    all_questions = {}

    for i in range(len(doc)):
        page = doc.load_page(i)
        text = page.get_text()

        print(f"\nGenerating questions for Page {i + 1}...")

        if text.strip() == "":
            print(f"[Page {i + 1}] Skipped (empty page)")
            continue

        questions = generate_questions_from_text(text, i + 1)

        if questions:
            print(f"\nQuestions from Page {i + 1}:\n{questions}")
            all_questions[f"Page_{i+1}"] = questions
        else:
            print(f"[Page {i + 1}] Failed to generate questions.")

        # Optional: wait to avoid rate limits
        time.sleep(2)

    # Save all questions to a JSON file
    with open("output\generated_questions.json", "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=4, ensure_ascii=False)
        print("\nAll questions saved to 'generated_questions.json'.")

if __name__ == "__main__":
    process_pdf(PDF_PATH)
