import pandas as pd
df = pd.read_csv("../data/sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
print("===ACCURACY CHECK===")
negative_prices = (df["price"]<0).sum()

assert (df["price"] >=0).all()

current_date = pd.Timestamp.now()
future_date_count = (df["date"]> current_date).sum()

print(f"Negative Prices: {negative_prices}")
print(f"Number of Future Dates: {future_date_count}")


print("===CONSISTENCY CHECK===")
unique_products = df["product"].nunique()
unique_count= df["product"].nunique()
print("Unique products: {unique_products}")
print("Count of unique products: {unique_count}")

print("===COMPLETENESS CHECK===")
missing_values = df.isnull().sum()
completeness = df.notnull().mean().mean()*100
print("Missing Values: {missing_values}")
print(f"Overall completeness rate: {completeness:.1f}%")

