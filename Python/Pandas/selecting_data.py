import pandas as pd

# Sample DataFrame
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print("Original DataFrame:")
print(df)

selected_columns = df[['Name', 'Salary']]
print("\nSelected Columns:")
print(selected_columns)

print("\nDataFrame Info:")
df.info()


print("\nType of selected_columns:")
print(type(selected_columns))

'''
Output:
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Name        4 non-null      object
 1   ID          4 non-null      int64 
 2   Department  4 non-null      object
 3   Salary      4 non-null      int64 
dtypes: int64(2), object(2)
memory usage: 256.0+ bytes

Type of selected_columns:
<class 'pandas.core.frame.DataFrame'>'''