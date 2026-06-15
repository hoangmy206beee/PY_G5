# Thu vien pandas dung de doc va ghi file Excel
import pandas as pd

# Duong dan file Excel luu lich su tim kiem
EXCEL_FILE_PATH = "data.xlsx"

def read_excel_data():
    # Doc du lieu tu file Excel va chuyen thanh list dictionary
    try:
        history_dataframe = pd.read_excel(EXCEL_FILE_PATH)
        return history_dataframe.fillna("").to_dict("records")
    except FileNotFoundError:
        return []

def save_excel_data(history_list):
    # Luu danh sach lich su tim kiem xuong file Excel
    history_dataframe = pd.DataFrame(history_list)
    history_dataframe.to_excel(EXCEL_FILE_PATH, index=False)