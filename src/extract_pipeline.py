"""
extract_pipeline.py

This module contains functions for extracting specific data from JSON data structures.
It focuses on parsing text blocks to retrieve information related to registration numbers, 
dates, and location details from a JSON format.

Functions:
- data_extraction_from_json: Extracts registration number, print date, and location details from JSON data.
"""

import re
import src.utils as utils
import src.functions as fn

def data_extraction_from_json(json_data):
    
    numero_de_matricula = None
    fecha_de_impresion = None
    departamento = None
    municipio = None
    vereda = None
    estado_del_folio = None
    estado_folio_bool = False

    for i, block in enumerate(json_data.get('Blocks', [])):
        if block['BlockType'] == 'LINE':
            text = block.get('Text', '')
            text = fn.fix_encoding(text)  # Attempts to fix encoding issues
            text = fn.replace_accents(text)  # Replaces accented vowels with unaccented vowels
            
            # 1. Search numero_de_matricula. Key: 'nro matrícula:'
            match = re.search(r'\bnro\s+matricula[:\s]*([^\s]+)', text, re.IGNORECASE)
            if match:
                    numero_de_matricula = match.group(1).strip()
            
            
            # 2. Search fecha_de_impresion. Key: 'impreso el [día] de [mes] de [año]'
            date_pattern = re.compile(r'impreso el\s(\d{1,2})\sde\s(\w+)\sde\s(\d{4})', re.IGNORECASE)
            match = date_pattern.search(text.lower())
            if match:
                    day, month, year = match.group(1), match.group(2), match.group(3)
                    month_number = utils.month_encoding.get(month.lower(), '01')
                    fecha_de_impresion = f"{year}-{month_number}-{int(day):02d}"
                    
            # 3. Search localization. Key: 'circulo registral: [dato] depto: [dato] municipio: [dato] vereda: [dato]'
            loc_pattern = (
                        r'circulo\sregistral:\s*[\w\s-]+.*?'
                        r'depto:\s*([^\s]+(?:\s+[^\s]+)*)'    
                        r'.*?'                               
                        r'municipio:\s*([^\s]+(?:\s+[^\s]+)*)'  
                        r'.*?'                               
                        r'vereda:\s*([^\s]+(?:\s+[^\s]+)*)'  
                    )
            localization_pattern = re.compile(loc_pattern, re.IGNORECASE)
            match = localization_pattern.search(text)
            if match:
                    departamento = match.group(1).strip()
                    municipio = match.group(2).strip()
                    vereda = match.group(3).strip()
            # 4. Search estado del folio. Key: 'estado del folio'
            if 'estado del folio' in text.lower():
                    estado_folio_bool = True

            if estado_folio_bool:
                if i + 1 < len(json_data['Blocks']):
                    next_block = json_data['Blocks'][i + 1]
                    if next_block['BlockType'] == 'LINE':
                        estado_del_folio = next_block.get('Text', '').strip()
                        estado_folio_bool = False
    
    return {
            'Numero_de_matricula': numero_de_matricula,
            'Fecha_de_impresion': fecha_de_impresion,
            'Departamento': departamento,
            'Municipio': municipio,
            'Vereda': vereda,
            'Estado_de_folio': estado_del_folio  
        }