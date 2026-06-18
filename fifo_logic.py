# File: fifo_logic.py - Code by Quang

max_history_size = 10  # Giới hạn tối đa 10 từ khóa

def add_keyword_to_fifo(history_list, keyword):
    """
    Thêm từ khóa vào danh sách theo chuẩn cấu trúc mảng chuỗi (String List).
    Nếu từ khóa đã tồn tại thì xóa cái cũ để đưa lên đầu.
    """
    # Nếu từ khóa đã có trong lịch sử thì xóa vị trí cũ đi
    if keyword in history_list:
        history_list.remove(keyword)
        
    # Thuat toan FIFO (First-In): Chèn từ khóa mới vào đầu danh sách (vị trí 0)
    history_list.insert(0, keyword)
    
    # Thuat toan FIFO (First-Out): Nếu danh sách vượt quá 10, cắt bỏ phần tử cũ nhất ở cuối
    if len(history_list) > max_history_size:
        history_list.pop()
        
    return history_list