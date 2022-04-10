import nltk
from nltk import word_tokenize
text = word_tokenize("Did you ever dance with the devil in the pale moon light")
output = nltk.pos_tag(text)
print(output)