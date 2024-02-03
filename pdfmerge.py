
from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["python1.pdf", "python.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()