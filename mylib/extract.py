"""
Extract a dataset from a URL 
"""
import requests
import pandas as pd
import io

def extract(url1="https://github.com/jjsantos01/aire_cdmx/raw/master/datos/contaminantes_2019-05-16.cvs", 
            url2="https://github.com/jjsantos01/aire_cdmx/raw/master/datos/contaminantes_2019-05-17.cvs",
            file_path1="data/air_pol_16.csv",
            file_path2="data/air_pol_17.csv"):
    """ "Extract a url to a file path"""
    with requests.get(url1, timeout=10) as r:
        with open(file_path1, "wb") as f:
            f.write(r.content)
    with requests.get(url1, timeout=10):
        with open(file_path1, "wb") as f:
            f.write(r.content) 
    return file_path1 file_path2

extract()