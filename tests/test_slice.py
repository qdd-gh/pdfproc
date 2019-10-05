from io import BytesIO
import pathlib
from typing import NamedTuple, BinaryIO, Generator

import pytest

from pdfslice import slice


class CorpusEntry(NamedTuple):
    file: BinaryIO
    pagecount: int


@pytest.fixture(scope="function", params=[("AV1611.pdf", 614), ("crazyones.pdf", 1)])
def corpus(shared_datadir: pathlib.Path, request) -> Generator[CorpusEntry, None, None]:
    filename, pagecount = request.param
    with (shared_datadir / filename).open("rb") as file:
        yield CorpusEntry(file, pagecount)


def test_splitting_produces_all_pages(corpus):

    counter = 0
    for _, page in slice.split(infile=corpus.file):
        counter += 1
        page.close()

    assert counter == corpus.pagecount
