#extract information from perfomance pdfs through regex

import os
import PyPDF2
from fnmatch import fnmatch


def list_pdf_files(path = "./", pattern = "*.pdf"):
    '''
    it returns a PDF files list found in the path folder/subfolders
    '''
    root = path
    files_lst = list()
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                print(os.path.join(path, name))
                files_lst.append(os.path.join(path, name))
                
    print(f'\n{len(files_lst)} .csv files found!\n')

    return files_lst

def read_pdfs(path = "./", pattern = "*.pdf"):
    '''
    it returns a dictiornary with each key corresponeding to a pdf file text
    input:  pdf filepaths list
    output: dictionary with pdfs text
    '''
    #getting files list
    print('Listing files..')
    files_lst = list_pdf_files(path, pattern)

    pdf_txt_dict = dict()

    print('Reading files text..')
    for file in files_lst:

        key = file.split('/')[-1].split('.pdf')[0] 

        with open(file,'rb') as f:
            print(f'Reading {file}')
            pdf_reader = PyPDF2.PdfFileReader(f)
            pdf_text = list()

            for p in range(pdf_reader.numPages):
                # List of every page's text.
                # The index will correspond to the page number.
                page = pdf_reader.getPage(p)
                pdf_text.append(page.extractText())

            pdf_txt_dict.update({key : pdf_text})

    print('Read all files!')

    return pdf_txt_dict