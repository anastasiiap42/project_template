# tests/test_input.py
import pytest
from app.io.input import read_from_file, read_from_file_pandas
import pandas as pd

SAMPLE_TEXT = """This is a test file
With multiple lines
For testing"""

def test_read_from_file_valid_content(tmpdir, monkeypatch):
    """
    Test reading valid content from existing file
    using Python's built-in method
    """
    data_dir = tmpdir.mkdir("data")
    test_file = data_dir.join("input.txt")
    test_file.write(SAMPLE_TEXT)
    
    monkeypatch.chdir(tmpdir)
    
    assert read_from_file() == SAMPLE_TEXT

def test_read_from_file_missing_file(tmpdir, monkeypatch):
    """
    Test handling of missing file in Python built-in method
    """
    monkeypatch.chdir(tmpdir)
    with pytest.raises(FileNotFoundError):
        read_from_file()

def test_read_from_file_empty_file(tmpdir, monkeypatch):
    """
    Test reading empty file using Python built-in method
    """
    data_dir = tmpdir.mkdir("data")
    test_file = data_dir.join("input.txt")
    test_file.write("")
    
    monkeypatch.chdir(tmpdir)
    assert read_from_file() == ""

def test_read_from_file_pandas_valid_content(tmpdir, monkeypatch):
    """
    Test reading valid content with pandas method
    """
    data_dir = tmpdir.mkdir("data")
    test_file = data_dir.join("input.txt")
    test_file.write("first line\nsecond line\nthird line")
    
    monkeypatch.chdir(tmpdir)
    result = read_from_file_pandas()
    assert result == "first line second line third line"

def test_read_from_file_pandas_missing_file(tmpdir, monkeypatch):
    """
    Test handling of missing file in pandas method
    """
    monkeypatch.chdir(tmpdir)
    with pytest.raises(FileNotFoundError):
        read_from_file_pandas()

def test_read_from_file_pandas_empty_file(tmpdir, monkeypatch):
    """
    Test reading empty file using pandas method
    """
    data_dir = tmpdir.mkdir("data")
    test_file = data_dir.join("input.txt")
    test_file.write("")
    
    monkeypatch.chdir(tmpdir)
    assert read_from_file_pandas() == ""
