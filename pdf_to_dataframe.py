import pandas as pd
import numpy as np
import tabula #pip install tabula-py
import PyPDF2

dataframe = tabula.read_pdf("C:/Users/natka/Desktop/project_fpdf/5e62b38c-ee20-4951-830f-07e4e65a37ba.pdf"
                            ,pages = 9
                            # ,stream = True
                            ,multiple_tables = True)
new_df = pd.DataFrame(dataframe[0])
print(new_df)

first_col = new_df.columns
new_names = []
for i in first_col:
    new_names.append(new_df[i][1])
print(new_names)
fin_dataframe = pd.DataFrame(columns = new_names)
counter = 0
for i in first_col:
    fin_dataframe[new_names[counter]] = new_df[i][5:].reset_index(drop = True)
    counter += 1
print(fin_dataframe)