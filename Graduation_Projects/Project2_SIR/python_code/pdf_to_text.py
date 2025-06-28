from pypdf import PdfReader

reader = PdfReader("/Users/adel/Documents/Project2_Sir/x.pdf")
number_of_pages = len(reader.pages)

pdf_text = ""

for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    if text:
        pdf_text += text.encode('utf-8', 'ignore').decode('utf-8')

print(pdf_text)  # Prints the full extracted text
