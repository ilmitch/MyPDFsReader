#extract information from perfomance pdfs through regex

import os
from fnmatch import fnmatch

import datetime as dt
import re
import PyPDF2

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# Listing available PDFs
root = "./"
pattern = "*.pdf"
files_lst = list()
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print(os.path.join(path, name))
            files_lst.append(os.path.join(path, name))
            
print(f'\n{len(files_lst)} .csv files found!\n')

# reading PDF text
aPDF = files_lst[0]
print(f"reading pdf: {aPDF}")

f = open(aPDF,'rb')
# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    
    page = pdf_reader.getPage(p)
    
    pdf_text.append(page.extractText())