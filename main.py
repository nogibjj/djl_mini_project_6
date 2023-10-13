"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.load_transform import load
from mylib.complex_query import complex_query

def main():

    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()

    # complex query
    print("Running complex query...")
    complex_query()


if __name__ == "__main__":
    main()