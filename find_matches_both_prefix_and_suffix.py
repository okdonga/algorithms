################
# Given a string of characters, find a series of letters starting from the left of the string that is repeated at the end of the string.

# For example, given a string 'jablebjab', 'jab' is found at the start of the string, and the same set of characters is also found at the end of the string.
# This is one match. Here, we call the first job - prefix, and the latter jab - suffix. Find all cases where a set of characters starting from the left of the string is also found at end of the string. The output should be the length of a series of letters that match this pattern. So, with 'jablebjab', a seris of letters that our pattern are 1, 'jab' 2, 'jablebjab'. So, the output is [3, 9]

# More examples as follows:
# eg1.
# input: alaghggiualagihjkbcala
# matches: 1. a 2. ala 3. alala
# output: [1, 3, 5]

# eg2.
# input: ababcababababcabab
# matches: 1. a 2. abab 3. ababcabab 4. ababcababababcabab
# output: [2, 4, 9, 18]


# PSEUDOCODE
# input : dad's nume + mum's name
# output : length of each combination of letters that can be both prefix and suffix

# find all possible cases of repeated letters that starts with a(original[0]) and ends with last word in the combined string (b)
# eg. ab, abab, ababcab, ababcabab, ababcababab, ... entire string
# compare if the prefix also match the last x digits of the string
# if it is, count the num and push it to to the results array

# CORNER CASE:
# 1. when there is no repeation in the string


def find_words_that_can_be_both_prefix_and_suffix(str):

    total_length = len(str)

    # If there is no repetition in the string, no need to proceed further
    uniq_str = set(str)
    if len(uniq_str) == total_length:
        return [total_length]

    start = str[0]
    end = str[total_length-1]

    # Find all cases of prefix that start with the first letter of string and end with the last letter of string
    prefixes = []

    for idx, letter in enumerate(str):
        if letter == end:
            prefixes.append(str[:idx+1])

    # Out of all prefixes, find ones that also count as suffixes
    prefixes_and_suffixes = []
    for prefix in prefixes:
        len_of_prefix = len(prefix)
        suffix_start_idx = total_length - len_of_prefix
        if str[suffix_start_idx:] == prefix:
            prefixes_and_suffixes.append(len_of_prefix)
            # prefixes_and_suffixes.append(prefix)

    return prefixes_and_suffixes

print find_words_that_can_be_both_prefix_and_suffix('aaaaaa')
# print find_words_that_can_be_both_prefix_and_suffix('jab56jab')
# print find_words_that_can_be_both_prefix_and_suffix('a')
# print find_words_that_can_be_both_prefix_and_suffix('ab')
# print find_words_that_can_be_both_prefix_and_suffix('alala')
# print find_words_that_can_be_both_prefix_and_suffix('abcde')
# print find_words_that_can_be_both_prefix_and_suffix('ababcababababcabab')











