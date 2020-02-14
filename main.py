from MyPDFsReader.readpdfs import list_pdf_files
from MyPDFsReader.readpdfs import read_pdfs

# example file showing how to use the list_pdf_files and read_pdfs functions

# listing pdf files in path directory
print('listing pdf files found in path directory:\n')
pdfs_lst = list_pdf_files(path="./input/pdf_new", pattern = "*.pdf")
print(pdfs_lst)
print('-'*72 + '\n')

# extracting text from pdfs list at path directory
## replace the path variable with your directory path contaninig pdf files
print('extracting text from pdfs list at path directory:\n')
pdfs_text = read_pdfs(path="./input/pdf_new", pattern = "*.pdf")
print(pdfs_text.keys())