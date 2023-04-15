from PyPDF2 import PdfReader

file_path = ('test1.pdf')

pdfReader = PdfReader(file_path)

numPages = len(pdfReader.pages)

text = ""

for pageNum in range(numPages):
    page = pdfReader.pages[pageNum]
    
    text += page.extract_text()
    
print(text)