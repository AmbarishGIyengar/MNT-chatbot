import unicodedata
import regex as re

# Read extracted text
with open("tamil_extracted.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1️⃣ Unicode normalization (VERY IMPORTANT)
text = unicodedata.normalize("NFC", text)

# 2️⃣ Remove extra spaces
text = re.sub(r"\s+", " ", text)

# 3️⃣ Fix common OCR junk (safe rules only)
text = re.sub(r"[•■◆]", "", text)

# 4️⃣ Restore paragraph breaks
text = re.sub(r"(Q\d+\.)", r"\n\n\1", text)

# Save cleaned text
with open("tamil_cleaned.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaned Tamil text saved to tamil_cleaned.txt")
