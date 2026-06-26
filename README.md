# 🛒 Enterprise Retail Sales ETL Pipeline with Automated Data Validation

A professional **Enterprise Retail Sales ETL Pipeline** built using **Python, Pandas, NumPy, SQLite, SQL, and Logging**. The pipeline extracts retail sales data from a CSV file, performs automated data validation and cleaning, transforms the data into business-ready information, loads it into a SQLite database, and generates business reports.

---

# 📌 Project Overview

This project demonstrates a complete **ETL (Extract → Transform → Load)** workflow used in Data Engineering.

The pipeline performs:

* Extract retail sales data from a CSV file
* Validate data quality automatically
* Clean invalid and duplicate records
* Transform raw data into business metrics
* Load processed data into SQLite
* Generate business reports
* Export cleaned datasets

---

# 🚀 Features

* CSV Data Extraction
* Automated Data Validation
* Duplicate Detection
* Null Value Validation
* Data Type Validation
* Data Cleaning
* Text Standardization
* Business Data Transformation
* SQLite Database Loading
* SQL Analytics Queries
* Business Report Generation
* CSV Export
* Python Logging
* Exception Handling
* Modular Project Structure

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQL
* CSV
* Python Logging Module
* Git
* GitHub

---

# 📂 Project Structure

```text
enterprise-retail-sales-etl-pipeline/

│── data/
│   ├── raw/
│   ├── cleaned/
│   └── exports/

│── database/

│── docs/
│   ├── architecture.md
│   └── screenshots/

│── logs/

│── scripts/
│   ├── extract.py
│   ├── validate.py
│   ├── clean.py
│   ├── transform.py
│   ├── load.py
│   └── report.py

│── sql/
│   └── business_queries.sql

│── main.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

# 🏗 ETL Pipeline Architecture

```
CSV Dataset
      │
      ▼
Extract
      │
      ▼
Validate
      │
      ▼
Clean
      │
      ▼
Transform
      │
      ▼
Load into SQLite
      │
      ▼
Business Reports
```

For the detailed architecture diagram, see:

```
docs/architecture.md
```

---

# 📸 Project Screenshots

### Project Structure

```
docs/screenshots/project_structure.png
```

### Pipeline Execution

```
docs/screenshots/pipeline_execution_part1.png
docs/screenshots/pipeline_execution_part2.png
```

### SQLite Database

```
docs/screenshots/sqlite_database.png
```

### Generated Output Files

```
docs/screenshots/output_files.png
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/ApurbaMistry/Enterprise-retail-sales-ETL-pipeline.git
```

Move into the project:

```bash
cd Enterprise-retail-sales-ETL-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

# 📊 Data Validation

The pipeline performs automatic validation including:

* Row Count Validation
* Column Count Validation
* Null Value Detection
* Duplicate Record Detection
* Data Type Validation

---

# 🧹 Data Cleaning

Cleaning operations include:

* Duplicate Removal
* Text Standardization
* Whitespace Removal

---

# 🔄 Data Transformation

Business transformations include:

* Profit Margin Calculation
* Sales Category Generation
* Discount Category Generation

---

# 🗄 Database

Processed data is loaded into a SQLite database.

Database:

```
database/retail_sales.db
```

Table:

```
sales
```

---

# 📈 Business Reports

The project automatically generates:

* Total Sales
* Total Profit
* Average Sales
* Highest Sale
* Lowest Sale
* Total Orders

Reports are exported to:

```
data/exports/business_report.txt
```

---

# 📁 Generated Outputs

The ETL pipeline generates:

```
data/cleaned/cleaned_superstore.csv

data/exports/business_report.txt

database/retail_sales.db
```

---

# 📜 SQL Analytics

Business SQL queries are available in:

```
sql/business_queries.sql
```

These queries demonstrate common analytical operations including:

* Total Sales
* Total Profit
* Average Sales
* Sales by Category
* Profit by Region
* Top Selling Records

---

# 🚀 Future Improvements

Potential enhancements include:

* PostgreSQL Integration
* Apache Airflow Scheduling
* Docker Deployment
* Cloud Storage Support
* Automated Email Reports
* Interactive Dashboard

---

# 👨‍💻 Author

**Apurba Mistry**

Aspiring Data Engineer | Python | SQL | Pandas | NumPy | SQLite | ETL Development
