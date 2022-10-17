"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Word finder from words list"""

    def __init__(self, path):
        """
        Creates a new WordFinder instance
        Generates a list of words from the given filepath

        Attributes
        -----------
        path: file path to read words. Should contain one word per line

        word_list: list of word read from given file
        
        >>> wf = WordFinder('wf_test.txt')
        3 words read
        
        >>> wf.random() in ['dog', 'hedgehog', 'cat']
        True
        
        >>> wf.random() in ['dog', 'hedgehog', 'cat']
        True
        
        >>> wf.random() in ['dog', 'hedgehog', 'cat']
        True
        """
        file = open(path)
        self.word_list = self.make_list(file)
        print(f"{len(self.word_list)} words read")

    def make_list(self, file):
        """Parse words_file -> word_list"""
        return [word.strip() for word in file]

    def random(self):
        """Returns a random word from the word list"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """
    Sub-class of WordFinder that works with files containing blank lines and comments.
    
    >>> swf = SpecialWordFinder('swf_test.txt')
    3 words read
    
    >>> swf.random() in ['dog', 'hedgehog', 'cat']
    True
    
    >>> swf.random() in ['dog', 'hedgehog', 'cat']
    True
    
    >>> swf.random() in ['dog', 'hedgehog', 'cat']
    True
    """

    def make_list(self, file):
        """Parse words_file -> word_list"""
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]
