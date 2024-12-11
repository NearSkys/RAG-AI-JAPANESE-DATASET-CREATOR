import csv
import json
import os

def convert_to_rag(input_file, output_file):
    rag_data = {
        "title": "Japanese Vocabulary Dataset",
        "description": "Vocabulary list with japanese words and their translations.",
        "content": []
    }

    try:
        with open(input_file, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if len(row) >= 3:
                    japanese, reading, english = row[0].strip(), row[1].strip(), row[2].strip()
                    rag_data["content"].append({
                        "japanese": japanese,
                        "reading": reading,
                        "english": english
                    })

        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(rag_data, json_file, ensure_ascii=False, indent=4)

        print(f"Conversion complete. JSON saved to: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

input_path = "vocabulary.csv"
output_path = "vocabulary_rag.json"
convert_to_rag(input_path, output_path)
