import os
TXT_FILE_PATH = "data.txt"

def read_txt_data():
    if not os.path.exists(TXT_FILE_PATH):
        return []
    try:
        with open(TXT_FILE_PATH, 'r', encoding='utf-8') as f:
            raw_list = [line.strip() for line in f if line.strip()]
            
        return raw_list[-10:][::-1]
    except Exception as e:
        return []

def save_txt_data(history_list):
    with open(TXT_FILE_PATH, 'w', encoding='utf-8') as f:
        for item in history_list:
            f.write(f"{item}\n")
