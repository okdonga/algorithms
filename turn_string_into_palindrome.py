# Compute the minimum number of characters
# required to turn a string into a palindrome.
# You can only add characters to the end of the string.

# For example, if a string is "there", shortest way to
# turn "there" into a palindrome is by appending "ht"
# at the end of the string. So, the output will be
# 7 - the length of "thereth"


import sys

def minInsert(word):
    word_clean = result.rstrip()
    if len(word_clean)==1 or len(word_clean)==0:
        return 0
    else:
        if word_clean[0]==word_clean[len(word_clean)-1]: # word_clean[0]==word_clean[n-1]
            return minInsert(word_clean[1:len(word_clean)-1])
        else:
            return 1+min(minInsert(word_clean[1:]),minInsert(word_clean[:-1]))


rl = lambda: sys.stdin.readline()

container = []

n = int(rl())
for i in range(n):
    container.append(rl())

def show_result():
    for word in container:
        print minInsert(word) + len(word.rstrip())

show_result()

