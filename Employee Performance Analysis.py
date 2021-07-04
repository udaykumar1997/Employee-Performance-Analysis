#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 

# To read the dataset
stu=pd.read_csv(‘EmployeePerformance.csv’,sep=’,’)
stu.head()

stu.shape

# To represent the summary of the dataframe
stu.info()

# To display the column index
stu.columns

 

# To display male and female count
stu[‘gender’].value_counts()

 

# To show the Gender bar plot
sns.set(style=’whitegrid’)
sns.barplot(x=stu[‘gender’].value_counts().index,y=stu[‘gender’].value_counts().values,hue=[‘female’,’male’])
plt.legend(loc=8)
plt.xlabel(‘gender’)
plt.ylabel(‘Frequency’)
plt.title(‘Show of Gender Bar Plot’)
plt.show()

 

stu[‘race/ethnicity’].value_counts()

 

# To show the Race/Ethicity bar plot
plt.figure(figsize=(8,5))
sns.barplot(x=stu[‘race/ethnicity’].value_counts().index, y=stu[‘race/ethnicity’].value_counts().values)
plt.xlabel(‘Race/Ethnicity’)
plt.ylabel(‘Frequency’)
plt.title(‘Show of Race/Ethnicity Bar Plot’)
plt.show()

 

# To visualize the comparison of math scores
stu[‘math score’].value_counts(normalize = True)
stu[‘math score’].value_counts(dropna = False).plot.bar(figsize = (18, 10))
plt.title(‘Comparison of math scores’)
plt.xlabel(‘score’)
plt.ylabel(‘count’)
plt.show()

 

# To visualize the comparison of math scores

stu[‘reading score’].value_counts(dropna = False).plot.bar(figsize = (18, 10), color = ‘red’)
plt.title(‘Comparison of math scores’)
plt.xlabel(‘score’)
plt.ylabel(‘count’)
plt.show()