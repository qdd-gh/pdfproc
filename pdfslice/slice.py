import pathlib
from io import BytesIO
from typing import BinaryIO, Generator

import PyPDF2 as pypdf
import attr


@attr.s(frozen=True)
class Page:
    """A single PDF page ready for further processing"""

    number = attr.ib(type=int)
    page = attr.ib(type=BytesIO)


@attr.s(frozen=True)
class PageFile:
    """A single PDF page for use in file I/O"""

    filename = attr.ib(type=pathlib.Path)
    page = attr.ib(type=BytesIO)


def split(infile: BinaryIO) -> Generator[Page, None, None]:
    """Split an entire PDF into its constituent pages.

    :param infile: An open binary stream containing the original PDF.

    :return: Yields `Pages`
    """
    pdf = pypdf.PdfFileReader(infile)

    for pagenum in range(pdf.getNumPages()):
        writer = pypdf.PdfFileWriter()
        writer.addPage(pdf.getPage(pagenum))

        page = BytesIO()
        writer.write(page)
        page.seek(0)

        yield Page(number=pagenum + 1, page=page)


def filesplit(infile: BinaryIO, prefix: str) -> Generator[PageFile, None, None]:
    """ Split the entire original PDF and prepare it for writing back to disk.

    The PageFile type that is returned contains all the information necessary
    to write each split page back out to disk.

    :param infile: An open binary IO stream containing the original PDF.
    :param prefix: The file name (may include a path) that will be used for each split.
        The split's page number and the ".pdf" extension will be added to this prefix.

    :return: Yields PageFiles
    """
    for page in split(infile):
        filename = pathlib.Path(f"{prefix}-{page.number}.pdf")
        yield PageFile(filename=filename, page=page.page)
