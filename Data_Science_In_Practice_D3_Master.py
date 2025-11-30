''' 
In this study, we aim to answer the following three questions: 
1. Who cheats more on their significant other - males or females? 
2. Are cigarette smokers less likely to skydive?
3. Do people in New England gamble more than other parts of the country?
'''

#Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

#Update visual settings (make plots huge and round all numbers to two decimals)
sns.set(context='poster', style='white')
pd.options.display.precision = 2

#Load, Examine, & Clean data
survey = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/steak-survey/steak-risk-survey.csv')
survey = survey.iloc[1:,2:]
survey.columns = ['smoking','alcohol','gambling',
 'skydiving','speeding', 'cheated',
 'steak', 'steak_preference','gender',
 'age', 'income', 'education', 'region']
survey = survey.dropna(how='all')
survey_preview = survey.head()
# print(survey_preview)

### Question #1: Who cheats more on their significant other - males or females? ###
#To answer, we need to make sure our dataset has the same number of males and femlaes in the dataset 
gender_counts = survey[['gender']].value_counts()
print(gender_counts)
plot_cheated = sns.countplot(data=survey, x='cheated', hue='gender')
# plt.show()

#The data is slightly off because there is more women then men, lets calculate the proportions instead of the raw numbers
prop_df = survey.groupby('gender')['cheated'].value_counts(normalize=True).rename('proportion').reset_index()
print(prop_df)