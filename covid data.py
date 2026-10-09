import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('owid-covid-data.csv')
print(df.head())
print(df.info())
print(df.describe())
continent_data = df.groupby('continent')['total_cases'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=continent_data, x='continent', y='total_cases')
plt.show()
continent_data = df.groupby('continent')['total_cases'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.pie(continent_data['total_cases'], labels=continent_data['continent'], autopct='%1.1f%%')
plt.show()
continent_data = df.groupby('continent')['total_cases'].sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(continent_data['total_cases'], labels=continent_data['continent'], autopct='%1.1f%%', startangle=140)
plt.title('Total COVID Cases by Continent')
plt.show()
plt.figure(figsize=(10, 6))
sns.histplot(df['aged_70_older'].dropna(), bins=20, kde=True)
plt.title('Age Distribution (70+ years)')
plt.xlabel('Percentage of Population 70+')
plt.ylabel('Count')
plt.show()
corr_matrix = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()



