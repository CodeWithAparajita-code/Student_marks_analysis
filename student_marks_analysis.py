import pandas as pd
import numpy as np
# Load the dataset
df = pd.read_csv('StudentsPerformance.csv')
# Standardize column names (remove spaces, lowercase)
df.columns = df.columns.str.strip().str.lower().str.replace('/', '_').str.replace(' ', '_')
# Drop rows with missing values in the score columns
df.dropna(subset=['math_score', 'reading_score', 'writing_score'], inplace=True)

# Calculate Average, Max, and Min scores
math_avg = np.mean(df['math_score'])
math_max = np.max(df['math_score'])
math_min = np.min(df['math_score'])

reading_avg = np.mean(df['reading_score'])
reading_max = np.max(df['reading_score'])
reading_min = np.min(df['reading_score'])

writing_avg = np.mean(df['writing_score'])
writing_max = np.max(df['writing_score'])
writing_min = np.min(df['writing_score'])

# Calculate overall average score for each student
df['average_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

# Display Results
print("--- DATASET SUMMARY ---")
print(df.head())

print("\n--- SCORE STATISTICS ---")
stats_df = pd.DataFrame({
    'Metric': ['Average', 'Maximum', 'Minimum'],
    'Math': [math_avg, math_max, math_min],
    'Reading': [reading_avg, reading_max, reading_min],
    'Writing': [writing_avg, writing_max, writing_min]
})

print(stats_df.to_string(index=False))