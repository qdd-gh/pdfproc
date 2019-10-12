import typing

import click

from pdfslice import slice


@click.command()
@click.argument("infile", type=click.File("rb"))
@click.argument("prefix", type=click.STRING)
def pdfslice(infile: typing.BinaryIO, prefix: str):

    for split in slice.filesplit(infile, prefix):
        split.filename.write_bytes(split.page.read())
