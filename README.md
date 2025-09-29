# CSV Price Updater

A simple Python tool to update product prices in a CSV file by matching **SKU** values with a reference CSV.  
If a SKU from the main file does not exist in the reference file, its price will be set to `0.00`.

---

## Features

- Reads two CSV files:
  - **Products_selection.csv** → Main product file (must contain `SKU` and `price` columns).
  - **list-price.csv** → Reference file (must contain `SKU` and `price` columns).
- Updates the `price` column in **Products_selection.csv** with values from **list-price.csv**.
- If no price is found for a SKU, defaults to `0.00`.
- Saves changes directly into the **same file** (`Products_selection.csv`).

---

## Example

**Products_selection.csv (before)**
```csv
SKU,Description,price
0,aaaa,
1,sss,
2,ddd,
3,ggg,
4,fff,
5,hhhh,
```
```csv
SKU,price
0,12
1,13
2,35
3,76
4,87
5,59
```

```csv
SKU,Description,price
0,aaaa,12.00
1,sss,13.00
2,ddd,35.00
3,ggg,76.00
4,fff,87.00
5,hhhh,59.00
```

---

## Installation

git clone https://github.com/your-username/csv-price-updater.git
cd csv-price-updater
pip install pandas


---

## Usage
python price_transfer.py Products_selection.csv list-price.csv

Products_selection.csv → main file (will be updated in place)

list-price.csv → reference file (contains SKU + price)


---

## Requirements
Python 3.8+

pandas

