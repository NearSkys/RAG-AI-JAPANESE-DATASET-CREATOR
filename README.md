# RAG-AI-JAPANESE-DATASET-CREATOR
A python script to format and create datasets for enhancing AI translation performance

# How to Use

Place the CSV file and the script in the same folder. The CSV file should contain three columns: the Japanese word, its reading, and the English translation. For example:

| Japanese | Reading  | English      |
|----------|----------|--------------|
| ご飯     | ごはん   | cooked rice  |
| 猫       | ねこ     | cat          |
| 学校     | がっこう | school       |

To run the script, open a terminal or command prompt, navigate to the folder where the script and CSV file are located, and execute the following command:

```bash
python3 Rag_Creator.py
```

The script will generate a JSON file in the same folder. This JSON file will have a structure like this:

```json
{
    "title": "Japanese Vocabulary Dataset",
    "description": "Vocabulary list with Japanese words and their translations.",
    "content": [
        {
            "japanese": "ご飯",
            "reading": "ごはん",
            "english": "cooked rice"
        },
        {
            "japanese": "猫",
            "reading": "ねこ",
            "english": "cat"
        },
        {
            "japanese": "学校",
            "reading": "がっこう",
            "english": "school"
        }
    ]
}
```

Make sure the file paths in the script match the names of your CSV and desired JSON files, once complete, the JSON file will be ready for use in your applications.
