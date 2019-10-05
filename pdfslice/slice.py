from io import BytesIO
from typing import BinaryIO, Generator, NamedTuple

import PyPDF2 as pypdf


class Page(NamedTuple):
    number: int
    page: BytesIO


def split(infile: BinaryIO) -> Generator[Page, None, None]:

    pdf = pypdf.PdfFileReader(infile)

    for pagenum in range(pdf.getNumPages()):
        writer = pypdf.PdfFileWriter()
        writer.addPage(pdf.getPage(pagenum))

        page = BytesIO()
        writer.write(page)
        page.seek(0)

        yield Page(pagenum + 1, page)
