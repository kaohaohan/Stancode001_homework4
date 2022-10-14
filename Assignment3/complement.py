"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    When the column prints the following texts,
    it will present the complementary characters of letters
    """

    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))




def build_complement(dna):
    """
    A and T are complementary
    C and G are complementary
    so if A shows up, then A will turn T
    if G shows up, then G will turn C
    """
    ans = ""
    for i in range (len(dna)):
        ch = dna[i]
        if ch == 'A':
            ans +='T'
        elif ch =='C':
            ans +="G"
        elif ch =="T":
            ans +="A"
        # elif ch =='':
        #     ans +='DNA strand is missing'
        elif ch =="G":
            ans +="C"
    if ans == "":
        ans = 'DNA strand is missing'
    return ans





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
