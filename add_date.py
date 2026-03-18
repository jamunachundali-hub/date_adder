import os
from datetime import datetime

def add_date_to_filenames(folder_path="."):
    # Get today's date in YYYY-MM-DD format
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Resolve absolute path
    abs_folder = os.path.abspath(folder_path)
    
    if not os.path.isdir(abs_folder):
        print(f"Error: Folder '{abs_folder}' does not exist.")
        return

    print(f"Processing folder: {abs_folder}")

    # Iterate through all items in the folder
    for filename in os.listdir(abs_folder):
        old_path = os.path.join(abs_folder, filename)
        
        # Only process files (skip directories)
        if os.path.isfile(old_path):
            # Check if file is already prefixed to avoid double prefixes
            if not filename.startswith(today_str):
                new_filename = f"{today_str}-{filename}"
                new_path = os.path.join(abs_folder, new_filename)
                
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"Failed to rename {filename}: {e}")
            else:
                print(f"Skipping: {filename} (already has today's date)")

if __name__ == "__main__":
    # Prompt for the folder path
    path = input("Enter the folder path (press Enter for current folder): ").strip()
    if not path:
        path = "."
    
    add_date_to_filenames(path)
