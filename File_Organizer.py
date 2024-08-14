import os
import logging
import shutil

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_files(path: str, target_dir: str = None) -> None:
    files = os.listdir(path)
    
    if target_dir is None:
        target_dir = path  # Default target directory is the same as the source
    
    for file in files:
        file_path = os.path.join(path, file)
        
        if os.path.isfile(file_path):
            # Get the file extension and remove the leading dot
            filename, extension = os.path.splitext(file)
            extension_dir = extension.lstrip('.')
            
            # If there's no extension, put the file in a folder named "No Extension"
            if not extension_dir:
                extension_dir = 'NULL'
            
            # Full path to the directory where files with this extension will be moved
            exten_dir_path = os.path.join(target_dir, extension_dir)
            
            # If the directory doesn't exist, create it
            if not os.path.isdir(exten_dir_path):
                os.makedirs(exten_dir_path)
                logging.info(f"Directory created: {exten_dir_path}")
            
            # Move the file to the target directory
            try:
                shutil.move(file_path, exten_dir_path)
                logging.info(f"Moved {file} to {exten_dir_path}")
            except Exception as e:
                logging.error(f"Failed to move {file} to {exten_dir_path}: {e}")

def main() -> None:
    path = input("Enter the path of the directory to organize: ")
    target_dir = input("Enter the target directory (or press Enter to organize in the same directory): ")
    
    # Organize files in the specified directory
    organize_files(path, target_dir if target_dir else None)

if __name__ == "__main__":
    main()

    # test()

