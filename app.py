import streamlit as st
import os
import datetime

TXT_FILE_PATH = "data.txt"
LOG_FILE_PATH = "history.log" 
max_history_size = 10 

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

def add_keyword_to_fifo(history_list, keyword):
    """
   Add a keyword to the list using the String List structure.
     If the keyword already exists, remove the old entry and move it to the beginning of the list.
    """
    if keyword in history_list:
        history_list.remove(keyword)
        
    history_list.insert(0, keyword)
    
    if len(history_list) > max_history_size:
        history_list.pop()
        
    return history_list

def clean_user_input(raw_text):
    if raw_text is None:
        return ""
    return str(raw_text).strip()

def is_valid_keyword(text):
    cleaned_text = clean_user_input(text)
    if cleaned_text == "":
        return False
    return True

def log_search_activity(keyword):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{formatted_time}] Search: \"{keyword}\"\n"

    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry) 

def read_log_file():
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
            log_lines = log_file.readlines() 
        return log_lines
    except FileNotFoundError:
        return []

def clear_log_file():
    with open(LOG_FILE_PATH, "w", encoding="utf-8") as log_file:
        log_file.write("") 

def render_search_form():
    with st.form(key="search_form"):
        user_keyword = st.text_input(
            label="Enter a search keyword",
            placeholder="Examples: Python, AI, Streamlit..."
        )
        is_search_button_clicked = st.form_submit_button("Search")
        
    user_keyword = user_keyword.strip()
    is_valid_input = len(user_keyword) > 0

    if is_search_button_clicked and not is_valid_input:
        st.warning("Please enter a keyword before searching")

    return user_keyword, is_search_button_clicked, is_valid_input

def render_history_list(history_list):
    st.subheader(" Recent Search History")
    if not history_list:
        st.info("No search history available")
    else:
        for index, keyword in enumerate(history_list, start=1):
            formatted_history_item = f"{index}. {keyword}"
            st.write(formatted_history_item)

def render_stats_ui(history_list):
    st.write("📊 SEARCH HISTORY ANALYTICS")

    if len(history_list) == 0:
        st.write("No data available")
        return
    
    total_keywords = len(history_list)
    longest_keywords = history_list[0]

    for i in history_list:
        if len(i) > len(longest_keywords):
            longest_keywords = i

    st.write(f"Total keywords: {total_keywords}")
    st.write(f"Longest keyword: `{longest_keywords}` ({len(longest_keywords)} characters)")

def main():
    st.set_page_config(page_title="Simulated Search History", layout="centered")
    st.title("🔍 Simulated Search History (FIFO)")
    
    if 'history_state' not in st.session_state:
        st.session_state.history_state = read_txt_data()
      
    raw_keyword, submit_clicked, is_valid_input = render_search_form()

    if submit_clicked:
        clean_keyword = clean_user_input(raw_keyword) 
        
        if is_valid_keyword(clean_keyword): 
            st.session_state.history_state = add_keyword_to_fifo(
                st.session_state.history_state, clean_keyword
            )
            
            save_txt_data(st.session_state.history_state) 
            log_search_activity(clean_keyword) 
            
            st.success(f"Search completed successfully: {clean_keyword}")
        else:
            st.warning("Please enter a valid keyword!")
            
    st.markdown("---")
    render_history_list(st.session_state.history_state)
    render_stats_ui(st.session_state.history_state)
if __name__ == "__main__":
    main()