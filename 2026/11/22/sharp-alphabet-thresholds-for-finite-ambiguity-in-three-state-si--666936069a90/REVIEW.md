# Independent mathematical audit

## correctness

PASS

For the stated trim adjacent-only chain, a letter with loops at both ends of an adjacent bridge and the bridge itself gives arbitrarily many crossing times; trim provides the required prefix or suffix. A letter in X followed by one in Y gives an endpoint-loop block with a complete crossing, so repetitions again give unbounded ambiguity. Avoiding these obstructions is exactly containment in T_X or T_Y. A fresh replay with ordinary full integer matrices computed the two 48-element closures from their 23 generators, matched both CSVs, and found maximum entry (1,3) = 4 in each. Reaching a fixed point under every right multiplication certifies arbitrary word lengths. The replay checked 1,024 ordered binary pairs, with exactly 216/28/2 trim finite pairs of degrees 1/2/3 (246 total), and found the four finite trim unary types 10,11,14,26, each of degree 1. It recovered the witnesses aa, aabb and abbc with counts 1,3,4; duplicate letter types extend the last witness without adding products. These conclusions exclude skip edges, other initial/final states and weighted parallel edges.

## originality

PASS

The lower bound of four at three states and the obstruction approach have prior coverage. The matching adjacent-only upper bound, alphabet thresholds, exact binary census and explicit two-family closure classification remain distinct on the inspected evidence.

## value

PASS

This is the first chain size with two compulsory crossings, where the small-alphabet restriction affects maximal ambiguity. The exact 1/3/4 gap and the two finite product families provide a sharp test case for general ambiguity estimates and a reusable way to certify upper bounds over all word lengths; the ordered census gives more than specimens achieving the maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
