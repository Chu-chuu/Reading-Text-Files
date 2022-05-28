# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here 
        with open("story.txt", "r") as f:
            text = f.read()
            
        return text
content = (read_file_content("filename"))  

import string
count_words = {}
dict = {}

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split
    return{word: text.count(word) for word in text.split()}

def strip_punctuations(lin):
    for lin in text:
        lin = text.strip()
        lin = text.lower()
        lin = text.translate(str.maketrans('','', string.punctuation))
        lin = lin.replace('\n','')
        words = lin.rstrip('\n').split('')
        return words

    for word in dict:
        word = word.lower()
        if word not in dict:
            count_words[word] = 0
        else:
            count_words[word] += 1

print (count_words())

 
  


   
    



    