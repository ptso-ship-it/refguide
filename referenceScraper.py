from docx import Document


file = 'Reference_Clean.docx'
text = Document(file)

text = text.paragraphs[0].text

ls = []

import re
def GetTheSentences(infile):
    for result in re.findall('##Start(.*?)##End', text, re.S):
        ls.append(result)

GetTheSentences(text)


country = []


for x in ls:
	countryname = re.findall('#Country:(.*?)Tax authority and relevant transfer pricing ', x, re.S)
	country.append(countryname)


import csv
import numpy

with open('test.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    for word in country:
        mywriter.writerow([word])