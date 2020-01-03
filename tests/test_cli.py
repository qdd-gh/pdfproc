import pathlib
from typing import Generator, NamedTuple, BinaryIO

import pytest
from click.testing import CliRunner

from pdfproc import cli


class CorpusEntry(NamedTuple):
    file: BinaryIO
    pagecount: int


@pytest.fixture(scope="function", params=[("AV1611.pdf", 614), ("crazyones.pdf", 1)])
def corpus(shared_datadir: pathlib.Path, request) -> Generator[CorpusEntry, None, None]:
    filename, pagecount = request.param
    with (shared_datadir / filename).open("rb") as file:
        yield CorpusEntry(file, pagecount)


def test_cli_provides_help_output():
    runner = CliRunner()
    result = runner.invoke(cli.pdfslice, ["--help"])
    assert result.exit_code == 0
    assert result.output


def test_can_split_pdfs_from_cli(corpus: CorpusEntry):

    runner = CliRunner()
    with runner.isolated_filesystem():
        pathlib.Path("testfile.pdf").write_bytes(corpus.file.read())
        result = runner.invoke(cli.pdfslice, ["testfile.pdf", "testsplit"])
        assert result.exit_code == 0

        splitfiles = list(pathlib.Path(".").glob("testsplit*"))
        assert len(splitfiles) == corpus.pagecount


def test_cli_requires_output_prefix():

    runner = CliRunner()
    with runner.isolated_filesystem():
        pathlib.Path("test.pdf").write_bytes(b"just some nonsense")
        result = runner.invoke(cli.pdfslice, ["test.pdf"])
        assert result.exit_code != 0
