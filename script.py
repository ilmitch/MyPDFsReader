#extract information from perfomance pdfs through regex

import os
from fnmatch import fnmatch

import datetime as dt
import re
import PyPDF2

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

root = "./"
pattern = "*.pdf"
files_lst = list()
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print(os.path.join(path, name))
            files_lst.append(os.path.join(path, name))
            
print(f'\n{len(files_lst)} .csv files found!\n')