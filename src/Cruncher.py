from Digest import Digest
import itertools
import hashlib
from alive_progress import alive_bar

class Cruncher:

    #Alphabets

    EN_FULL = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.'
    EN_LOW = 'abcdefghijklmnopqrstuvwxyz'
    EN_UP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    DIGIT = '0123456789'
    digest : Digest

    #Constructors

    def __init__(self):
    
        self.digest = Digest();

    #Utility methods

    def switchAlphabet(self, i : str):  #When an alphabet is giving as an argument it gets switched here and the string is returned to main as a giveable argument

        if(i == "EN_LOW"):

            return self.EN_LOW

        elif(i == "EN_UP"):

            return self.EN_UP

        elif(i == "EN_FULL"):

            return self.EN_FULL

        elif(i == "DIG"):

            return self.DIGIT

        else:

            raise Exception("[ERROR: Selected alphabet invalid]")    

    #Print methods

    def sha_noSaveDisplay(self, n : int, dict : str):

        possible_combinations = list(itertools.product(dict, repeat=n))  # Convert to a list
        tc = len(possible_combinations)  # Calculate the total number of combinations

        with alive_bar(tc, title="Progress") as bar:
            for combination in possible_combinations:
                word = ''.join(combination)
                sha_hash = self.digest.getSha256of(word)
                bar()
                print(f"{word} -> {sha_hash}", end="\r")


    def md5_noSaveDisplay(self, n : int, dict : str):

        possible_combinations = list(itertools.product(dict, repeat=n))  # Convert to a list
        tc = len(possible_combinations)  # Calculate the total number of combinations

        with alive_bar(tc, title="Progress") as bar:
            for combination in possible_combinations:
                word = ''.join(combination)
                md5_hash = self.digest.getMD5of(word)
                bar()
                print(f"{word} -> {md5_hash}", end="\r")


    #File methods (faster than print methods)

    def sha_SaveToFile(self, n: int, dict: str, output_file: str):
        possible_combinations = list(itertools.product(dict, repeat=n))
        tc = len(possible_combinations)

        with alive_bar(tc, title="Progress") as bar:
            with open(output_file, "w") as file:
                for combination in possible_combinations:
                    word = ''.join(combination)
                    sha_hash = self.digest.getSha256of(word)
                    bar()
                    result = f"{word} -> {sha_hash}\n"
                    file.write(result)

    def md5_SaveToFile(self, n: int, dict: str, output_file: str):

        possible_combinations = list(itertools.product(dict, repeat=n))
        tc = len(possible_combinations)

        with alive_bar(tc, title="Progress") as bar:
            with open(output_file, "w") as file:
                for combination in possible_combinations:
                    word = ''.join(combination)
                    sha_hash = self.digest.getMD5of(word)
                    bar()
                    result = f"{word} -> {sha_hash}\n"
                    file.write(result)


