"""
functions.py

This module provides utility functions for retrieving and processing content from various sources. 
It includes functions for fetching content from URLs or local files and for loading JSON data.

Functions:
- retrieve_content: Fetches content from a specified URL or reads it from a local file.
- load_json: Loads and parses JSON data from a URL or local file
"""

import json
import requests

def retrieve_content(file_path):
    """
    Retrieves the content from a URL or reads it from a local file.

    Parameters:
    file_path (str): The path to the local file or the URL.

    Returns:
    str: The content of the file or URL as a string.

    Raises:
    FileNotFoundError: If the local file is not found.
    ValueError: If there is an error retrieving data from the URL.
    """
    try:
        if file_path.startswith(('http://', 'https://')):
            response = requests.get(file_path)
            response.raise_for_status()
            return response.text
        else:
            with open(file_path, 'r') as file:
                return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found")
    except requests.RequestException as e:
        raise ValueError(f"Error retrieving data from URL: {e}")
    
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
    