from scripts.extract import extract_data


def main():

    file_path = "data/raw/superstore.csv"

    dataframe = extract_data(file_path)

    


if __name__ == "__main__":
    main()