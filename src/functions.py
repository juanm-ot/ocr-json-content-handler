"""
functions.py

This module provides utility functions for retrieving and processing content from various sources. 
It includes functions for fetching content from URLs or local files, loading JSON data, fixing encoding issues, 
and replacing accented characters.

Functions:

- fix_encoding: Attempts to fix encoding issues by converting text from 'latin1' to 'utf-8'.
- load_json: Loads and parses JSON data from a URL or local file.
- replace_accents: Replaces accented characters in the given text with their unaccented equivalents.
- retrieve_content: Fetches content from a specified URL or reads it from a local file.

The functions are listed in alphabetical order
"""

import json
import requests

def fix_encoding(text):
    """
    Attempts to fix encoding issues by converting the text from 'latin1' to 'utf-8'.

    Parameters:
    text (str): The input string that may contain encoding issues.

    Returns:
    str: The text after attempting to fix encoding issues.

    Notes:
    This function tries to encode the text to 'latin1' and then decode it to 'utf-8'. If a UnicodeEncodeError is encountered, 
    the function will simply return the original text.
    """
    try:
        text = text.encode('latin1').decode('utf-8')
    except UnicodeEncodeError:
        pass
    return text

def load_json(file_path):
    """
    Loads data from a JSON file or URL.

    Parameters:
    file_path (str): The path to the JSON file or URL to be loaded.

    Returns:
    dict: A dictionary containing the loaded data.
    
    Raises:
    ValueError: If there is an error parsing the JSON content.
    """
    try:
        content = retrieve_content(file_path)
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON content: {e}")

def replace_accents(text):
    """
    Replaces accented characters in the given text with their unaccented equivalents.

    Parameters:
    text (str): The input string containing accented characters.

    Returns:
    str: A new string with accented characters replaced by their unaccented equivalents.
    """
    replacements = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }
    for accented_char, unaccented_char in replacements.items():
        text = text.replace(accented_char, unaccented_char)
    return text

def retrieve_content(file_path):
    """
    Reads the content from a local file.

    Parameters:
    file_path (str): The path to the local file.

    Returns:
    str: The content of the file as a string.

    Raises:
    FileNotFoundError: If the local file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found")
    
