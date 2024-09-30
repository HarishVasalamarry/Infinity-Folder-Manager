import os
import time
import zipfile
import threading
import subprocess
import shutil

# Define the path to the infinity folder
INFINITY_FOLDER = r"path\to\infinity-folder-manager"

# Path to VLC Media Player (for media files)
VLC_PATH = r"C:\Path\To\Your\VLC\vlc.exe"

# Create the infinity folder if it doesn't exist
if not os.path.exists(INFINITY_FOLDER):
    os.makedirs(INFINITY_FOLDER)

# Keep track of uncompressed files being monitored
monitored_files = {}

# Function to check if a file is a temporary or system file
def is_temporary_or_system_file(file_path):
    file_name = os.path.basename(file_path)
    # Ignore files starting with '~$' (temporary files created by Word, etc.)
    if file_name.startswith('~$'):
        return True
    # Add more conditions if necessary (e.g., hidden files, system files)
    return False

# Function to check if a file is an audio or video file
def is_media_file(file_path):
    media_extensions = ['.mp3', '.wav', '.mp4', '.avi', '.mov', '.wmv', '.flac', '.mkv', '.mpeg', '.mpg']
    _, ext = os.path.splitext(file_path)
    return ext.lower() in media_extensions

# Function to check if a file is an image file
def is_image_file(file_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.ico']
    _, ext = os.path.splitext(file_path)
    return ext.lower() in image_extensions

# Function to compress a file into a ZIP archive
def compress_file(file_path):
    if is_temporary_or_system_file(file_path):
        print(f"Skipping temporary or system file: {file_path}")
        return

    if not os.path.exists(file_path):
        print(f"File not found: '{file_path}'")
        return

    if file_path.endswith('.zip'):
        print(f"Skipping already compressed file: {file_path}")
        return

    zip_file_path = f"{file_path}.zip"
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        print(f"Compressed '{file_path}' to '{zip_file_path}'")
    except Exception as e:
        print(f"Error compressing '{file_path}': {e}")
        return

    # Delete the original file after compression
    try:
        os.remove(file_path)
        print(f"Deleted original file: '{file_path}'")
    except Exception as e:
        print(f"Error deleting '{file_path}': {e}")

# Function to uncompress a ZIP file
def uncompress_file(zip_file_path):
    if not os.path.exists(zip_file_path):
        print(f"Zip file not found: '{zip_file_path}'")
        return

    if not zip_file_path.endswith('.zip'):
        print(f"Not a zip file: {zip_file_path}")
        return

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            zipf.extractall(INFINITY_FOLDER)
        print(f"Extracted '{zip_file_path}'")
    except Exception as e:
        print(f"Error extracting '{zip_file_path}': {e}")
        return

    # Delete the zip file
    try:
        os.remove(zip_file_path)
        print(f"Deleted zip file: '{zip_file_path}'")
    except Exception as e:
        print(f"Error deleting '{zip_file_path}': {e}")

# Function to monitor an uncompressed file for closure
def monitor_file_for_closure(file_path, process=None):
    print(f"Monitoring '{file_path}' for closure")

    if is_media_file(file_path) and process:
        # Wait for the VLC process to exit
        process.wait()
        # Recompress the file
        compress_file(file_path)
        print(f"Recompressed and cleaned up '{file_path}'")
        monitored_files.pop(file_path, None)
    elif is_image_file(file_path):
        # Prompt user to press Enter when done viewing the image
        print(f"Press Enter when you are done viewing the image '{os.path.basename(file_path)}' to recompress it.")
        input()
        compress_file(file_path)
        print(f"Recompressed and cleaned up '{file_path}'")
        monitored_files.pop(file_path, None)
    else:
        # For other files, monitor until they are no longer in use
        while True:
            time.sleep(1)
            if is_file_in_use(file_path):
                continue
            else:
                # File is no longer in use
                compress_file(file_path)
                print(f"Recompressed and cleaned up '{file_path}'")
                # Remove from monitored files
                monitored_files.pop(file_path, None)
                break

# Function to check if a file is in use
def is_file_in_use(file_path):
    try:
        # Try to open the file exclusively
        with open(file_path, 'a'):
            return False
    except Exception:
        return True

# Function to display menu and handle user interaction
def display_menu():
    while True:
        print("\n--- Infinity Folder Manager ---")
        print("1. List files")
        print("2. Access and edit a file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            list_files()
        elif choice == '2':
            access_file()
        elif choice == '3':
            print("Exiting Infinity Folder Manager.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Function to list files in the infinity folder
def list_files():
    files = os.listdir(INFINITY_FOLDER)
    if not files:
        print("The infinity folder is empty.")
    else:
        print("\nFiles in the infinity folder:")
        for idx, file in enumerate(files, start=1):
            print(f"  {idx}. {file}")

# Function to access and edit a file
def access_file():
    # List available zip files
    zip_files = [f for f in os.listdir(INFINITY_FOLDER) if f.endswith('.zip')]
    if not zip_files:
        print("No ZIP files available to access.")
        return

    print("\nAvailable ZIP Files:")
    for idx, zip_file in enumerate(zip_files, start=1):
        print(f"  {idx}. {zip_file}")

    zip_choice = input("Enter the number of the ZIP file you want to access: ")
    if not zip_choice.isdigit() or int(zip_choice) < 1 or int(zip_choice) > len(zip_files):
        print("Invalid choice. Please try again.")
        return

    selected_zip = zip_files[int(zip_choice) - 1]
    zip_path = os.path.join(INFINITY_FOLDER, selected_zip)

    # Uncompress the selected zip file
    uncompress_file(zip_path)
    uncompressed_file = os.path.join(INFINITY_FOLDER, selected_zip[:-4])  # Remove .zip extension

    # Open the uncompressed file
    if os.path.exists(uncompressed_file):
        print(f"Attempting to open file: {uncompressed_file}")
        try:
            if is_media_file(uncompressed_file):
                # Use VLC to open the file
                if os.path.exists(VLC_PATH):
                    process = subprocess.Popen([VLC_PATH, uncompressed_file])
                    # Start monitoring the media file using the process handle
                    if uncompressed_file not in monitored_files:
                        monitored_files[uncompressed_file] = True
                        threading.Thread(target=monitor_file_for_closure, args=(uncompressed_file, process), daemon=True).start()
                else:
                    print(f"VLC Media Player not found at '{VLC_PATH}'. Please check the VLC_PATH variable.")
            else:
                # Open the file with the default application using os.startfile()
                os.startfile(uncompressed_file)
                # Start monitoring the uncompressed file
                if uncompressed_file not in monitored_files:
                    monitored_files[uncompressed_file] = True
                    threading.Thread(target=monitor_file_for_closure, args=(uncompressed_file,), daemon=True).start()
        except Exception as e:
            print(f"Error opening file '{uncompressed_file}': {e}")
    else:
        print(f"Uncompressed file '{uncompressed_file}' does not exist.")

# Function to monitor the infinity folder for new files
def monitor_folder():
    existing_files = set(os.listdir(INFINITY_FOLDER))
    print(f"Started monitoring '{INFINITY_FOLDER}' for new files...\n")
    while True:
        time.sleep(1)
        current_files = set(os.listdir(INFINITY_FOLDER))
        new_files = current_files - existing_files
        for file_name in new_files:
            file_path = os.path.join(INFINITY_FOLDER, file_name)
            if is_temporary_or_system_file(file_path):
                print(f"Skipping temporary or system file: {file_path}")
                continue
            if not file_name.endswith('.zip'):
                # Check if the file is already being monitored (e.g., uncompressed for editing)
                if file_path in monitored_files:
                    continue
                # Delay to ensure file is fully written
                time.sleep(1)
                compress_file(file_path)
        existing_files = current_files

def main():
    # Start the folder monitor in a separate thread
    folder_monitor_thread = threading.Thread(target=monitor_folder, daemon=True)
    folder_monitor_thread.start()

    # Start the menu interface
    display_menu()

if __name__ == "__main__":
    main()
