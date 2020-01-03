import typing

import click

from pdfproc import slice


@click.command()
@click.argument("infile", type=click.File("rb"))
@click.argument("prefix", type=click.STRING)
def pdfslice(infile: typing.BinaryIO, prefix: str) -> None:
    """Split an N-page PDF into N individual PDFs.

    e.g., INFILE.pdf -> [PREFIX-1.pdf, PREFIX-2.pdf, ..., PREFIX-N.pdf]
    \f

    :param infile: An open file-like object containing the original PDF
    :param prefix: The base name used for each output file. Does not include the file extension
    """
    for split in slice.filesplit(infile, prefix):
        split.filename.write_bytes(split.page.read())
