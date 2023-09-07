import fitz

file_path = "Gesetzesentwurf.pdf"


doc = fitz.open(file_path)

for page in doc:
    text = page.get_text()
    print(text)