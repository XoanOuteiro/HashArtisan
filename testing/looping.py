import itertools
import hashlib
from alive_progress import alive_bar, config_handler

EN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.'
DIG = '0123456789'



def getMD5of(s : str):

    md5_hash = hashlib.md5(s.encode()).hexdigest()
    return md5_hash

def wordSpawn(length : int, dict : str):

    possible_combinations = list(itertools.product(dict, repeat=length))  # Convert to a list
    tc = len(possible_combinations)  # Calculate the total number of combinations

    print("Generating words and calculating MD5 hashes:")
    with alive_bar(tc, title="Progress") as bar:
        for combination in possible_combinations:
            word = ''.join(combination)
            md5_hash = getMD5of(word)
            bar()
            print(f"{word} -> {md5_hash}", end="\r")



length = int(input("Len? "))
wordSpawn(length, DIG)