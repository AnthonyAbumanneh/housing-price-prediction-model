import pandas as pd
df = pd.read_csv('startups_funding_dataset_2024_2025.csv')

df_preview = df.head(3)
#print(df_preview)

df_summary = df.describe()
df_value_types = df.dtypes
df_shape = df.shape
#print(df_summary)
#print(df_value_types)
#print(df_shape)

startup_names = df['Startup Name']
#print(startup_names)

find_missing_columns = df.isna().any().any()
#print(find_missing_columns)

Usa_funding_stats = df.loc[(df['Country'] == 'USA')]
USA_funding_stats_only = Usa_funding_stats.sort_values(by=['Raised Amount (USD)'], ascending=False)
USA_funding_stats_only = USA_funding_stats_only.reset_index(drop=True)
Final_Visualization = USA_funding_stats_only[['Startup Name', 'Country', 'Raised Amount (USD)']]
print(Final_Visualization)
USA_Comapany_Avg_Funding = Final_Visualization['Raised Amount (USD)'].mean()
print(USA_Comapany_Avg_Funding )

#Try to compare & graph the usa average funding vs average funding for other countries 