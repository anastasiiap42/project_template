import pandas as pd

def input_from_console():
    """
    Function to input text from the console.
    
    Return:
    str: Text input by the user
    """
    return input("Enter your text: ")

def read_from_file():
    """
    Function to read text from a file using built-in Python capabilities.
    
    Return:
    str: Content of the file
    """
    with open('data/input.txt', 'r') as file:
        return file.read()

def read_from_file_pandas():
    """
    Function to read text from a file using pandas library.
    
    Return:
    str: Content of the file
    """
    df = pd.read_csv('data/input.txt', header=None)
    return df[0][0]