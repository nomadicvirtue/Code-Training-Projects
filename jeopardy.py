import pandas as pd
pd.set_option('display.max_colwidth', -1)
df = pd.read_csv('jeopardy.csv')
print(df.head())

df = df.rename(columns={'Show Number' : 'show_num',' Air Date' : 'air_date', ' Round' : 'round',' Category' : 'category',' Value' : 'value', ' Question': 'question', ' Answer' : 'answer' })


# function that filters the dataset for questions that contains all of the words in a list
words = ['King', 'England']

def find_word (df, words):
    find = lambda x: all(word.lower() in x.lower() for word in words)
    return df[df['question'].apply(find)]

questions = find_word (df, words)
print(questions['question'].reset_index())

#function to convert the " Value" column to floats
convert = lambda x: float(x.removeprefix('$').replace(',', '') if x != 'None' else 0)
df['converted'] = df['value'].apply(convert)

print(df['converted'].mean())


#count of the unique answers to all of the questions in a dataset
num_unique_answers = df['answer'].nunique()
print(num_unique_answers)
#or
unique_answers = df['answer'].value_counts()
print(unique_answers)


#How many questions from the 90s use the word "Computer" compared to questions from the 2000s?
df['air_date'] = pd.to_datetime(df['air_date'])
print(df['air_date'])

nineties = df[((df.air_date >= '1990-01-01') & (df.air_date <= '1999-12-31')) & (df['question'].str.contains(pat = 'computer'))]
print("Number of questions with word \"computer\" in 1990-s : " + str(len(nineties)))
questions_2000 = df[((df.air_date >= '2000-01-01') & (df.air_date <= '2009-12-31')) & (df['question'].str.contains(pat = 'computer'))]
print("Number of questions with word \"computer\" in 2000-s : " + str(len(questions_2000)))




#Is there a connection between the round and the category?
df['category'] = df['category'].apply(lambda x: x.lower())

for_pivot = df.groupby(['round', 'category'])['question'].count().reset_index()
category_round_table = for_pivot.pivot(
    columns='round',
    index='category',
    values='question'
).reset_index()
print(category_round_table)

lit_category = category_round_table[(category_round_table.category.str.contains(pat = 'liter'))]
print(lit_category.reset_index())


