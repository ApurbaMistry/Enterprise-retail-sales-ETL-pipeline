import logging
import os


def clean_data(dataframe):

    logging.info("Starting data cleaning...")

    initial_rows = dataframe.shape[0]

    dataframe = dataframe.drop_duplicates()

    final_rows = dataframe.shape[0]

    removed_rows = initial_rows - final_rows

    logging.info(f"Duplicate rows removed: {removed_rows}")

    # Remove extra spaces from text columns
    object_columns = dataframe.select_dtypes(include="object").columns

    for column in object_columns:
        dataframe[column] = dataframe[column].str.strip()

    logging.info("Extra spaces removed.")

    logging.info("Data cleaning completed.")


    os.makedirs("data/cleaned", exist_ok=True)

    dataframe.to_csv(
        "data/cleaned/cleaned_superstore.csv",
        index=False
    )
    
    logging.info("Cleaned dataset saved successfully.")

    return dataframe