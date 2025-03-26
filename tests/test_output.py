import pytest
from app.io.output import print_to_console, write_to_file
import io
import sys

def test_print_to_console(capsys):
    """
    Test that print_to_console correctly outputs to console
    """
    test_text = "Hello, World!"
    print_to_console(test_text)
    captured = capsys.readouterr()
    assert captured.out == test_text + "\n"

def test_print_to_console_empty_string(capsys):
    """
    Test print_to_console with an empty string
    """
    print_to_console("")
    captured = capsys.readouterr()
    assert captured.out == "\n"

def test_print_to_console_non_string(capsys):
    """
    Test print_to_console with a non-string input
    """
    print_to_console(42)
    captured = capsys.readouterr()
    assert captured.out == "42\n"

def test_write_to_file(tmpdir):
    """
    Test that write_to_file correctly writes content to a file
    """
    test_text = "This is a test file content."
    file_path = tmpdir.join("test_output.txt")
    write_to_file(test_text, str(file_path))
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    assert content == test_text

def test_write_to_file_empty_string(tmpdir):
    """
    Test write_to_file with an empty string
    """
    file_path = tmpdir.join("empty_output.txt")
    write_to_file("", str(file_path))
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    assert content == ""

def test_write_to_file_overwrite(tmpdir):
    """
    Test that write_to_file overwrites existing file content
    """
    file_path = tmpdir.join("overwrite_output.txt")
    
    write_to_file("Initial content", str(file_path))
    
    new_content = "New content" # overwrite with new content
    write_to_file(new_content, str(file_path))
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    assert content == new_content
