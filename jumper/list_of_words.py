from pickle import TRUE
import random

class puzzle:
    def __init__(self):
        self._list_of_words= ["love", "banana","world","portugal","brazil", "friends"]
        self._word =""
        self._puzzle =[]

    def choose_word(self):
        self._word=random.choice(self._list_of_words)
        for i in range(len(self._word)):
            self._puzzle.append("_")

    def verify(self, letter):
        if letter in self._puzzle:
            return True
        elif letter in self._word:
            for i in range(len(self._word)):
                if self._word[i] == letter:
                    self._puzzle[i] = f"{letter}"
            return True
        else:
            return False


    def get_puzzle(self):
        return self._puzzle

    def get_word(self):
        return self._word
        


class terminal_services:

    def read_letter(self):
        pass