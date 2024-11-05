import pandas as pd
from pathlib import Path
import openai

openai.api_key = ""
def correct_column_name(column_name):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", 
        messages=[
            {"role": "user", "content": f"Correct or expand this column name: '{column_name}'"}
        ]
    )
    return response['choices'][0]['message']['content']

def correct_mistaken_file(expected_file: str, mistaken_file: str, corrected_file: str):
    # Load the files
    expected_csv_path = Path(expected_file)
    mistaken_csv_path = Path(mistaken_file)

    expected_df = pd.read_csv(expected_csv_path)
    mistaken_df = pd.read_csv(mistaken_csv_path)

    # Get the expected column order
    expected_columns = expected_df.columns

    # Use OpenAI API to correct or expand each column name in the mistaken DataFrame
    corrected_columns = {}
    for column in mistaken_df.columns:
        corrected_name = correct_column_name(column)
        corrected_columns[column] = corrected_name

    # Rename columns in the mistaken DataFrame
    mistaken_df = mistaken_df.rename(columns=corrected_columns)

    # Reorder columns to match the expected format
    mistaken_df = mistaken_df[expected_columns]

    # Save the corrected DataFrame
    mistaken_df.to_csv(corrected_file, index=False)

    print(f"Corrected file saved at {corrected_file}")
