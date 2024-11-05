import pandas as pd
from pathlib import Path
from fuzzywuzzy import process

def correct_mistaken_file(expected_file: str, mistaken_file: str, corrected_file: str):
    # Load the files
    expected_csv_path = Path(expected_file)
    mistaken_csv_path = Path(mistaken_file)

    expected_df = pd.read_csv(expected_csv_path)
    mistaken_df = pd.read_csv(mistaken_csv_path)

    # Get the expected column names
    expected_columns = expected_df.columns.tolist()

    # Create a mapping from mistaken columns to expected columns
    column_mapping = {}
    for col in mistaken_df.columns:
        best_match, score = process.extractOne(col, expected_columns)
        if score >= 75:
            column_mapping[col] = best_match

    # Rename columns in the mistaken DataFrame
    mistaken_df = mistaken_df.rename(columns=column_mapping)

    # Reorder columns to match the expected format
    mistaken_df = mistaken_df[expected_columns]

    # Save the corrected DataFrame
    mistaken_df.to_csv(corrected_file, index=False)

    print(f"Corrected file saved at {corrected_file}")
