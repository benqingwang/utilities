# pip install pandas openpyxl

import pandas as pd

# Path to the Excel file
file_path = 'path_to_your_file.xlsx'

# Load Excel file
xlsx = pd.ExcelFile(file_path)

# List to hold data from each sheet
dfs = []

# Loop through the sheets
for sheet_name in xlsx.sheet_names:
    df = pd.read_excel(xlsx, sheet_name=sheet_name)
    # Optionally, add a column to indicate the source sheet
    df['Source'] = sheet_name
    dfs.append(df)

# Concatenate all dataframes into a single dataframe
combined_df = pd.concat(dfs, ignore_index=True)

# Show the combined DataFrame
print(combined_df)
