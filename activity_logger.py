import datetime  # Thu vien lay thoi gian thuc

# --- HANG SO ---
LOG_FILE_PATH = "history.log"  # Duong dan den file ghi log

# ============================================================
# Ham chinh: log_search_activity(keyword)
# Nhiem vu: Lay thoi gian thuc va ghi 1 dong vao file history.log
#           moi khi co tu khoa hop le duoc tim kiem
# Tham so dau vao: keyword (str) - tu khoa nguoi dung vua tim
# Khong tra ve gi (chi ghi file)
# ============================================================
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


# ============================================================
# Ham phu: read_log_file()
# Nhiem vu: Doc toan bo noi dung file log de hien thi (neu can)
# Tra ve: list cac dong log (list of str), hoac list rong neu file chua co
# ============================================================
def read_log_file():
    # Thu mo file de doc, neu khong co file thi tra ve danh sach rong
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
            log_lines = log_file.readlines()  # Doc tung dong vao danh sach
        return log_lines
    except FileNotFoundError:
        # File chua ton tai lan nao (chua co ai tim kiem), tra ve rong
        return []


# ============================================================
# Ham phu: clear_log_file()
# Nhiem vu: Xoa toan bo noi dung file log (dung khi can reset)
# Khong tra ve gi
# ============================================================
def clear_log_file():
    # Mo file o che do 'w' (write) se xoa het noi dung cu va tao file trong
    with open(LOG_FILE_PATH, "w", encoding="utf-8") as log_file:
        log_file.write("")  # Ghi chuoi rong = xoa sach file


# ============================================================
# Phan test thu - chi chay khi mo thang file nay (khong chay khi import)
# ============================================================
if __name__ == "__main__":
    # Thu ghi 2 tu khoa gia lap
    log_search_activity("python flask")
    log_search_activity("fifo algorithm")

    # Doc lai file log de kiem tra
    all_logs = read_log_file()
    print("=== Noi dung history.log ===")
    for line in all_logs:
        print(line, end="")
