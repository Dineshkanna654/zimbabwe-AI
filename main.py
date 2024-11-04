from Components.order_spell import correct_mistaken_file
from Components.DateFormat import standardize_date
import pandas as pd

# arrange the correct order and spell correct 
correct_mistaken_file('SOA_Reff_num.csv', 'Diff format.csv', 'corrected_mistaken_file.csv')

# Fix the Date in only one format
file_path = 'corrected_mistaken_file.csv'
df = pd.read_csv(file_path)

df['Date'] = df['Date'].apply(standardize_date)

# save the final csv file
df.to_csv('corrected_mistaken_file.csv', index=False)


