# import requests

# r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')

# print(r)

# print(r.content)

# from pypdf import PdfReader

# reader = PdfReader('My_Resume.pdf')
# print(len(reader.pages))


# page = reader.pages[0]
# print(page.extract_text())


#Extracting text from pdf 

# import pypdf 

# reader = pypdf.PdfReader('My_Resume.pdf')

# print(len(reader.pages))

# data = reader.pages[0]

# print(data.extract_text())











import pypdf

reader = pypdf.PdfReader('My_Resume.pdf')

print(len(reader.pages))

data = reader.pages[0]

print(data.extract_text())