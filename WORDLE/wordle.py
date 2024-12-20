import random, os
from time import sleep


alpha = 'abcdefghijklmnopqrstuvwxyz '
answer = ""
stats = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    'Fail':0,
}


#create list of usable words
word_file = open("words.txt", "r")
words = word_file.readlines()
word_list = []
for line in words:
    new_line = str(line)[:5]
    word_list.append(new_line)
word_file.close()


#define a function to clear console
def clear():
    os.system('cls')

#creates a dictionary with letter counts from word
def dictify(word):
    dic = {}
    for letter in alpha:
        dic[letter] = 0
    for letter in word:
        dic[letter] += 1
    return dic

#create check string
def create_check_string(word):
    check_string_1 = ""
    string_dict = dictify(word)
    answer_dict = dictify(answer)
    # print(f'string dict: {string_dict}')
    # print(f'answer dict: {answer_dict}')
    for i in range(5):
        if word[i] == answer[i]:
            check_string_1 += '🟩'
            answer_dict[word[i]] -= 1
        elif word[i] in list(answer) and answer_dict[word[i]] > 0:
            check_string_1 += '🟨'
        else:
            check_string_1 += '🟥'
    
#run the same thing but backwards
    check_string_2 = ""
    string_dict = dictify(word)
    answer_dict = dictify(answer)
    for i in range(4, -1, -1):
        if word[i] == answer[i]:
            check_string_2 += '🟩'
            answer_dict[word[i]] -= 1
        elif word[i] in list(answer) and answer_dict[word[i]] > 0:
            check_string_2 += '🟨'
        else:
            check_string_2 += '🟥'

        
#return whichever string contains more red

    count1 = check_string_1.count('🟥')
    count2 = check_string_2.count('🟥')

    if count1 > count2:
        return check_string_1
    else:
        return check_string_2[::-1]
        

                        
#space out word to print
def pretty_space(word):
    string = " "
    for letter in word:
        string += letter
        string += " "
    return string

#print board
def print_board(guesses_list):
    current_guess = guesses_list[-1]
    for word in guesses_list:
        print(pretty_space(word.upper()))
        check_string = create_check_string(word)
        print(check_string)
        print("\n")

        global win_check
        if check_string == "🟩🟩🟩🟩🟩":
            win_check = True
        else:
            win_check = False


#check string validity
def check_valid_guess(guess):
    if len(guess) != 5:
        return False
    for letter in guess:
        if letter not in alpha or letter == " ":
            return False
    if guess.lower() not in word_list:
        return False
    return True


def play_game():
    #define current guess, guesses list, sets win to false, defines alphabet
    global win_check
    win_check = False
    global answer
    answer = word_list[random.randrange(len(word_list))]
    guesses_list = []
    guesses_remaining = 6
    clear()
    print("Welcome to Wordle!")
    sleep(2)
    clear()

    while True:
        while True:
            guess = input("What is your guess? ")
            if check_valid_guess(guess) == True:
                clear()
                break
            print("Invalid guess.")
            sleep(1.5)

        guesses_list.append(guess)

        print_board(guesses_list)
        guesses_remaining -= 1
        print(f"You have {guesses_remaining} guesses left.")

        global stats
        if win_check == True:
            print(f"Congratulations! You solved the Wordle in {6-guesses_remaining} guesses!")
            stats[6-guesses_remaining] += 1
            break
        if guesses_remaining == 0:
            print(f"You ran out of guesses. The answer was {answer.upper()}")
            stats['Fail'] += 1
            break
        sleep(1.5)


def show_stats():
    clear()
    print('STATISTICS\n')

    print('   1 | ', end = "")
    for i in range(stats[1]):
        print('X ', end="")
    print("\n")
    print('   2 | ', end = "")
    for i in range(stats[2]):
        print('X ', end="")
    print("\n")
    print('   3 | ', end = "")
    for i in range(stats[3]):
        print('X ', end="")
    print("\n")
    print('   4 | ', end = "")
    for i in range(stats[4]):
        print('X ', end="")
    print("\n")
    print('   5 | ', end = "")
    for i in range(stats[5]):
        print('X ', end="")
    print("\n")
    print('   6 | ', end = "")
    for i in range(stats[6]):
        print('X ', end="")
    print("\n")
    print('Fail | ', end = "")
    for i in range(stats['Fail']):
        print('X ', end="")
    print("\n")



#game start sequence

clear()
print('WORDLE')
sleep(1)
print('by ', end = "")
sleep(0.5)
print("Ezra ", end = "")
sleep(0.5)
print("Passalacqua")
sleep(2.5)

# gameplay

while True:
    clear()
    again = ''
    while True:
        question = input(f"Hit enter to play{again}, or type 'stats' to see your statistics!  ")
        if question == "":
            play_game()
            continue
        elif question == 'stats':
            clear()
            show_stats()
        else:
            clear()
            continue
    again = ' again'
    sleep(2)
    
