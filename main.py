from input import input_from_console, read_from_file, read_from_file_pandas
from output import print_to_console, write_to_file

def main():
    """
    Main function to demonstrate the use of input and output functions.
    """
    console_input = input_from_console()
    print_to_console("Text from console:")
    print_to_console(console_input)
    write_to_file("Text from console:\n" + console_input + "\n\n")

    file_input = read_from_file()
    print_to_console("\nText from file (built-in Python):")
    print_to_console(file_input)
    write_to_file("Text from file (built-in Python):\n" + file_input + "\n\n")

    pandas_input = read_from_file_pandas()
    print_to_console("\nText from file (pandas):")
    print_to_console(pandas_input)
    write_to_file("Text from file (pandas):\n" + pandas_input)

if __name__ == "__main__":
    main()
