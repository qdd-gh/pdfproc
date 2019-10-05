import PyPDF2 as pypdf


def split(infile):
    pdf = pypdf.PdfFileReader(infile)

    for pagenum in range(pdf.getNumPages()):
        writer = pypdf.PdfFileWriter()
        writer.addPage(pdf.getPage(pagenum))
        yield writer
