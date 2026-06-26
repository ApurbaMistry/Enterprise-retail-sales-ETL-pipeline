import logging


def transform_data(dataframe):

    logging.info("Starting data transformation...")

    dataframe["Profit Margin"] = (
        dataframe["Profit"] / dataframe["Sales"]
    ) * 100

    logging.info("Profit Margin column created.")

    dataframe["Sales Category"] = "Low"

    dataframe.loc[dataframe["Sales"] >= 500, "Sales Category"] = "Medium"
    
    dataframe.loc[dataframe["Sales"] >= 1000, "Sales Category"] = "High"
    
    logging.info("Sales Category column created.")


    dataframe["Discount Category"] = "No Discount"

    dataframe.loc[dataframe["Discount"] > 0, "Discount Category"] = "Discount Applied"
    
    logging.info("Discount Category column created.")

    logging.info("Data transformation completed.")

    return dataframe