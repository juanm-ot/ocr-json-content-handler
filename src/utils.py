"""
utils.py

This module contains auxiliary functions and data structures used throughout the project. 
It provides utility functions and constant values that are intended to simplify and standardize various operations.

Contents:
- month_encoding: A dictionary for encoding month names into their corresponding numeric values.
"""

numero_de_matricula = None
fecha_de_impresion = None
departamento = None
municipio = None
vereda = None
estado_del_folio = None
estado_folio_bool = False
    
month_encoding = {
                'enero': '01', 
                'febrero': '02', 
                'marzo': '03', 
                'abril': '04',
                'mayo': '05', 
                'junio': '06', 
                'julio': '07', 
                'agosto': '08',
                'septiembre': '09', 
                'octubre': '10', 
                'noviembre': '11', 
                'diciembre': '12'
                }

extracted_data = {
            'Numero_de_matricula': numero_de_matricula,
            'Fecha_de_impresion': fecha_de_impresion,
            'Departamento': departamento,
            'Municipio': municipio,
            'Vereda': vereda,
            'Estado_de_folio': estado_del_folio  
        }
