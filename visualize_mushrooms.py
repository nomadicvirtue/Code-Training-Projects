import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

#for i in columns:
for col in df:
  if df[col].str.count('\w').sum() > 6:
    sns.countplot(df[col], order=df[col].value_counts(ascending=True).index)
  else:
    plt.pie(df[col])
   # rotates the value labels slightly so they don’t overlap, also slightly increases font size
  plt.xticks(rotation=30, fontsize=10)
   # increases the variable label font size slightly to increase readability
  plt.xlabel(col, fontsize=10)
  plt.title(col  + ' Value Counts')
  plt.show()
  plt.clf()
  #print(i)










