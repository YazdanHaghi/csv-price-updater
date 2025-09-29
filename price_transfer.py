import pandas as pd

def update_prices(file1, file2, output_file):
    # Read both CSVs
    df1 = pd.read_csv(file1, dtype={"SKU": str})
    df2 = pd.read_csv(file2, dtype={"SKU": str})

    # Ensure SKUs are comparable
    df1["SKU"] = df1["SKU"].astype(str).str.strip()
    df2["SKU"] = df2["SKU"].astype(str).str.strip()

    # Make a mapping from SKU → price
    price_map = df2.set_index("SKU")["price"].to_dict()

    # Update df1.price with values from df2 (default 0.00 if not found)
    df1["price"] = df1["SKU"].map(price_map).fillna(0.00).astype(float)

    # Save back
    df1.to_csv(output_file, index=False, float_format="%.2f", encoding="utf-8-sig")
    print(f"✅ Updated file saved as {output_file}")

# Example
update_prices("Products_selection.csv", "list-price.csv", "output.csv")
