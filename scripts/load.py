import logging
import sqlite3


def load_data(dataframe):

    logging.info("Starting database loading...")

    connection = sqlite3.connect("database/retail_sales.db")

    dataframe.to_sql(
        "sales",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    logging.info("Data loaded into SQLite successfully.")