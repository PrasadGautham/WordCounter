import os


class WordCounter:
    words: list=[]
    wordcount:dict = {}
    def __init__(self,words=[]):
        self.words=words
        self.wordcount=self.get_word_counts()
        
    def get_word_counts(self):
        for word in self.words:
            if word not in self.wordcount:
                self.wordcount[word] = 1
            else:
                self.wordcount[word] += 1
        return sorted(self.wordcount.items(), key=lambda x: x[1], reverse=True)

    def display_word_counts(self):
        print('\nThe top 10 most common words are:\n')
        for word, count in self.wordcount[:10]:
            print(word, count)
    


class FileWordExtractor:
    file_path: str='input.txt'
    words:list = []

    def __init__(self,file_path=file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path,'r') as file:  # close scope of file after with
                    data=file.read().split()
                    words = [character for character in data if character.isalpha()] 
                    self.words=words
            except:
                print('File Type not supported')
                
        else:
            print('File not found')

    def total_words(self):
        return len(self.words)
    
    def display_total_words(self):
        print(f'\nTotal number of words in text file are {len(self.words)}')
