"""
File: extract.py

Purpose:
Reads the raw retail sales CSV dataset
and returns a Pandas DataFrame.
"""

import logging
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_data(file_path):

    logging.info("Reading dataset...")

    dataframe = pd.read_csv(file_path)

    logging.info("Dataset loaded successfully.")

    return dataframe