# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        original_word_list = sorted([letter for letter in self.word])
        matching_word_list = []
        for element in list:
            if original_word_list == sorted([letter for letter in element]):
                matching_word_list.append(element)
        return matching_word_list
