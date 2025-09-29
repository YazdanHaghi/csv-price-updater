# CSV Price Updater

A simple Python tool to update product prices in a CSV file by matching **SKU** values with a reference CSV.  
If a SKU from the main file does not exist in the reference file, its price will be set to `0.00`.

---

## Features

- Reads two CSV files:
  - **File 1** → Main product file (must contain `SKU` and `price` columns).
  - **File 2** → Reference file (must contain `SKU` and `price` columns).
- Updates the `price` column in File 1 with values from File 2.
- If no price is found for a SKU, defaults to `0.00`.
- Outputs the updated CSV.

---

## Example

**file1.csv**

SKU,Description,price
0,aaaa,
1,sss,
2,ddd,
3,ggg,
4,fff,
5,hhhh,

**file2.csv**
SKU,price
0,12
1,13
2,35
3,76
4,87
5,59
**output.csv**
SKU,Description,price
0,aaaa,12.00
1,sss,13.00
2,ddd,35.00
3,ggg,76.00
4,fff,87.00
5,hhhh,59.00


## Installation

Clone this repo and install dependencies:

git clone https://github.com/your-username/csv-price-updater.git
cd csv-price-updater
pip install pandas

## Usage

Run the script from the command line:

python price_transfer.py file1.csv file2.csv output.csv



