# 📄 PDF to Question Generator

This project extracts text and images from a given PDF and then uses Groq's Mixtral model to generate meaningful questions based on the content.

---

## 🔧 Project Structure

```
.
├── extract_pdf_content.py         # Extracts images and text from the PDF
├── generate_questions.py         # Generates questions using Groq API
├── IMO class 1 Maths Olympiad.pdf # Sample input PDF
├── .env                          # Stores the Groq API key
├── .gitignore                    # Git ignored files and folders
├── output/
│   ├── images/ 
│   │   ├── page_1_img_1.png
│   │   ├── page_2_img_1.png
│   │   └── ...                   # Extracted page images
│   ├── generated_questions.json  # Contains generated questions from Groq
│   └── structured_content.json   # Stores extracted text per page
```

---

## 🧠 Features

- ✅ Converts all PDF pages into images.
- ✅ Extracts text from images using Tesseract OCR.
- ✅ Generates relevant questions using Groq’s Mixtral model.
- ✅ Saves both structured content and generated questions into JSON files.

---

## 📦 Requirements

Install the required Python packages using:

```bash
pip install pytesseract pdf2image openai python-dotenv
```

Additionally, make sure you have:

- **Tesseract OCR installed**  
  - For Windows: [Tesseract installer](https://github.com/tesseract-ocr/tesseract/wiki)
  - For Linux: `sudo apt install tesseract-ocr`
  - For Mac: `brew install tesseract`

- **Poppler installed** (needed for `pdf2image`)  
  - For Windows: Download from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
  - For Linux: `sudo apt install poppler-utils`
  - For Mac: `brew install poppler`

---

## 🔑 Environment Variables

Create a `.env` file in the root directory with the following content:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual API key.

---

## 🚀 How to Run

1. **Extract Text and Images from PDF**  
   This will extract each page as an image and apply OCR to extract structured text.

   ```bash
   python extract_pdf_content.py
   ```

2. **Generate Questions using Groq API**  
   This reads the structured text and produces questions stored in JSON.

   ```bash
   python generate_questions.py
   ```

3. **Check Outputs**  
   - `output/images/`: Contains all page images.
   - `output/structured_content.json`: Contains OCR text extracted from each page.
   - `output/generated_questions.json`: Contains AI-generated questions.

---

## 📌 Notes

- The project uses Groq’s **Mixtral** model via the OpenAI-compatible API.
- Make sure the `.env` file is properly configured and the API key is valid.
- Test PDF is already included as a sample.

---

## 📥 Example Output Format

### `structured_content.json`

```json
[
  {
    "page": 1,
    "text": "1 \n CLASS 1  SAMPLE PAPER 1  \n   SECTION -01   LOGICAL REASONI NG \n1. Find the next figures in the figure pattern given below.  \n  \n  \n [A]  \n [B]  \n [C]  \n [D]  \nAns. [D] \n \n2. Complete the number pattern.  \n  \n [A]  [B]"
  },
  {
    "page": 2,
    "text": "2 \n  [C]  [D]  \nAns [C]  \n \n3. In the questions given below, the series with one or more \nterms figures are missing marked with ‘?’ Choose the \ncorrect option to replace the ‘?’ mark(s).  \n \n [A] 19 [B] 18 \n [C] 17 [D] 20 \nAns [C]  \n \n4. Number of the groups of 9 paper clips ( ) shown here is  \n \n [A] 2 [B] 3 \n [C] 9 [D] 27 \nAns [D]  \n \n5. How many bananas are kept outside the basket?  \n \n [A] 1 [B] 2 \n [C] 3 [D] 4"
  }
]
```

### `generated_questions.json`

```json
{
  "page_1": [
    "What is the name of the shape shown in the figure?",
    "How many sides does a triangle have?"
  ],
  "page_2": [
    "What is 4 + 3?",
    "Identify the pattern in the series shown."
  ]
}
```

---

## 🛠️ Built With

- Python
- Tesseract OCR
- PDF2Image
- Groq API (Mixtral model)

---

## 📚 License

This project is for educational/demo purposes. Please cite appropriately if reused.

