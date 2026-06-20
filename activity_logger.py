import datetime  # Library to get the real-time clock

# --- CONSTANTS ---
LOG_FILE_PATH = "history.log"  # Path to the log file

# ============================================================
# Main function: log_search_activity(keyword)
# Purpose: Get the current real time and write 1 line to history.log
#          every time a valid keyword is searched
# Input parameter: keyword (str) - the keyword the user just searched
# Returns nothing (only writes to file)
# ============================================================
def log_search_activity(keyword):
    # Get the current time (real time on the machine)
    current_time = datetime.datetime.now()
    # Format the time as: 2025-06-12 14:35:22
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # Build a text line like: [2025-06-12 14:35:22] Search: "python"
    log_entry = f"[{formatted_time}] Search: \"{keyword}\"\n"
    # Open history.log in 'a' (append) mode = add new content, keep old content
    # If the file doesn't exist yet, it will be created automatically
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)  # Write the log line to the file


# ============================================================
# Helper function: read_log_file()
# Purpose: Read the entire log file content for display (if needed)
# Returns: list of log lines (list of str), or an empty list if the file doesn't exist yet
# ============================================================
def read_log_file():
    # Try to open the file for reading; if it doesn't exist, return an empty list
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
            log_lines = log_file.readlines()  # Read each line into a list
        return log_lines
    except FileNotFoundError:
        # The file has never been created (no one has searched yet), return empty
        return []


# ============================================================
# Helper function: clear_log_file()
# Purpose: Delete the entire log file content (used when resetting)
# Returns nothing
# ============================================================
def clear_log_file():
    # Opening the file in 'w' (write) mode wipes all old content and creates an empty file
    with open(LOG_FILE_PATH, "w", encoding="utf-8") as log_file:
        log_file.write("")  # Write an empty string = clear the file
