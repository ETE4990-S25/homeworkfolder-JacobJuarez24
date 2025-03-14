#Jacob Juarez

import os
import hashlib

# Menu Function
def show_menu():
    """Displays a simple menu for user interaction."""
    print("File Comparison Tool")
    print("1. Find identical files in a directory")
    print("2. Exit")
    
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1/2): ")
        
        if choice == '1':
            directory = input("Enter the directory path to search: ")
            if os.path.isdir(directory):
                print("Searching for identical files...")
                identical_files = find_identical_files(directory)
                if identical_files:
                    print("Identical files found:")
                    for group in identical_files:
                        print("\n".join(group))
                else:
                    print("No identical files found.")
            else:
                print("Invalid directory. Try again.")
        
        elif choice == '2':
            print("Exiting the program.")
            break
        
        else:
            print("Not an option. Try again.")

# Recursive Search and File Comparison
def find_identical_files(directory):
    """Recursively searches for files in a directory and finds identical files based on checksum."""
    files_dict = {}

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_checksum = get_checksum(file_path)

            # Add file checksum to dictionary with file name as key
            if file not in files_dict:
                files_dict[file] = {}
            if file_checksum not in files_dict[file]:
                files_dict[file][file_checksum] = []
            files_dict[file][file_checksum].append(file_path)

    identical_files = []

    # Check for identical files (same file name and checksum)
    for file_name, checksum_dict in files_dict.items():
        for checksum, file_paths in checksum_dict.items():
            if len(file_paths) > 1:  # More than one file with the same checksum
                identical_files.append(file_paths)

    return identical_files

# Function to get the checksum (MD5 or SHA-256) of a file
def get_checksum(file_path, algorithm='md5'):
    """Returns the checksum (MD5 by default) of a file."""
    hash_obj = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

if __name__ == "__main__":
    main()