import os
import hashlib

# Menu
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
                print("Invalid directory. Please try again.")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Recursive Search

# Comparison

# output