How many different Bee puzzles are there? Or more precisely, how many different
combinations of seven letters can be used to build bee puzzles?

### The Bee

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

### This Program

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
einprst ['enspirit', 'enterprise', 'enterpriser', 'episternite', 'inspiriter', 'interpretress', 'intersperse', 'perienteritis', 'persistent', 'pertinentness', 'preinsert', 'preinterest', 'presentient', 'presentist', 'preteriteness', 'preteritness', 'prettiness', 'priesteen', 'pristine', 'reinspirit', 'ripienist', 'serpentine', 'spinneret', 'spinster', 'spinstress', 'sprinter', 'strepsitene']
```

The full output can be found in [```timesbee.out```](timesbee.out).

### Future Work

- What are the distributions of number of words?
- How does that change when arranged with a different center letter?
- Graph histograms of the different number of pangrams, number of answers.
