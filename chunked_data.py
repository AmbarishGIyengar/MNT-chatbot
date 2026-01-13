import re
import json

# Read the cleaned Tamil text
with open("tamil_extracted.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split based on question numbers (01., 02., etc.)
parts = re.split(r"(?:^|\n)\s*(\d+\.)", text)
chunks = []
current_q = None

for part in parts:
    if re.match(r"\d{2}\.", part):
        current_q = part
    else:
        if current_q:
            chunk = (current_q + " " + part).strip()
            if len(chunk) > 80:   # avoid tiny junk chunks
                chunks.append(chunk)

# Save chunks to JSON
with open("tamil_chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print(f"Created {len(chunks)} chunks")
