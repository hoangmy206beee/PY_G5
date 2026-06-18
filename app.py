import streamlit as st
from data_handler import read_txt_data, save_txt_data
from fifo_logic import add_keyword_to_fifo
from input_validator import clean_user_input, is_valid_keyword
from activity_logger import log_search_activity
from ui_input import render_search_form
from ui_display import render_history_list
from analytics import render_stats_ui

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
