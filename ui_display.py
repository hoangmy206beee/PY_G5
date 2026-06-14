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

# ==========================================
# HƯỚNG DẪN GIẢI THÍCH CHO THẦY CÔ KHI BỊ HỎI:
# 1. Hàm `render_history_list` nhận tham số là một mảng/danh sách chứa lịch sử.
# 2. Câu lệnh `if not history_list:` dùng để bắt lỗi tránh giao diện bị trống trải khi chưa có dữ liệu.
# 3. Vòng lặp `for` kết hợp `enumerate` giúp tự động đánh số thứ tự từ 1 đến hết danh sách mà không cần tạo biến đếm thủ công.
# 4. `st.write` là câu lệnh cơ bản của Streamlit để xuất văn bản ra giao diện người dùng.
# ==========================================