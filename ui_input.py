import streamlit as st
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

