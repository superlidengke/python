# need pandas and xlrd
import pandas as pd
# Assign spreadsheet filename to `file`
file = r"C:\Users\UC212310\Desktop\work\ESG\18592_2017_20180423_030645.xlsx"

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet')

for index,row in df1.iterrows():
    print(row[0])
    print(row['DP Code'])
    break

#the index of every row
for i in df1.index:
    print(i)
    break
#all column name
for column in df1.columns:
    print(column)
    break
#read one column
for code in df1['DP Code']:
    print(code)
    break