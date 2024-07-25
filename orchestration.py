import os
import logging
from dotenv import load_dotenv
import pandas as pd
import src.functions as fn 
import src.extract_pipeline as extract

load_dotenv()

input_path = os.getenv("input_path")
output_path = os.getenv("output_path")

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s - %(message)s')

def run_pipeline():
    
    logging.info("Process initiated...")
    try:
        
        json_files = [f for f in os.listdir(input_path) if f.endswith('.json')]
        
        if not json_files:
            logging.warning("No JSON files found in the input directory.")
            return
        
        all_data = []
        
        logging.info("Processing %d JSON files...", len(json_files))
        
        for json_file in json_files:
            file_path = os.path.join(input_path, json_file)
            logging.info("Loading JSON data from: %s", file_path)
            json_data = fn.load_json(file_path)
            logging.info("JSON data successfully loaded from: %s", file_path)
        
            logging.info("Starting data extraction pipeline...")
            extracted_data = extract.data_extraction_from_json(json_data)
            logging.info("Data extraction completed for file: %s", json_file)
            
            all_data.append(extracted_data)
        
        logging.info("Converting extracted data into a DataFrame...")
        df = pd.DataFrame(all_data)
        logging.info("Data successfully converted into DataFrame")
        
        logging.info("Saving DataFrame to CSV at: %s", output_path)
        df.to_csv(output_path, index=False)
        logging.info("DataFrame successfully saved to CSV")
        
    except Exception as e:
        logging.error("An error occurred during the process: %s", str(e))

if __name__ == "__main__":
    run_pipeline()