import pandas as pd
from pathlib import Path
from transformers import pipeline
import numpy as np

# Load a pre-trained model for semantic similarity
model = pipeline('feature-extraction', model='bert-base-uncased')

def get_similarity(col1, col2):
    emb1 = model(col1)[0][0]
    emb2 = model(col2)[0][0]
    emb1 = np.array(emb1)
    emb2 = np.array(emb2)
    
    if np.linalg.norm(emb1) == 0 or np.linalg.norm(emb2) == 0:
        return 0.0
    
    return np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))

def correct_mistaken_file(expected_file: str, mistaken_file: str, corrected_file: str):
    expected_csv_path = Path(expected_file)
    mistaken_csv_path = Path(mistaken_file)

    expected_df = pd.read_csv(expected_csv_path)
    mistaken_df = pd.read_csv(mistaken_csv_path)

    # Standardize column names
    expected_df.columns = expected_df.columns.str.strip().str.lower()
    mistaken_df.columns = mistaken_df.columns.str.strip().str.lower()

    # Get the expected column order
    expected_columns = expected_df.columns.tolist()

    # Create a dynamic mapping based on semantic similarity
    column_mapping = {}
    for expected_col in expected_columns:
        best_match = None
        best_score = -1
        for mistaken_col in mistaken_df.columns:
            similarity_score = get_similarity(expected_col, mistaken_col)
            if similarity_score > best_score:
                best_score = similarity_score
                best_match = mistaken_col
        if best_match:
            column_mapping[best_match] = expected_col

    # Rename columns in the mistaken DataFrame
    mistaken_df = mistaken_df.rename(columns=column_mapping)

    # Check renamed columns
    print("Renamed Mistaken DataFrame columns:", mistaken_df.columns.tolist())

    # Reorder columns to match the expected format
    missing_columns = [col for col in expected_columns if col not in mistaken_df.columns]
    if missing_columns:
        print("Missing columns in the mistaken DataFrame:", missing_columns)
        return  # Exit if there are missing columns

    mistaken_df = mistaken_df[expected_columns]

    # Save the corrected DataFrame
    mistaken_df.to_csv(corrected_file, index=False)
    print(f"Corrected file saved at {corrected_file}")
