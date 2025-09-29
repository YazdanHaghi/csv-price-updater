import pandas as pd

def read_csv_robust(path):
    # Try common encodings and delimiters
    encodings = ["utf-8-sig", "utf-8", "cp1252", "latin1"]
    seps = [None, ",", ";"]  # None lets pandas sniff
    last_err = None
    for enc in encodings:
        for sep in seps:
            try:
                return pd.read_csv(path, dtype={"SKU": str}, encoding=enc, sep=sep, engine="python")
            except Exception as e:
                last_err = e
                continue
    raise last_err

def update_prices_inplace(file1, file2):
    df1 = read_csv_robust(file1)
    df2 = read_csv_robust(file2)

    # Normalize column names
    df1.columns = [c.strip() for c in df1.columns]
    df2.columns = [c.strip() for c in df2.columns]

    # Validate required columns
    if "SKU" not in df1.columns or "price" not in df1.columns:
        raise ValueError(f"{file1} must have columns: SKU, price")
    if "SKU" not in df2.columns or "price" not in df2.columns:
        raise ValueError(f"{file2} must have columns: SKU, price")

    # Clean SKUs
    df1["SKU"] = df1["SKU"].astype(str).str.strip()
    df2["SKU"] = df2["SKU"].astype(str).str.strip()

    # Create mapping from file2
    price_map = df2.set_index("SKU")["price"].apply(pd.to_numeric, errors="coerce").to_dict()

    # Update file1 prices
    df1["price"] = df1["SKU"].map(price_map).fillna(0.00).astype(float)

    # Save back to the SAME file
    df1.to_csv(file1, index=False, float_format="%.2f", encoding="utf-8-sig")
    print(f"✅ Prices updated directly in {file1}")

# Example usage
update_prices_inplace("Products_selection.csv", "list-price.csv")
