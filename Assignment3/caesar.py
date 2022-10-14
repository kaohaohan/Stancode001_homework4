"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    At first, user inputs the random number so the ALPHABET will shift spaces which based the number to the rights
    so the new string comes up,
    Second, if user conveys apple, then the input letters should be based on each letter in ALPHABET to corresponding
    in new string in order.

    """
    n = int(input('Secret number: '))
    ciphered_words = input("What's the ciphered string?")
    ans = decipher(n, ciphered_words)
    print('The deciphered string is:' + ans)




def decipher(n,ciphered_words):
    """
    First, the user inputs random number will came up new string which calls new_alphabet
    Then user inputs the ciphered string As a result, this function deciphers string to find real answer.
    """


    first_half = ALPHABET[ :26- n]
    second_half = ALPHABET[26-n: ]
    new_alphabet = second_half + first_half
    ans = ""
    for i in range(len(ciphered_words)):
        ch = ciphered_words[i]
        if ch == " ":
            ans += ' '
        else:
            if ch.islower():
                ch = ch.upper()
                index = new_alphabet.find(ch)
                decipher_cr= ALPHABET[index]
                ans += decipher_cr
    return ans







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

