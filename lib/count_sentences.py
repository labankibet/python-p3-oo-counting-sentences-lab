#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
      if not isinstance(value, str):
        print("The value must be a string.")
        self._value = ""
      else:
        self._value = value

    #analysing sentences by checking punctuation  
    def is_sentence(self):
        return True if self._value.endswith(".") else False
    
    def is_question(self):
        return True if self._value.endswith("?") else False
    
    def is_exclamation(self):
        return True if self._value.endswith("!") else False
    
    def count_sentences(self):
        # splitting the input string using regular expressions
        sentences = re.split(r'[.!?]', self._value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

string = MyString()
string._value = "This is a string! It has three sentences. Right?"
print("Is it a sentence?", string.is_sentence())  # True
print("Is it a question?", string.is_question())  # False
print("Is it an exclamation?", string.is_exclamation())  # False
print("Number of sentences:", string.count_sentences())  # 3

