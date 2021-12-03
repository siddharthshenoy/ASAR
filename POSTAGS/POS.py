import nltk
from nltk import word_tokenize

example = "the dog is bleeding can't get up, please need help at madiwalla"
word_tokens = word_tokenize(example)
pos = nltk.pos_tag(word_tokens)
selective_pos = ['NN','NNP','NNPS','NNS','VB','VBD','VBG','VBN','VBP']
selective_pos_words = []
for word,tag in pos:
     if tag in selective_pos:
         selective_pos_words.append(word)
print(selective_pos_words)