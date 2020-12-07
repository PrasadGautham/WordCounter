import os
from WordCounter import WordCounter,FileWordExtractor

FILEPATH=os.path.join(os.path.dirname(__file__), 'input.txt')

try:
    if os.path.exists(FILEPATH):
        text_file=FileWordExtractor(FILEPATH)
        words=text_file.words
        word_counter=WordCounter(words=words) #init wordcounter class
        word_count_dict=word_counter.wordcount #get wordcount
        text_file.display_total_words()
        word_counter.display_word_counts()
    else:
        print('File not found')
except: 
    print('Application Error')

        