import random, string, logging, os

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def action():
    path = input("Enter path: ")
    created_files = []  # keep track of created files
    
    for i in range(10):
        # Generate random filename and extension
        file_name = generate_random_string(8)
        rand_exten = generate_random_string(3)
        file = f"{file_name}.{rand_exten}"  # Add a dot before the extension
        action_path = os.path.join(path, file)
        
        try:
            # Create the file and write "Hello World"
            with open(action_path, 'w') as f:
                f.write("Hello World")
            logging.info(f"File created: {action_path}")
            created_files.append(action_path)
        except Exception as e:
            logging.error(f"Failed to create file {action_path}: {e}")
    return created_files

def clean(path):
    confirm = input("Do you want to clean your mess(y/N): ")
    if confirm.lower() == 'y':
        try:
            os.remove(path)
            logging.info(f"File removed: {path}")
        except Exception as e:
            logging.error(f"Failed to remove file {path}: {e}")
    else:
        logging.info("Program exited with code 0.")

if __name__ == "__main__":
    created_files = action()
    for files in created_files:
        clean(files)
