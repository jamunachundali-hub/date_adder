import os
import argparse
from datetime import datetime

def add_date_to_filenames(directory):
    """
    Adds today's date (YYYY-MM-DD) to the beginning of every filename in a folder.
    Excludes the script itself if it's in the target directory.
    """
    # Get today's date in YYYY-MM-DD format
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Resolve the directory path
    abs_directory = os.path.abspath(directory)
    script_name = os.path.basename(__file__)
    
    if not os.path.isdir(abs_directory):
        print(f"Error: The directory '{abs_directory}' does not exist.")
        return

    print(f"--- Processing folder: {abs_directory} ---")
    print(f"Prefix to add: {today_str}-")

    processed_count = 0
    skipped_count = 0

    # Iterate through all files in the directory
    for filename in os.listdir(abs_directory):
        # Full path for the current file
        old_path = os.path.join(abs_directory, filename)
        
        # Skip if it's a directory
        if not os.path.isfile(old_path):
            continue

        # Skip the script itself if it's in the folder
        if filename == script_name:
            continue
            
        # Check if it already starts with the current date
        if filename.startswith(today_str):
            print(f"Skipping: {filename} (Already prefixed)")
            skipped_count += 1
            continue

        # Calculate new filename and path
        new_filename = f"{today_str}-{filename}"
        new_path = os.path.join(abs_directory, new_filename)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
            processed_count += 1
        except Exception as e:
            print(f"Failed to rename {filename}: {e}")

    print(f"\nSummary:")
    print(f"  Files renamed: {processed_count}")
    print(f"  Files skipped: {skipped_count}")
    print(f"----------------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add today's date to filenames in a folder.")
    parser.add_argument("directory", nargs="?", default=".", help="The folder containing files to rename (default: current directory)")
    
    args = parser.parse_args()
    add_date_to_filenames(args.directory)
