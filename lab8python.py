from abc import ABC, abstractmethod


class LetterFrequency(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(LetterFrequency):
    def calculateFreqs(self):
        letter_counts = {}
        with open(self.address, 'r') as file:
            text = file.read().lower()
            for letter in text:
                if letter.isalpha():
                    if letter in letter_counts:
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1
        for letter, count in letter_counts.items():
            print(f"List -> {letter} Resulting List -> {letter} = {count}")


class DictCount(LetterFrequency):
    def calculateFreqs(self):
        letter_counts = {}
        with open(self.address, 'r') as file:
            text = file.read().lower()
            for letter in text:
                if letter.isalpha():
                    if letter in letter_counts:
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1
        for letter, count in letter_counts.items():
            print(f"Dict -> \"{letter}\" 0 Updated Dict -> \"{letter}\" {count}")


list_counter = ListCount("weirdWords.txt")
list_counter.calculateFreqs()

dict_counter = DictCount("weirdWords.txt")
dict_counter.calculateFreqs()