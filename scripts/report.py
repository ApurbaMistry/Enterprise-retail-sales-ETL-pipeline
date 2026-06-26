import logging
import os


def generate_report(dataframe):

    logging.info("Generating business report...")

    total_sales = dataframe["Sales"].sum()
    total_profit = dataframe["Profit"].sum()
    average_sales = dataframe["Sales"].mean()
    highest_sale = dataframe["Sales"].max()
    lowest_sale = dataframe["Sales"].min()
    total_orders = len(dataframe)

    print("\n========== BUSINESS REPORT ==========")
    print(f"Total Sales      : {total_sales:,.2f}")
    print(f"Total Profit     : {total_profit:,.2f}")
    print(f"Average Sales    : {average_sales:,.2f}")
    print(f"Highest Sale     : {highest_sale:,.2f}")
    print(f"Lowest Sale      : {lowest_sale:,.2f}")
    print(f"Total Orders     : {total_orders}")

    os.makedirs("data/exports", exist_ok=True)

    with open("data/exports/business_report.txt", "w") as file:

        file.write("BUSINESS REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Total Sales      : {total_sales:,.2f}\n")
        file.write(f"Total Profit     : {total_profit:,.2f}\n")
        file.write(f"Average Sales    : {average_sales:,.2f}\n")
        file.write(f"Highest Sale     : {highest_sale:,.2f}\n")
        file.write(f"Lowest Sale      : {lowest_sale:,.2f}\n")
        file.write(f"Total Orders     : {total_orders}\n")

    logging.info("Business report exported successfully.")