# In this project we will be creating NATO phonetic alphabet for a given input by user
# We have a csv file with standard words for each letter

import pandas as pd

# first we will use .csv file to create a dictionary of nato phonetic alphabet

df = pd.read_csv("nato_phonetic_alphabet.csv")

# using dictionary comprehension to convert given dataframe to dictionary
df_dict = {row.letter:row.code for index,row in df.iterrows()}
# print(df_dict)

# taking input from user and print its nato_phonetic_code in the form of list
user_input = input("Enter the word: ")
result = [df_dict[letter.upper()] for letter in user_input if letter.upper() in df_dict]

print(result)
