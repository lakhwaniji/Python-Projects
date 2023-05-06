from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
df=pd.read_csv("topics.csv")
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_text_color(100,100,100)
    pdf.set_font(family="Times",style="B",size=24)
    pdf.cell(w=0,h=24,txt=row["Topic"],align="L")
    pdf.line(10,31,200,31)
    for i in range(0,25):
        pdf.line(10,41+(i*10),200,41+(i*10))
    pdf.ln(270)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
    for i in range(row["Pages"]-1):
        pdf.add_page()
        for i in range(0, 27):
            pdf.line(10, 21 + (i * 10), 200, 21 + (i * 10))
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
pdf.output("result.pdf")

