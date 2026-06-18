import streamlit as st
from data_handler import read_excel_data, save_excel_data
from fifo_logic import add_keyword_to_fifo
from input_validator import clean_user_input, is_valid_keyword
from activity_logger import log_search_activity
from ui_input import render_search_form
from ui_display import render_history_list
from analytics import render_stats_ui

def main():
    st.set_page_config(page_title="Mô phỏng Lịch sử Tìm kiếm", layout="centered")
    st.title("🔍 Mô phỏng Lịch sử Tìm kiếm (FIFO)")
    st.markdown("**Nhóm thực hiện:** Mỹ (Leader), Loan, Quang, Nghĩa, Đạt, Phong, Bình, Giang")
    

    if 'history_state' not in st.session_state:
        st.session_state.history_state = read_excel_data()

    submit_clicked, raw_keyword = render_search_form()

    if submit_clicked:
        clean_keyword = clean_user_input(raw_keyword) 
        
        if is_valid_keyword(clean_keyword): 
            st.session_state.history_state = add_keyword_to_fifo(
                st.session_state.history_state, clean_keyword
            )
            
            save_excel_data(st.session_state.history_state) 
            log_search_activity(clean_keyword) 
            
            st.success(f"Đã tìm kiếm thành công: {clean_keyword}")
        else:
            st.warning("Vui lòng nhập từ khóa hợp lệ!")
    st.markdown("---")
    render_history_list(st.session_state.history_state)
    render_stats_ui(st.session_state.history_state)

if __name__ == "__main__":
    main()
#---------activity_logger
import datetime  # Thu vien lay thoi gian thuc

# --- HANG SO ---
LOG_FILE_PATH = "history.log"  # Duong dan den file ghi log
# Ham chinh: log_search_activity(keyword)
# Nhiem vu: Lay thoi gian thuc va ghi 1 dong vao file history.log
#           moi khi co tu khoa hop le duoc tim kiem
# Tham so dau vao: keyword (str) - tu khoa nguoi dung vua tim
# Khong tra ve gi (chi ghi file)
def log_search_activity(keyword):
    # Lay thoi gian hien tai (thoi gian thuc tren may)
    current_time = datetime.datetime.now()

    # Dinh dang thoi gian theo kieu: 2025-06-12 14:35:22
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Tao 1 dong text theo dang: [2025-06-12 14:35:22] Tim kiem: "python"
    log_entry = f"[{formatted_time}] Tim kiem: \"{keyword}\"\n"

    # Mo file history.log o che do 'a' (append = ghi them, khong xoa cu)
    # Neu file chua ton tai thi tu dong tao moi
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)  # Ghi dong log vao file
# Ham phu: read_log_file()
# Nhiem vu: Doc toan bo noi dung file log de hien thi (neu can)
# Tra ve: list cac dong log (list of str), hoac list rong neu file chua co
def read_log_file():
    # Thu mo file de doc, neu khong co file thi tra ve danh sach rong
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
            log_lines = log_file.readlines()  # Doc tung dong vao danh sach
        return log_lines
    except FileNotFoundError:
        # File chua ton tai lan nao (chua co ai tim kiem), tra ve rong
        return []

# Ham phu: clear_log_file()
# Nhiem vu: Xoa toan bo noi dung file log (dung khi can reset)
# Khong tra ve gi
def clear_log_file():
    # Mo file o che do 'w' (write) se xoa het noi dung cu va tao file trong
    with open(LOG_FILE_PATH, "w", encoding="utf-8") as log_file:
        log_file.write("")  # Ghi chuoi rong = xoa sach file
# Phan test thu - chi chay khi mo thang file nay (khong chay khi import)

if __name__ == "__main__":
    # Thu ghi 2 tu khoa gia lap
    log_search_activity("python flask")
    log_search_activity("fifo algorithm")
    all_logs = read_log_file()
    print("=== Noi dung history.log ===")
    for line in all_logs:
        print(line, end="")
#-----------analytics
import streamlit as st

def render_stats_ui(history_list):
    st.write("SEARCH HISTORY ANALYTICS")

    if len(history_list) == 0:
        st.write("No data available")
        return
    
    total_keywords = len(history_list)

    longest_keywords = history_list[0]

    for i in history_list:
        if len(i) > len(longest_keywords):
            longest_keywords = i

    st.write(f"Total keywords: {total_keywords}")
    st.write(f"Longest keyword: `{longest_keywords}` ({len(longest_keywords)} character)")
#--------data_handler
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
#-----fifo
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
#----------input
def clean_user_input(raw_text):
    if raw_text is None:
        return ""
    return str(raw_text).strip()
def is_valid_keyword(text):
    cleaned_text = clean_user_input(text)
    if cleaned_text == "":
        return False
    return True
#--------ui_display
import streamlit as st

# ==========================================
# THÀNH VIÊN THỰC HIỆN: ĐỒNG VĂN BÌNH
# NHIỆM VỤ: HIỂN THỊ DANH SÁCH LỊCH SỬ TÌM KIẾM
# ==========================================

def render_history_list(history_list):
    """
    Hàm này nhận vào một danh sách các từ khóa (history_list)
    và hiển thị chúng lên giao diện web Streamlit một cách gọn gàng.
    """
    
    # Dùng st.subheader để tạo một tiêu đề nhỏ cho phần lịch sử
    st.subheader("📜 Lịch sử tìm kiếm gần đây")
    
    # Kiểm tra xem danh sách lịch sử truyền vào có bị rỗng hay không
    if not history_list:
        # Nếu danh sách trống (chưa có ai tìm gì), thông báo cho người dùng biết
        st.info("Chưa có lịch sử tìm kiếm nào.")
    else:
        # Nếu danh sách có dữ liệu, dùng vòng lặp để duyệt qua từng từ khóa
        # Dùng enumerate để lấy cả số thứ tự (index) bắt đầu từ 1 và nội dung từ khóa (keyword)
        for index, keyword in enumerate(history_list, start=1):
            
            # Tạo tên biến rõ ràng lưu chuỗi định dạng hiển thị theo quy tắc d_case
            formatted_history_item = f"{index}. {keyword}"
            
            # Sử dụng st.write để in từng dòng lịch sử ra màn hình web
            st.write(formatted_history_item)

# HƯỚNG DẪN GIẢI THÍCH:
# 1. Hàm `render_history_list` nhận tham số là một mảng/danh sách chứa lịch sử.
# 2. Câu lệnh `if not history_list:` dùng để bắt lỗi tránh giao diện bị trống trải khi chưa có dữ liệu.
# 3. Vòng lặp `for` kết hợp `enumerate` giúp tự động đánh số thứ tự từ 1 đến hết danh sách mà không cần tạo biến đếm thủ công.
# 4. `st.write` là câu lệnh cơ bản của Streamlit để xuất văn bản ra giao diện người dùng.


#-------ui_input
import streamlit as st
EXCEL_FILE_PATH = "data.xlsx"
def render_search_form():
    with st.form(key="search_form"):
        user_keyword = st.text_input(
            label="Nhập từ khóa tìm kiếm",
            placeholder="Ví dụ: Python, AI, Streamlit..."
        )
        is_search_button_clicked = st.form_submit_button("Tìm kiếm")
    user_keyword = user_keyword.strip()
    is_valid_input = len(user_keyword) > 0

    if is_search_button_clicked and not is_valid_input:
        st.warning("Vui lòng nhập từ khóa trước khi tìm kiếm.")

    return user_keyword, is_search_button_clicked, is_valid_input

#thư viên  **Streamlit** để tạo một form tìm kiếm đơn giản cho người dùng nhập dữ liệu.
# hằng số `EXCEL_FILE_PATH = "data.xlsx"` được khai báo ở đầu file. Đây là đường dẫn đến file Excel dùng để lưu trữ hoặc đọc dữ liệu trong chương trình.
#Hàm `render_search_form()` có nhiệm vụ hiển thị form nhập liệu trên giao diện Streamlit. Bên trong hàm, câu lệnh `with st.form(key="search_form"):` được dùng để tạo một form có tên là `search_form`. Form này giúp gom ô nhập dữ liệu và nút bấm vào cùng một khu vực xử lý.
#Trong form, `st.text_input()` tạo một ô nhập văn bản để người dùng nhập từ khóa tìm kiếm. Biến `user_keyword` dùng để lưu nội dung mà người dùng nhập vào. Thuộc tính `label` hiển thị tiêu đề cho ô nhập, còn `placeholder` hiển thị ví dụ gợi ý khi ô nhập đang trống.
#Sau đó, `st.form_submit_button("Tìm kiếm")` tạo nút bấm có tên là **Tìm kiếm**. Khi người dùng nhấn nút này, biến `is_search_button_clicked` sẽ nhận giá trị `True`, ngược lại sẽ là `False`.
#Dòng `user_keyword = user_keyword.strip()` dùng để loại bỏ khoảng trắng thừa ở đầu và cuối từ khóa. Điều này giúp dữ liệu nhập vào sạch hơn trước khi xử lý.
#Biến `is_valid_input = len(user_keyword) > 0` dùng để kiểm tra xem người dùng có nhập nội dung hay không. Nếu độ dài của từ khóa lớn hơn 0 thì dữ liệu hợp lệ.
#Câu lệnh `if is_search_button_clicked and not is_valid_input:` dùng để kiểm tra trường hợp người dùng bấm nút **Tìm kiếm** nhưng chưa nhập từ khóa. Khi đó, chương trình sẽ hiển thị cảnh báo bằng `st.warning("Vui lòng nhập từ khóa trước khi tìm kiếm.")`.
#Cuối cùng, hàm trả về ba giá trị: `user_keyword`, `is_search_button_clicked` và `is_valid_input`. Các giá trị này có thể được sử dụng ở file chính để tiếp tục xử lý việc tìm kiếm dữ liệu.
