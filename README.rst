.. image:: https://img.shields.io/travis/qdd-gh/pdfslice
    :target: https://travis-ci.org/qdd-gh/pdfslice

.. image:: https://img.shields.io/github/license/qdd-gh/pdfproc
    :target: https://github.com/qdd-gh/pdfproc/blob/master/LICENSE

.. image:: https://img.shields.io/readthedocs/pdfslice
    :target: https://pdfslice.readthedocs.io/en/latest/

.. image:: https://img.shields.io/codecov/c/gh/qdd-gh/pdfproc
    :target: https://codecov.io/gh/qdd-gh/pdfproc

pdfproc
========

PDF processing tools

.. code-block:: pycon

    >>> import pathlib
    >>> from pdfproc import slice
    >>> with open("big.pdf", "rb") as p:
    ...     for s in slice.filesplit(p, "someprefix"):
    ...          pathlib.Path(s.filename).write_bytes(s.page)
    ...
    >>> [print(p) for p in pathlib.Path(".").glob("someprefix*")]
    someprefix-1.pdf
    someprefix-2.pdf
    someprefix-3.pdf

Installation
------------

PyPI (coming soon!)
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ pip install pdfproc
    
Latest from GitHub source
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ pip install -e git+https://github.com/qdd-gh/pdfproc.git#egg=pdfproc
