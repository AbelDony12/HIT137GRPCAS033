Group Name: [Group CAS033]

Group Members:
[Name: Saj Pradhan] -[ID: S309494]
[Name: Imran Masud] -[ID: S376952]
[Name: Abel Aynikkadan Dony] -[ID: S379301]
[Name: Ibrahim Salman] -[ID: S376575]

import csv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_csv(csv_file_path):
    """Extract text from the 'TEXT' column of a CSV file."""
    text_column = []
    try:
        with csv_file_path.open('r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if 'TEXT' not in reader.fieldnames:
                raise ValueError(f"'TEXT' column not found in {csv_file_path.name}")
            text_column = [row['TEXT'] for row in reader]
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except FileNotFoundError:
        logging.error(f"FileNotFoundError: {csv_file_path} does not exist.")
    except PermissionError:
        logging.error(f"PermissionError: Cannot open {csv_file_path}. Check permissions.")
    except Exception as e:
        logging.error(f"Unexpected error processing file {csv_file_path}: {e}")
    return text_column

def write_to_txt(output_file_path, text_list):
    """Write the list of text entries to a text file."""
    try:
        with output_file_path.open('w', encoding='utf-8') as file:
            file.write('\n'.join(text_list) + '\n')
    except PermissionError:
        logging.error(f"PermissionError: Cannot write to {output_file_path}. Check permissions.")
    except Exception as e:
        logging.error(f"Unexpected error writing to file {output_file_path}: {e}")

def extract_and_merge_csv_files(csv_folder_path, output_txt_file):
    """Extract text from all CSV files in a folder and write to a single text file."""
    all_text = []
    csv_folder_path = Path(csv_folder_path)
    output_txt_file = Path(output_txt_file)

    if not csv_folder_path.is_dir():
        logging.error(f"The directory {csv_folder_path} does not exist.")
        return

    try:
        for file_path in csv_folder_path.glob('*.csv'):
            logging.info(f"Processing file: {file_path}")
            text_column = extract_text_from_csv(file_path)
            all_text.extend(text_column)
    except Exception as e:
        logging.error(f"Unexpected error reading files from folder {csv_folder_path}: {e}")

    if all_text:
        write_to_txt(output_txt_file, all_text)
        logging.info(f'Text extracted from CSV files and saved to {output_txt_file}')
    else:
        logging.info('No text found in CSV files.')

csv_folder = "C:/Python/new folder/Assignment 2"
output_txt_file = 'text.txt'

extract_and_merge_csv_files(csv_folder, output_txt_file)
