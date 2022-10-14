"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    User has 7 chances to find the answers. If users can't find the answer within 7 times, console will print users
    will be hung.
    """

    play_game()


def play_game():
    """
 This function operates how this game works
    """
    word = random_word()     #為了不要讓random word 隨機換字 先把第一次呼叫的單字存下來，後面就不會一直變了 別人建議
    answer = len(word) * "-"
    failure_left = 7

    while failure_left > 0:
        if answer == word:
            print("You win!!")
            print("The word was:"+ answer)
            return
        print("THe word looks like " +answer)
        print("You have " + str(failure_left) + " wrong guesses left")
        guess = input("Your guess: ")
        guess = guess.upper() #改大寫
        index = find_char(word, guess)
        if index != '':
            answer = replace_word(answer, index, guess)
            print("You are correct!")
        else:
            failure_left -= 1  # 扣一分
            print("There is no " + guess + "'s in the word.")

    print("You are completely hung :( ")
    print("The word was: " + word)




def find_char(string, word):
    """
    The function can replace the word, if user guess right one.
    """
    ans = ''
    for i in range(len(string)):
        ch = string[i]
        if ch == word:
            i_to_string = str(i)
            ans += i_to_string
    return ans

def replace_word(string, position, word):
    """
    The function can replace the word, if user guesses right one.
    Moreover, if the user guesses the word, there are more than two answers. This function can solve it.
    """
    ans = ''
    for i in range(len(string)):
        ch = string[i] #字母
        i_to_string = str(i)
        if position.find(i_to_string) != -1:
            ans += word
        else:
            ans += ch
    return ans




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"



# def replace_first(str,replace_word):    #換字功能
#     """
#     The function can replace the word, if user guess right one.
#     """
#     ans=''
#     for i in range(len(str)):
#         ch = str[i]
#         if i == 0:
#             ans+=replace_word
#         else:
#             ans+=ch
#     return ans

# if index != -1:   #如果單字裡的數字不等於-1就把單字拆成前半部跟後半部
#     first_half = answer[:index]
#     second_half = answer[index:]
#     second_half = replace_first( second_half, guess)    # 把user猜的字帶進 換字function裡
#     answer = first_half+ second_half #串起來再return給answer

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
