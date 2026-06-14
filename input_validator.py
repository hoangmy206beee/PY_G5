def clean_user_input(raw_text):
    if raw_text is None:
        return ""
    return str(raw_text).strip()
def is_valid_keyword(text):
    cleaned_text = clean_user_input(text)
    if cleaned_text == "":
        return False
    return True
