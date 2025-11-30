### GOALS: 1. Find average prices per neighborhood.      2. Compare entire home vs private room prices.  
import kagglehub
import os
import pandas as pd

os.system('clear')

# Download latest version
path = kagglehub.dataset_download("dominoweir/inside-airbnb-nyc")

#print("Path to dataset files:", path)

#print(os.listdir(path))

dataset = os.path.join(path, "listings.csv" )
df = pd.read_csv(dataset)
columns = df.columns
print(columns)
#mising_columns = print(df.isna().sum().sum())

data_preview = df.head()
#print(data_preview)
Important_columns = df[['name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'price', 'room_type']]
Important_missing_columns = Important_columns.isna().any
#print(Important_missing_columns)
Cleaner_data = Important_columns.dropna(axis='columns')
#print(Cleaner_data)

Avg_neighborhood_price = Cleaner_data.groupby('neighbourhood')['price'].mean()
print(Avg_neighborhood_price)

Home_renters_data = Cleaner_data[Cleaner_data['room_type'] == 'Entire home/apt']
Room_renters_data = Cleaner_data[Cleaner_data['room_type'] == 'Private room']
Avg_Home_price = Home_renters_data['price'].agg(['mean', 'median'])
Avg_Room_price = Room_renters_data['price'].agg(['mean', 'median'])
print(Avg_Home_price)
print(Avg_Room_price)