import pdfplumber
from PyPDF2 import PdfFileReader, PdfFileWriter

def lerPDF(pdf):
    with pdfplumber.open(pdf) as pdf:
        first_page = pdf.pages[0]
        conteudo = first_page.extract_text()
        return conteudo

def extrairPDFs(pdf, caminho):
    inputpdf = PdfFileReader(open(pdf, "rb"))
    #numeroArquivos = inputpdf.getNumPages()
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(f"{caminho}\\document-page{i}.pdf", "wb") as outputStream:
            output.write(outputStream)
    return True

def getNumeroPaginasPDF(pdf):
    inputpdf = PdfFileReader(open(pdf, "rb"))
    numeroPaginas = inputpdf.getNumPages()
    return numeroPaginas