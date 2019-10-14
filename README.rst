########
pdfslice
########

.. image:: https://img.shields.io/travis/qdd-gh/pdfslice
    :alt: Travis (.org)

.. image:: https://img.shields.io/github/license/qdd-gh/pdfslice
    :alt: GitHub

PDF splitting for Python

.. code-block:: pycon

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

Installation
============
PyPI (comming soon!)
--------------------

.. code-block:: console

    $ pip install pdfslice
    
Latest from GitHub source
-------------------------

.. code-block:: console

    $ pip install -e git+https://github.com/qdd-gh/pdfslice.git#egg=pdfslice