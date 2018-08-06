# file = open(r"C:\Users\ABCD FAMILY\Downloads\Experience-Electrical-Engineering-Resume.pdf\Experience Electrical Engineering Resume.pdf")
# file.read()
# file.close()

import PyPDF2
import re

object = PyPDF2.PdfFileReader(r"C:\Users\ABCD FAMILY\Downloads\Experience-Electrical-Engineering-Resume.pdf\Experience Electrical Engineering Resume.pdf")
page_nums = object.getNumPages()

String = "VOLUNTEER EXPERIENCE"

for i in range(0, page_nums):
    PageObj = object.getPage(i)
    print("page number " + str(i)) 
    Text = PageObj.extractText() 
    Search = re.search(String, Text)
    print(Search)