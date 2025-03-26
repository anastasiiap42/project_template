def print_to_console(text):
    """
    Function to print text to the console.
    
    Args:
    text (str): Text to be printed
    """
    print(text)

def write_to_file(text, file_path='data/output.txt'):
    """
    Function to write text to a file using built-in Python capabilities.
    
    Args:
    text (str): Text to be written to the file
    file_path (str): Path to the file where text will be written (default: 'data/output.txt')
    """
    with open(file_path, 'w') as file:
        file.write(text)