How many different New York Times Spelling Bee puzzles are there? Or more
precisely, how many combinations of seven letters can be used to build bee
puzzles?

This program found that there are 7,742 different seven letters combinations
that could be used to generate unique Bee-style puzzles. There are more unique
puzzles themseves, because a different choice of middle letter would affect
the number of words that could be found with that required letter.

The majority of letter choices, about 62%, have just one pangram. That's lower
than I expected, actually. It's not that uncommon to have two or three pangrams,
which happens about about 25% of the time, and nearly 4 out of 10 puzzles will
have more than one pangram. 

And watch out for the combination ```einprst```. If this one ever comes up, good
luck finding all 27 pangrams.


## The Bee

The Bee is a puzzle consisting of seven letters, with one central "special" letter,
arranged like so:

```
     e   g
   n   P   r
     s   t
```

The center letter has to be used in all answers. Letters can be used any number
of times to make up words of four letters or more. Every puzzles has at least
one pangram, a word that uses all letters. A puzzle to have multiple pangrams.

For more information, see https://nytbee.com/. This site isn't affiliated with the
NY Times but is well done and the Times seems OK with it.


## This Program

Input: standard Unix dictionary file with one word per line.

Output: A list of all valid seven-letter possibilities for building Bee-style
puzzles. For each the list of pangrms matching those seven letters is listed
The overall list is grouped/sorted by the number of pangrams found.

Example output below:

```
---- 1 pangram ----
abcdefk ['feedback']
abcdefl ['defaceable']
abcdegh ['cabbagehead']

<...snip...>

---- 27 pangrams ----
einprst ['enspirit', 'enterprise', 'enterpriser', 'episternite', 'inspiriter',
'interpretress', 'intersperse', 'perienteritis', 'persistent', 'pertinentness',
'preinsert', 'preinterest', 'presentient', 'presentist', 'preteriteness', 'preteritness',
'prettiness', 'priesteen', 'pristine', 'reinspirit', 'ripienist', 'serpentine',
'spinneret', 'spinster', 'spinstress', 'sprinter', 'strepsitene']
```

The full output can be found in [```timesbee.out```](timesbee.out).


## Future Work

- What are the distributions of number of words?
- How does that change when arranged with a different center letter?
- Graph histograms of the different number of pangrams, number of answers.


## Counts of Pangrams

The [program output](timesbee.out) is written with one line for each set of
letters, with separators splitting the count of pangrams in sections. This makes
it easy to get an idea of the sizes each group by just searching for those 
separators with their position (line number) in the output. The ```grep -n```
does that nicely.

```
1:---- 1 pangram ----
4975:---- 2 pangrams ----
6342:---- 3 pangrams ----
6936:---- 4 pangrams ----
7230:---- 5 pangrams ----
7418:---- 6 pangrams ----
7516:---- 7 pangrams ----
7589:---- 8 pangrams ----
7632:---- 9 pangrams ----
7660:---- 10 pangrams ----
7679:---- 11 pangrams ----
7695:---- 12 pangrams ----
7708:---- 13 pangrams ----
7722:---- 14 pangrams ----
7734:---- 15 pangrams ----
7738:---- 16 pangrams ----
7744:---- 17 pangrams ----
7748:---- 18 pangrams ----
7750:---- 19 pangrams ----
7753:---- 20 pangrams ----
7757:---- 22 pangrams ----
7761:---- 23 pangrams ----
7763:---- 26 pangrams ----
7765:---- 27 pangrams ----
7767:---- found: 7742 puzzles, 14502 pangrams, of 235886 words considered
7768:---- words rejected because: {'proper noun': 25199, 'not seven letters': 190537, 'too many vowels': 157574}
```
