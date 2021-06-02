import random

print("Welcome to Hangman game!")
print("You have 10 tries to guess word")


fin = open('words.txt')
words = [line.strip().lower() for line in fin.readlines()]
figures = [
    """
    ---------
    |       |
    |       O
    |       
    |
    |
    |
    """
    ,
    """
    ---------
    |       |
    |       O
    |       |
    |
    |
    |
    """
    ,

    """
    ---------
    |       |
    |       O
    |      / \ 
    |       
    |
    |
    """
    ,

    """
    ---------
    |       |
    |       O
    |      / \ 
    |       |  
    |
    |
    """
    ,

    """
    ---------
    |       |
    |       O
    |      / \ 
    |       |
    |      / \ 
    |
    """
]

while True:
    word = random.choice(words)
    length = len(word)
    print(f"Guess the word with {length} letters!")



    word_list_easy = []
    word_list_medium = []
    word_list_hard = []
    word_list = []



    indx = 0
    for i in range(length):
        word_list.append('_')
    print(*word_list)

    score_all = 0
    score_one_game = 0

    count = 0
    fails = 0
    while True:
        count = count + 1

        letter = input("Guess a letter: ")
        for i in range(length):
            if letter == word[i]:
                word_list[i] = letter

        if letter in word_list:
            score_one_game += 5
            score_all += 5
            print('score :',score_one_game)

        if letter not in word_list:
            fails += 1
            score_one_game -= 5
            score_all -= 5
            print(figures[fails-1])
            print('score :', score_one_game)


        if fails >= len(figures):
            print("You Failed!")
            print("Your score: ", score_all)
            input("Press enter to play again!")


        if '_' not in word_list:
            print("You won!")
            print("Your score: ",score_all)

        print(*word_list)





















