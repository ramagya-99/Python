from openpyxl import load_workbook

data_file = 'C:/Users/ramag/Downloads/EWR_SQL.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# Load one worksheet.
ws = wb['Sheet1']
all_column = list(ws.columns)

for column in all_column[2]:
    print(column.value)
