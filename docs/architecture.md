# Enterprise Retail Sales ETL Pipeline Architecture

                +----------------------+
                |  superstore.csv      |
                | (Raw CSV Dataset)    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    extract.py        |
                |  Read CSV File       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   validate.py        |
                | Data Validation      |
                | - Null Check         |
                | - Duplicate Check    |
                | - Data Types         |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     clean.py         |
                | Data Cleaning        |
                | - Remove Duplicates  |
                | - Remove Spaces      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   transform.py       |
                | Business Features    |
                | - Profit Margin      |
                | - Sales Category     |
                | - Discount Category  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      load.py         |
                | Load to SQLite       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | retail_sales.db      |
                | SQLite Database      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     report.py        |
                | Business Reports     |
                +----------+-----------+
                           |
                           v
        +------------------------------------------+
        | cleaned_superstore.csv                   |
        | business_report.txt                      |
        +------------------------------------------+