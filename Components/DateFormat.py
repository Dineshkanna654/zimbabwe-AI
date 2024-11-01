from datetime import datetime


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






