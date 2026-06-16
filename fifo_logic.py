# Thu vien pandas va data_handler cho chuc nang FIFO
from data_handler import read_excel_data, save_excel_data


max_history_size = 10  # Gioi han toi da 10 tu khoa trong lich su

def add_keyword_to_fifo(keyword):
   
    #Thêm từ khóa vào đầu danh sách FIFO.
    #Nếu danh sách vượt quá max_history_size (10), xóa từ cũ nhất ở cuối.
    
    history_list = read_excel_data() #Doc du lieu lich su hien tai tu file Excel
    
    new_entry = {"keyword": keyword} #Tao dict moi chua tu khoa vua nhap
    
    history_list.insert(0, new_entry) #Them tu khoa moi vao DAU danh sach (vi tri 0)
    
    if len(history_list) > max_history_size:
        history_list = history_list[:max_history_size] #Neu danh sach vuot qua 10 tu, cat bo phan cuoi
    
    save_excel_data(history_list) #Luu danh sach da cap nhat lai vao file Excel

