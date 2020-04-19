#!/usr/bin/python3
#
# Count the number of possible New York Times Bee puzzles candidates.
# Sef Kloninger, 19-April-2020
#
# Takes a list of words on stdin. On MacOS, you can run like this:
#   pv /usr/share/dict/words | ./timesbee.py > timesbee.out

import sys

puzzlemap = {}
rejected = {}
considered = 0
pangrams = 0
vowel_set = set(['a', 'e', 'i', 'o', 'u', 'y'])

def RejectBecause(reason):
    if reason not in rejected.keys():
        rejected[reason] = 0
    rejected[reason] = rejected[reason] + 1

def ValidWord(word, letter_set):
    valid = True
    if word[0] >= 'A' and word[0] <= 'Z':
        RejectBecause('proper noun')
        valid = False
    if len(letter_set) != 7:
        RejectBecause('not seven letters')
        valid = False
    if len(letter_set.intersection(vowel_set)) != 2:
        RejectBecause('not two vowels')
        valid = False
    return valid

# Build a map of all puzzles
# key = seven letters for the puzzle
# value = list of all pangrams given those letters to work with.
for word in sys.stdin:
    word = word.strip()
    considered = considered + 1
    letter_set = set()
    for char in list(word):
        letter_set.add(char.lower())
    if not ValidWord(word, letter_set):
        continue
    pangrams = pangrams + 1
    letters = ''.join(sorted(list(letter_set)))
    if letters not in puzzlemap.keys():
        puzzlemap[letters] = []
    puzzlemap[letters].append(word)

# Pivot by pangram count
# key = number of pangrams found
# value = list of tuples, each tuple is (letters, pangram list) from puzzlemap
pangram_counts = {}
for (letters, wordlist) in puzzlemap.items():
    count = len(wordlist)
    if count not in pangram_counts.keys():
        pangram_counts[count] = []
    found_tuple = (letters, wordlist)
    pangram_counts[count].append(found_tuple)

# Print out all letters andp
for (count, pangrams_list) in sorted(pangram_counts.items()):
    noun = "pangram" if count == 1 else "pangrams"
    print( "---- %d %s ----" % (count,noun))
    for pangram_tuple in sorted(pangrams_list):
        print(pangram_tuple[0], sorted(pangram_tuple[1]))

print("---- found: %d puzzles, %d pangrams, of %d words considered" 
        % (len(puzzlemap), pangrams, considered))
print("---- words rejected because:", rejected)
