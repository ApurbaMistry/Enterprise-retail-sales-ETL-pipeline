import logging


def validate_data(dataframe):

    logging.info("Starting data validation...")

    logging.info(f"Rows: {dataframe.shape[0]}")
    logging.info(f"Columns: {dataframe.shape[1]}")

    # Check Null Values
    null_values = dataframe.isnull().sum()

    print("\nNull Value Report")
    print(null_values)

    duplicate_rows = dataframe.duplicated().sum()

    logging.info(f"Duplicate Rows: {duplicate_rows}")
    

    logging.info("Data validation completed.")

    return dataframe