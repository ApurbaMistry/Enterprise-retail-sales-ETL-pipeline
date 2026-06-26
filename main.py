from scripts.extract import extract_data
from scripts.validate import validate_data
from scripts.clean import clean_data
from scripts.transform import transform_data
from scripts.load import load_data


def main():

    file_path = "data/raw/superstore.csv"

    dataframe = extract_data(file_path)

    dataframe = validate_data(dataframe)

    dataframe = clean_data(dataframe)

    dataframe = transform_data(dataframe)

    load_data(dataframe)

    print(dataframe.head())

    


if __name__ == "__main__":
    main()