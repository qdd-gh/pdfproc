# pdfslice

[![Build Status](https://travis-ci.org/qdd-gh/pdfslice.svg?branch=master)](https://travis-ci.org/qdd-gh/pdfslice)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
PDF splitting for Python

    >>> import pathlib
    >>> from pdfslice import slice
    >>> with open("big.pdf", "rb") as p:
    ...     for s in slice.filesplit(p, "someprefix"):
    ...          pathlib.Path(s.filename).write_bytes(s.page)
    ...
    >>> [print(p) for p in pathlib.Path(".").glob("someprefix*")]
    someprefix-1.pdf
    someprefix-2.pdf
    someprefix-3.pdf
    >>>

## Installation
### PyPI (Comming Soon!)
    $ pip install pdfslice
    
### Latest From GitHub Source
    $ pip install -e git+https://github.com/qdd-gh/pdfslice.git#egg=pdfslice
