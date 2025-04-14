import os
from fpdf import FPDF
import pandas as pd


pdf_data = pd.read_csv('topics.csv', sep=';')
# print(f"\n\n{pdf_data}\n\n")

#put the Dataframe object into a dictionary/set that has topic string
#better way to do it than a nested for loop?
for index, data in pdf_data.iterrows:
    pass


#Create pdf file object with parameters defined in the implem library file
refbook_pdf = FPDF(orientation='P', unit= 'mm', format='A4')

refbook_pdf.add_page()

refbook_pdf.set_font(family='Times', style='B', size=12)

refbook_pdf.cell(w=0, h=12, txt="Hello there!", 
             align='L', ln=1)
refbook_pdf.cell(w=0, h=12, txt="Hi there...", 
             align='L', ln=1)

refbook_pdf.output("refbook_pdf.pdf")

print("done")


