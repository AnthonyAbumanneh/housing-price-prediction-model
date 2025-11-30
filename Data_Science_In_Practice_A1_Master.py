#Importing Pandas Modules
import numpy as np
import pandas as pd

#Preset Settings
pd.options.display.max_rows = 10
pd.options.display.max_columns = 10
pd.set_option('display.precision', 2)

#Read Data With Pandas
df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/candy-power-ranking/candy-data.csv")

#Summarize Data
df.shape
df.head(3)
df.describe()
df.dtypes 

#Find Specific Values
chocolate_values = df['chocolate'].value_counts()

#Missing Data
df.isna().mean #calculate % of missing values in each column
df.dropna(axis='columns') #drops all columns with any missing values
df.dropna(thresh=len(df)*0.9, axis='columns') #drops all columns that more are missing more than 10% of values
df.isna().sum().sum() #counts all mising values in the dataframe
df.isna().any().any() #shows you if there are any missing values
df.isna().any() #shows you what columns have missing data

#Techniques
df_string = df.replace({0: 'is not', 1: 'is'}) #replaces 0 with 'is not' and 1 with 'is'
df_grouped = df.groupby('chocolate') #splits data into one group 
df_grouped = df.groupby('chocolate')['pricepercent'].mean #groups the chocoalte and pricepercent columns and shows you the mean 
sugar_summary = df.groupby('fruity')['Sugarpercent'].agg(['min', 'mean', 'max']) #.agg combines multiple functions

#Manipulating Columns
df.columns['fruity', 'caramel', 'bar', 'winpercent'] #rename columns
#df['new_col'] = df[caramel] * val #creating a new column with an exsting column
#data = data.assign(risk_combo = (data[['gambling', 'speeding']] == "Yes").sum(axis=1))
#(sums up the rows from the two columns where gambling and speeding equal yes)


#Row Operations
df.loc['Al': 'Bob', ['A', 'B']] #selects the rows 'A1' and 'Bob' and returns the 'A' and 'B' columns (slices by labels)
df.iloc[0:5, 0:3] 
#selects the first 5 rows and the first 3 columns(slices by integrers)
#data = data.loc[(data['gambling'] == 'yes') | (data['speeding' == 'yes'])] #Filters data by rows where gambling = yes or where data = yes
df.sort_values(by=['col1, col2']) # sort rows by specific columns
#data = data.sort_values(by=['age'], ascending=False) #another way to sort by a specific column
#data = data.reset_index(drop=True) #creates a new index for thr columns [0,1,2,3,..]
