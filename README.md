# anti-magic-square-generator
Generator of one or multiple Magic or Anti-Magic Squares of a given size.

The idea behind it:
- The set of all possible number positions in a square, is equivalent to a
Symmetric Group (add link). The degree of that Group is equal to how many are
the numbers (give example for 3x3 square is a degree of 9)
- Construct with the degree given OR with the degree AND the two generators.
-- If the first, then check if possible to look for them
-- If the later, could the degree come out of the generators?
(Add link to Theorem about the 2 and 3 degree generators for every Symmetric Group)
- Construct methods using the listing algorithm to generate (6)
-- A random (Anti-)Magic Square (2)
-- A specific (Anti-)Magic Square with an ID (e.g. the number of (anti-)magic
squares to skip) (2)
-- All (Anti-)Magic Squares (2)
(Check if the listing algorithm could exist as a function)
