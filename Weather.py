#The dataset I am using is a time-series dataset that provides monthly weather statistics for a particular location.
# It records information such as:
#Temperature (tem): The average temperature for the month.
#Month (Month): The month of the year (1–12).
#Year (Year): The year of observation.
#Rain: The total rainfall in millimeters for the month.
#This data is stored in a CSV file and spans multiple years, making it a useful dataset for analyzing trends and patterns in weather over time.
# I will perform various analyses using the Pandas DataFrame library to gain insights into temperature variations,
# rainfall distributions, and relationships between different variables.

import pandas as pd
data = pd.read_csv(r"C:\Users\Abir\OneDrive\Desktop\Rashna's Document\Project_BIA\weather\sorted_temp_and_rain_dataset.csv")
print(data)

# how to Analyze DataFrame
# .head it shows first numbers [N] of rows in the data[by default [N = 5 ] .
# I am going to show 1st 10
print(data.head(10))

#.shape it shows the total no. of rows and columns of the dataframe.
print(data.shape)

#.index this attribute provide the index of the dataframe
print(data.index)

#.columns it shows the name of each column
print(data.columns)

#.dtypes it shows the data-type of each column
print(data.dtypes)

#.unique in a column it shows all the unique values.
# it can be applied on a single column only. Not on the whole dataframe.
month_mapping = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}
# Convert the 'Month' column to string using map
data['Month'] = data['Month'].map(month_mapping)
# Display the updated DataFrame
print(data)
# Show unique values in the 'Month' column
unique_months = data['Month'].unique()
# Print the unique months
print("Unique months in the dataset:")
print(unique_months)

#.nunique it shows the total no. of unique values in each column.
# it can be applied on a single column as well as on whole dataframe.
unique_month_count = data['Month'].nunique()

# Print the count of unique months
print("Number of unique months in the dataset:")
print(unique_month_count)

#.count it shows the total no. of non-null in each column.
#it can be applied on a single column as well as on whole dataframe.
print(data.count())

#.value_counts in a column it shows all the unique valus with their count.
# it can be applied on a single column only.
print(data['Month'].value_counts())

#.info provides bsic information about the dataframe
print(data.info)

#Find all the unique rain values in the data.
print(data.head(2))
print(data['rain'].nunique())
print(data['rain'].unique())

#Find the number of times when the rain is exactly 0.
count_zero_rain = (data['rain'] == 0).sum() #.Sum Counts the number of True values in the Boolean Series.
print("The number of times rain is exactly 0 is: " + str(count_zero_rain))

#Find the number of times when the tem was exactly 25°C.
count_tem_25 = (data['tem'] == 25).sum()
print(f'The number of times when the tem was exactly 25°C is: {count_tem_25}')

#Find out all the Null values in the data.
null_values = data.isnull().sum()
print('Number of null values in each column:')
print(null_values)

#Rename the column rain to Rainfall.
data.rename(columns={'rain': 'Rainfall'}, inplace= True)
print('Updated Column:')
print(data.columns)

#What is the Standard Deviation of rain in this data?
rainfall_std = data['Rainfall'].std() #the .std()function in pandas calculate the sample standard deviation by default
print(f'The Standard Deviation of rain in this data is: {rainfall_std}')

#What is the Variance of tem in this data?
tem_variance = data['tem'].var() #the .var()function calculates the sample varience by default
print(f'The variance of the tem in this data is: {tem_variance}')

#Find all instances when rain was greater than 100 mm.
rain_above_100 = data[data['Rainfall']>100]
print('All instance where rainfall was greater than 100 mm')
print(rain_above_100)

#Find all instances when tem is above 30°C and rain is below 50 mm.
tem_above_30 = data[data['tem'] > 30]
print("Instances where tem > 30°C:")
print(tem_above_30)
rain_below_50 = data[data['Rainfall'] < 50]
print("Instances where Rainfall < 50 mm:")
print(rain_below_50)

#What is the mean value of each column grouped by Month?
mean_by_month = data.groupby('Month').mean() #.groupby() groups the dataset and. mean() computes the mean for each numaric column within each group
print('Mean value of each column grouped by month:')
print(mean_by_month)

#What is the Minimum & Maximum value of each column grouped by Year?
min_by_year = data.groupby('Year').min()
max_by_year = data.groupby('Year').max()
print("Minimum value of each column grouped by Year:")
print(min_by_year)
print("Maximum value of each column grouped by Year:")
print(max_by_year)

#Show all the records where rain is exactly 0.
record_zero = data[data['Rainfall'] == 0]
print('All records where Rainfall is exactly 0:')
print(record_zero)

#Find all instances when tem is above 35°C or rain is above 200 mm.
tem_or_rain_condition = data[(data['tem']>35)| (data['Rainfall']>200)]
print("All instances where tem is above 35°C or Rainfall is above 200 mm:")
print(tem_or_rain_condition)

#Find all instances when:
#tem is above 30°C and rain is greater than 100 mm, or tem is below 10°C.
complex_condition = data[((data['tem'] > 30) & (data['Rainfall'] > 100)) | (data['tem'] < 10)]
print(complex_condition)

