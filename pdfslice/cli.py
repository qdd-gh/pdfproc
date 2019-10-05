import argparse
import pathlib


from pdfslice import slice


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=pathlib.Path)
    parser.add_argument("--prefix", type=str)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.prefix:
        prefix = args.prefix
    else:
        prefix = args.infile.stem

    outbase = args.infile.parent
    with args.infile.open(mode="rb") as infile:

        for pagenum, page in enumerate(slice.split(infile)):
            outfile = outbase / f"{prefix}-{pagenum}.pdf"
            page.write(outfile.open("wb"))
