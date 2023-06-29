import glob
from datetime import date

import pandas as pd
from pathlib import Path
from fpdf import FPDF

filepaths = glob.glob("Invoices/*.xlsx")
for filepath in filepaths:
    filename = Path(filepath).stem
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    df = pd.read_excel(filepath)
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=16, txt=f"Invoice No -: {filename.split('-')[0]}", ln=1)
    pdf.cell(w=0, h=16, txt=f"Date -: {date.today()}", ln=1)
    col = list(df.columns)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.cell(w=30, h=12, txt=col[0], border=1, align="C")
    pdf.cell(w=60, h=12, txt=col[1], border=1, align="C")
    pdf.cell(w=30, h=12, txt=col[2], border=1, align="C")
    pdf.cell(w=30, h=12, txt=col[3], border=1, align="C")
    pdf.cell(w=30, h=12, txt=col[4], border=1, ln=1, align="C")
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=8)
        pdf.cell(w=30, h=12, txt=str(row["product_id"]), border=1, align="C")
        pdf.cell(w=60, h=12, txt=str(row["product_name"]), border=1, align="C")
        pdf.cell(w=30, h=12, txt=str(row["amount_purchased"]), border=1, align="C")
        pdf.cell(w=30, h=12, txt=str(row["price_per_unit"]), border=1, align="C")
        pdf.cell(w=30, h=12, txt=str(row["total_price"]), border=1, ln=1, align="C")
    total_sum=df["total_price"].sum()
    pdf.cell(w=30, h=12, border=1, align="C")
    pdf.cell(w=60, h=12, border=1, align="C")
    pdf.cell(w=30, h=12, border=1, align="C")
    pdf.cell(w=30, h=12, border=1, align="C")
    pdf.cell(w=30, h=12, txt=str(total_sum), border=1, ln=1, align="C")
    pdf.set_font(family="Times", style="B", size=16)

    pdf.cell(w=0, h=16, txt=f"The Total due amount is -- {total_sum}", ln=1)

    pdf.output(f"Invoices_Pdf/{filename}.pdf")
