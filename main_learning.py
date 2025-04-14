import os
from fpdf import FPDF

#Create pdf file object with parameters defined in the implem library file
testpdf = FPDF(orientation='P', unit= 'mm', format='A4')

testpdf.add_page()

testpdf.set_font(family='Times', style='B', size=12)

#ln means a line break (\n). If it is 1, then there is 1 line break, 2...
#w is width of the cell. If it is 0, it extends to the end of the pages, 
# if it is a value, it extends to a certain value. 
#border=1 creates a border

testpdf.cell(w=0, h=12, txt="Hello there!", 
             align='L', ln=1)
testpdf.cell(w=0, h=12, txt="Hi there...", 
             align='L', ln=1)

#call output method from fpdf object instance named testpdf
#output method returns a pdf file in the directory where the script is located
#takes as a parameter the name of the pdf file with the file type in string format  
#output is called after pdf file object is created and configured
testpdf.output("testpdf.pdf")

print("done")


