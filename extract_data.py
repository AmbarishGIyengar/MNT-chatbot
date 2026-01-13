import pytesseract
from pdf2image import convert_from_path
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

images = convert_from_path(
    "tamil.pdf",
    dpi=300,
    poppler_path=r"C:\poppler\poppler-25.12.0\Library\bin"
)

full_text = ""

for img in images:
    img = img.convert("L")  # grayscale helps OCR
    text = pytesseract.image_to_string(img, lang="tam")
    full_text += text + "\n"

# 👇 PUT THIS AT THE VERY END
with open("tamil_extracted.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Tamil text saved to tamil_extracted.txt")


