Group Name: [Group CAS033]

Group Members:
[Name: Saj Pradhan] -[ID: S309494]
[Name: Imran Masud] -[ID: S376952]
[Name: Abel Aynikkadan Dony] -[ID: S379301]
[Name: Ibrahim Salman] -[ID: S376575]



import csv
from collections import Counter
import re
import os

def get_top_words(file_path, top_n=30, chunk_size=4096):
    word_counts = Counter()
    total_chunks = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                words = re.findall(r'\b(?![0-9]+\b)\w+\b', chunk.lower()) 
                word_counts.update(words)
                total_chunks += 1

        print(f"Total chunks read: {total_chunks}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return []

    return word_counts.most_common(top_n)

def write_top_words_to_csv(top_words, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Count'])
            writer.writerows(top_words)
    except IOError as e:
        print(f"Error writing to file {csv_file_path}: {e}")

def main():
    input_txt_file = "C:\\Python\\new folder\\Assignment 2\\text.txt"
    output_csv_file = 'Top 30 most common words.csv'

    if not os.path.isfile(input_txt_file):
        print(f"The file {input_txt_file} does not exist.")
        return

    top_words = get_top_words(input_txt_file)
    if top_words:
        write_top_words_to_csv(top_words, output_csv_file)
        print(f'Top 30 words and their counts saved to {output_csv_file}')
    else:
        print("No words to process.")

if __name__ == "__main__":
    main()
