from datetime import datetime
import pandas as pd

file_path = 'Diff format.csv'
df = pd.read_csv(file_path)

print(df.columns)


def standardize_date(date):
    formats = [
        '%d %m %Y',  # 30 10 2024
        '%Y%m%d',    # 20241030
        '%d.%m.%Y',  # 30.10.2024
        '%d-%m-%Y',  # 30-10-2024
        '%d-%b-%y'   # 30-Oct-24
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date, fmt).strftime('%d-%b-%y')
        except ValueError:
            continue 
    return date  

df['Date'] = df['Date'].apply(standardize_date)

df.to_csv('cleaned_file.csv', index=False)


df = pd.read_csv(file_path)

ori = ['Date', 'Customer Number', 'Account Number', 'Account Name',
       'Account Class', 'Account Status', 'Account Currency',
       'Alternative Currency', 'Outstanding Amount', 'Up 30days', 'Up 60days',
       'Up 90days', 'Up 120days', 'Up 150days', 'Up 180days', 'Up 210days',   
       'Up 240days', 'Up 270days', 'Up 300days', 'Up 330days', 'Up 364days',  
       'Up 365days+']

err = ['Date', 'Account Name', 'Acc Num', 'Account Class', 'Account Status',  
       'Cust Num', 'Account Currency', 'Alternative Currency',
       'Outstanding Amt', 'Up 30days', 'Up 60days', 'Up 90days', 'Up 120days',
       'Up 150days', 'Up 180days', 'Up 210days', 'Up 240days', 'Up 270days',  
       'Up 300days', 'Up 330days', 'Up 364days', 'Up 365days+']




