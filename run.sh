#!/bin/bash

VENV_NAME="ocr-json-extract"

python3 -m venv $VENV_NAME # Create the virtual environment

# Detect the operating system and activate the virtual environment
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    # Linux or macOS
    source $VENV_NAME/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source $VENV_NAME/Scripts/activate
else
    echo "Unsupported operating system"
    exit 1
fi

echo "Creating the virtual environment, installing dependencies..."
pip install --upgrade pip # Update pip
pip install -r requirements.txt # Install dependencies
echo "The virtual environment has been successfully created and is now activated"

echo "The orchestration process of the project will begin"
python orchestration.py # Run main script
echo "Data extracting completed successfully"

deactivate # close env