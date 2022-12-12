import nltk
import numpy
import pandas
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pprint

file = open("data.txt", "r")
text = file.read()
final_text = ""
my_lines = text.split('.')
for char in text:
    if char.isalnum() or char == '.' or char == ' ':
        final_text += char
    else:
        continue
#print(final_text)
lines = final_text.split('.')
for line in lines:
    if line == ' ' or line == '':
        lines.remove(line)
i = 0
lines_words = list()
for line in lines:
    temp = line.split(' ')
    temp.insert(0, i)
    lines_words.append(temp)
    i += 1
stemmer = PorterStemmer()
stop_words = nltk.corpus.stopwords.words("english")

final_list = list()
for line in lines_words:
    temp_list = list()
    for word in line:
        word = str(word)
        if word.isnumeric():
            temp_list.append(word)
            continue
        if word.isalpha():
            if word in stop_words:
                continue
            else:
                word = word.lower()
                word = stemmer.stem(word)
                temp_list.append(word)
    final_list.append(temp_list)
#print(final_list)

hash_map = dict()
for line in final_list:
    for word in line:
        if word.isalpha():
            if word in hash_map.keys():
                hash_map[word]+=1
            if word not in hash_map.keys():
                hash_map[word]=1
max_freq = max(hash_map.values())
list_weights = list()
for line in final_list:
    total = 0
    for word in line:
        if word.isalpha():
            total += (hash_map[word])/max_freq
    list_weights.append(total)
avg = 0
for i in list_weights:
    avg+=i
avg = avg/len(list_weights)
f = open("out.txt","w")
for i in range(0,len(list_weights)):
    if list_weights[i] >=(avg*4/5):
        print(my_lines[i],".", file =f)