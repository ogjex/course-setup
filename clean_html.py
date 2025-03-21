import os
import sys

def clean_html(file:str):
    #create the full path to the file that needs cleaning
    file_path = os.path.abspath(file)
    if not os.path.exists(file_path):
        print(f"file not found: {file_path}")
        os._exit(0)
    else:
        print(f"path to file found: {file_path}")
# make the main method that counts arguments
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_html.py file-to-clean")
        sys.exit(1)
    
    clean_html(sys.argv[1])

