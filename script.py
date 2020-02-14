#extract information from perfomance pdfs through regex

import os
import re
import PyPDF2
from fnmatch import fnmatch


def list_pdf_files(root = "./", pattern = "*.pdf"):
    '''
    it returns PDF files list at root directory
    '''
    files_lst = list()
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                print(os.path.join(path, name))
                files_lst.append(os.path.join(path, name))
                
    print(f'\n{len(files_lst)} .csv files found!\n')

    return files_lst

def read_pdfs(pdf_lst):
    '''
    it returns a dictiornary with each key corresponeding to a pdf file text
    input:  pdf filepaths list
    output: dictionary with pdfs text
    '''

    pdf_txt_dict = dict()

    for file in files_lst:

        key = file.split('/')[1].split('.pdf')[0] 
        # f = open(file,'rb')
        # pdf_reader = PyPDF2.PdfFileReader(f)
        with open(file,'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)

            pdf_text = list()

            for p in range(pdf_reader.numPages):
                # List of every page's text.
                # The index will correspond to the page number.
                page = pdf_reader.getPage(p)
                pdf_text.append(page.extractText())
                print(f"Page txt: {page.extractText()}")

            pdf_txt_dict.update({key : pdf_text})

    return pdf_txt_dict

# Listing available PDFs
files_lst = list_pdf_files()
# reading PDF text
pdf_txt_dict = read_pdfs(pdf_lst=files_lst)