import words_in_proteome
from words_in_proteome import *
f = open("english_common_words.txt","r+")
f1 = open("human_proteome.fasta","r+")
liste1 = read_words(f)
dict = read_sequences(f1)
dict2 = search_words_in_proteome(liste1,dict)
find_most_frequent_word(dict2,dict)
graph(dict)
f1.close()
f.close()


