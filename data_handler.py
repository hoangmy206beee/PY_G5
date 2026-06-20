import os

TXT_FILE_PATH = "data.txt"

def read_txt_data():
    # Kiểm tra nếu file txt chưa tồn tại thì trả về danh sách rỗng
    if not os.path.exists(TXT_FILE_PATH):
        return []
    try:
        with open(TXT_FILE_PATH, 'r', encoding='utf-8') as f:
            # Đọc từng dòng, xóa khoảng trắng thừa và loại bỏ dòng trống
            raw_list = [line.strip() for line in f if line.strip()]

        # Chỉ lấy 10 từ khóa mới nhất và đảo ngược để từ mới nhất lên đầu
        return raw_list[-10:][::-1]
    except Exception as e:
        return []

def save_txt_data(history_list):
    # Mở file txt ở chế độ ghi đè 'w' để cập nhật danh sách mới nhất
    with open(TXT_FILE_PATH, 'w', encoding='utf-8') as f:
        for item in history_list:
            f.write(f"{item}\n")