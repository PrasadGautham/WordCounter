from unittest import TestCase,TestSuite,TestLoader,TextTestRunner
import os
from WordCounter import WordCounter,FileWordExtractor

class FileWordExtractorTestCase(TestCase):
    def setUp(self):
        pass
    def test_letters_only_text_file(self):
        file_path=os.path.join(os.path.dirname(__file__), 'samples/test1.txt')
        file_word_extractor=FileWordExtractor(file_path)
        self.assertEqual(file_word_extractor.total_words(),20)
    def test_digits_only_text_file(self):
        file_path=os.path.join(os.path.dirname(__file__), 'samples/test2.txt')
        file_word_extractor=FileWordExtractor(file_path)
        self.assertEqual(file_word_extractor.total_words(),0)
    def test_special_symbols_only_text_file(self):
        file_path=os.path.join(os.path.dirname(__file__), 'samples/test3.txt')
        file_word_extractor=FileWordExtractor(file_path)
        self.assertEqual(file_word_extractor.total_words(),0)
    def test_combined_characters_text_file(self):
        file_path=os.path.join(os.path.dirname(__file__), 'samples/test4.txt')
        file_word_extractor=FileWordExtractor(file_path)
        self.assertEqual(file_word_extractor.total_words(),15)
    def test_blank_text_file(self):
        file_path=os.path.join(os.path.dirname(__file__), 'samples/test5.txt')
        file_word_extractor=FileWordExtractor(file_path)
        self.assertEqual(file_word_extractor.total_words(),0)
    
class WordCounterTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_word_count(self):
        word_list=['test','this','this','that','is','test','is','test','is','of','yes']
        word_counter=WordCounter(words=word_list) 
        self.assertEqual(word_counter.wordcount,[('test', 3), ('is', 3), ('this', 2), ('that', 1), ('of', 1), ('yes', 1)])


if __name__ == "__main__":

    suite = TestSuite()
    tests = TestLoader()
    suite.addTests(tests.loadTestsFromTestCase(FileWordExtractorTestCase))
    suite.addTests(tests.loadTestsFromTestCase(WordCounterTestCase))
    runner = TextTestRunner()
    runner.run(suite)