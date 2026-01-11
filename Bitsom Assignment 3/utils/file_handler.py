import os

def load_raw_data(file_path):
    """
    Reads pipe-delimited data using 'latin1' encoding 
    to handle non-UTF-8 characters.
    """
    data_lines = []
    try:
        # 'latin1' handles non-UTF-8 encoding issues
        with open(file_path, 'r', encoding='latin1') as file:
            header = file.readline() # Skip header row
            for line in file:
                if line.strip():
                    # Split by pipe delimiter
                    parts = line.strip().split('|')
                    data_lines.append(parts)
        return data_lines
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []