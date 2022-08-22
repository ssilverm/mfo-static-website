from PyPDF2 import PdfFileReader

from pathlib import Path
pdf_path = ("space_plan_OPPORTUNITY_MFO2021-template_v1.pdf")
pdf = PdfFileReader(str(pdf_path))
