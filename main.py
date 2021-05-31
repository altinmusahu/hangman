import random

print("Welcome to Hangman game!")
fin = open('words.txt')
words = [line.strip().lower() for line in fin.readlines()]

while True:
    word = random.choice(words)
    length = len(word)
    print(f"Guess the word with {length} letters!")
    word_list = []
    indx = 0
    for i in range(length):
        word_list.append('_')
    print(*word_list)

    while True:
        letter = input("Guess a letter: ")
        for i in range(length):
            if letter == word[i]:
                word_list[i] = letter

        if '_' not in word_list:
            print("You won!")

        if letter not in word_list:
            print("---------")
            print("|       |")
            print("|       O")
            print("|")
            print("|")
            print("|")
            print("|")
        print(*word_list)

        while True:
            letter = input("Guess a letter: ")
            for i in range(length):
                if letter == word[i]:
                    word_list[i] = letter

                if '_' not in word_list:
                    print("You won!")

                if letter not in word_list:
                    print("---------")
                    print("|       |")
                    print("|       O")
                    print("|       |")
                    print("|")
                    print("|")
                    print("|")
                print(*word_list)

                while True:
                    letter = input("Guess a letter: ")
                    for i in range(length):
                        if letter == word[i]:
                            word_list[i] = letter

                        if '_' not in word_list:
                            print("You won!")

                        if letter not in word_list:
                            print("---------")
                            print("|       |")
                            print("|       O")
                            print("|      / \ ")
                            print("|")
                            print("|")
                            print("|")
                        print(*word_list)

                        while True:
                            letter = input("Guess a letter: ")
                            for i in range(length):
                                if letter == word[i]:
                                    word_list[i] = letter

                            if '_' not in word_list:
                                print("You won!")

                            if letter not in word_list:
                                print("---------")
                                print("|       |")
                                print("|       O")
                                print("|      / \ ")
                                print("|       |")
                                print("|")
                                print("|")
                            print(*word_list)

                            while True:
                                letter = input("Guess a letter: ")
                                for i in range(length):
                                    if letter == word[i]:
                                        word_list[i] = letter

                                    if '_' not in word_list:
                                        print("You won!")

                                    if letter not in word_list:
                                        print("---------")
                                        print("|       |")
                                        print("|       O")
                                        print("|      / \ ")
                                        print("|       |")
                                        print("|      / \ ")
                                        print("|")

                                        print("You Failed")
                                        play_again = input("Press enter to play again")
                                    print(*word_list)
                                    break

























