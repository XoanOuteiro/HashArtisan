from Digest import Digest
import itertools
import hashlib
from alive_progress import alive_bar

class Translator:

    EN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.'
    DIGIT = '0123456789'
    digest : Digest

    def sha_noSaveDisplayOfLength(self, n : int, dict : str):

        possible_combinations = list(itertools.product(dict, repeat=n))  # Convert to a list
        tc = len(possible_combinations)  # Calculate the total number of combinations

        with alive_bar(tc, title="Progress") as bar:
            for combination in possible_combinations:
                word = ''.join(combination)
                sha_hash = self.digest.getSha256of(word)
                bar()
                print(f"{word} -> {sha_hash}", end="\r")


    def md5_noSaveDisplayOfLength(self, n : int, dict : str):

        possible_combinations = list(itertools.product(dict, repeat=n))  # Convert to a list
        tc = len(possible_combinations)  # Calculate the total number of combinations

        with alive_bar(tc, title="Progress") as bar:
            for combination in possible_combinations:
                word = ''.join(combination)
                md5_hash = self.digest.getMD5of(word)
                bar()
                print(f"{word} -> {md5_hash}", end="\r")


    def __init__(self):

        self.dig = Digest();