import pandas as pd

# Convert data files to dataframes
df1 = pd.read_csv(r"C:\Users\jahag\OneDrive\Desktop\repos\quantium-starter-repo\data\daily_sales_data_0.csv")
df2 = pd.read_csv(r"C:\Users\jahag\OneDrive\Desktop\repos\quantium-starter-repo\data\daily_sales_data_1.csv")
df3 = pd.read_csv(r"C:\Users\jahag\OneDrive\Desktop\repos\quantium-starter-repo\data\daily_sales_data_2.csv")

# Combine all dataframes into one single dataframe
combined_df = pd.concat([df1,df2,df3], ignore_index=True)

# Filter combined_df having product as 'pink morsel'
filter_by_pink_morsel_df = combined_df[combined_df["product"] == "pink morsel"]

final_df = filter_by_pink_morsel_df.drop(columns=["product"])
final_df["sales"] = final_df["price"] * final_df["quantity"]
final_df = final_df.drop(columns=["price", "quantity"])

print(final_df.info())