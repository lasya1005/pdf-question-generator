import json
import os
from PyPDF2 import PdfReader

pdf_path = "IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
output_path = os.path.join("output", "structured_content.json")

os.makedirs("output", exist_ok=True)

reader = PdfReader(pdf_path)
structured_content = []

for page_num, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        structured_content.append({
            "page": page_num + 1,
            "text": text.strip()
        })

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(structured_content, f, indent=2)

print(f">> Extracted content saved to {output_path}")
