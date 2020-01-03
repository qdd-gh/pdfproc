"""PDF splitting for Python"""

from datetime import date
import os

__version__ = os.environ.get("PDFPROC_VERSION", date.today().strftime("%Y.%m.%d"))
