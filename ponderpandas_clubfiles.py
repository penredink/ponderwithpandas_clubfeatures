import os
import pandas as pd

# Create early binding
df_clubbed = pd.DataFrame()
# Iterate through the default directory
for an_item in os.scandir():
    # Check if is an Excel file
    if an_item.is_file() and str(an_item).__contains__("xlsx"):
        print(f"Clubbing file {an_item}...")
        # Read each Excel file
        df1 = pd.read_excel(an_item)
        # When axis = 0, columns are clubbed one after the other
        df_clubbed = pd.concat([df_clubbed, df1], axis=0)
# Write the final file
print("Writing 'the_final.xlsx'...")
df_clubbed.to_excel("the_final.xlsx", index=False)


