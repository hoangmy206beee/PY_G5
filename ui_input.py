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
