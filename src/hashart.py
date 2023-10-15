import argparse
from Cruncher import Cruncher

def main():
    crunch = Cruncher()

    # Declaration of Parser
    parser = argparse.ArgumentParser(description="HashArt")

    #Declaration of arguments
    parser.add_argument("-v", "--version", action="version", version="HashArt 0.2.4")
    
    parser.add_argument("-w", "--write", action="store_true", help="Indicates that the output will be written to the file.")
    parser.add_argument("-d", "--display", action="store_true", help="Indicates that the output will be displayed on the console.")

    parser.add_argument("-a", "--alphabet", choices=["EN_LOW", "EN_UP", "EN_FULL", "DIG"],help="Choose from predefined alphabets")
    parser.add_argument("-c", "--complexity", type=int,help="Specify the size (integer) of the hashable words. Above 5 may take a long time with big alphabets")

    parser.add_argument("-sha", "--sha", action="store_true", help="Flag for SHA hashing")
    parser.add_argument("-md5", "--md5", action="store_true", help="Flag for MD5 hashing")

    parser.add_argument("-f", "--file", help="Specify the output file for writing (used with -w)")

    args = parser.parse_args()

    #write switch-case
    if args.write and args.complexity and args.alphabet and args.file:

        comp = args.complexity
        alph = crunch.switchAlphabet(args.alphabet)
        output_file = args.file

        if args.sha:
            crunch.sha_SaveToFile(comp, alph, output_file)
        elif args.md5:
            crunch.md5_SaveToFile(comp, alph, output_file)

    #display switch-case
    elif args.display and args.complexity and args.alphabet:

        comp = args.complexity
        alph = crunch.switchAlphabet(args.alphabet)

        if args.sha:
            crunch.sha_noSaveDisplay(comp, alph)
        elif args.md5:
            crunch.md5_noSaveDisplay(comp, alph)

    else:
        print("Usage incorrect: please use python hashart.py -h/--help for usage instructions")

if __name__ == "__main__":
    main()