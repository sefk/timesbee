How many different Bee puzzles are there? Or more precisely, how many different
combinations of seven letters can be used to build bee puzzles?

This program found that there are 7231 different choices of seven letters. 
The majority (about 62%) have just one pangram in each puzzle, but it's not
uncommon to have two or three pangrams (about 25% of the time. The breakdown


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
one pangram, a word that uses all letters. It's possible for a puzzle to have
multiple pangrams.

For more information, see https://nytbee.com/. This site isn't affiliated with the
NY Times but is very cool and they don't seem to mind.

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

## Rough Breakdown

The [program output](timesbee.out) is written with one line for each set of
letters, with separators splitting the count of pangrams in sections. This makes
it easy to get an idea of the sizes each group by just searching for those 
separators with their position (line number) in the output. The ```grep -n```
does that nicely.

```
grep -n -- ---- timesbee.out
1:---- 1 pangram ----
4537:---- 2 pangrams ----
5844:---- 3 pangrams ----
6429:---- 4 pangrams ----
6722:---- 5 pangrams ----
6907:---- 6 pangrams ----
7005:---- 7 pangrams ----
7078:---- 8 pangrams ----
7121:---- 9 pangrams ----
7149:---- 10 pangrams ----
7168:---- 11 pangrams ----
7184:---- 12 pangrams ----
7197:---- 13 pangrams ----
7211:---- 14 pangrams ----
7223:---- 15 pangrams ----
7227:---- 16 pangrams ----
7233:---- 17 pangrams ----
7237:---- 18 pangrams ----
7239:---- 19 pangrams ----
7242:---- 20 pangrams ----
7246:---- 22 pangrams ----
7250:---- 23 pangrams ----
7252:---- 26 pangrams ----
7254:---- 27 pangrams ----
7256:---- found: 7231 puzzles, 13898 pangrams, of 235886 words considered
```

