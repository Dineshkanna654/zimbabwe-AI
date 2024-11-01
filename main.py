from Components.order_spell import correct_mistaken_file
from Components.DateFormat import standardize_date
import pandas as pd

# Now you can use the function
correct_mistaken_file('SOA_Reff_num.csv', 'Diff format.csv', 'corrected_mistaken_file.csv')

file_path = 'corrected_mistaken_file.csv'
df = pd.read_csv(file_path)

df['Date'] = df['Date'].apply(standardize_date)

df.to_csv('corrected_mistaken_file.csv', index=False)

print(df.columns)


