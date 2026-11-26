# Independent mathematical audit

## correctness

PASS

The literal cyclic strings with 0, 1, 2, and 3 ones are disjoint. The first two groups give c and b+1. With two ones, each distinct internal gap g contributes one plus the smaller remaining gap (repeated choices of g give the same padding range), and the circumference never binds. With three ones the two internal gaps must agree and the outside gap bounds twice the padding. Summation gives the formula in every case, including zero gaps. For distinct gaps the count is 2n-2-c; distinctness bounds n-3<=3c-3 and the listed triples attain the smallest c. At fixed smallest c the deficits (c-a,c-b) are strictly decreasing positive integers summing to 3c-n+3, giving exactly the displayed one or two triples. In n=6t+d, 0<=d<6, the distinct-gap maximum minus the repeat-gap count is t-2 for d=1 and t-1 otherwise. This gives strict superiority for n>=14 and the small cases follow by direct comparison, including the tie at n=13. Rotation and reflection realize all permutations of three gaps. An independent bounded replay fixed one 1 at index 0, enumerated the two other positions, expanded odd and even cyclic centers to length n and deduplicated literal strings: 8,436 anchored words at lengths 3–38 passed the counts, maxima and (from 14) optimizer checks. The packaged verify_pal3.py takes the alternate factor-start/length route through 36; its 7,140 count is recorded in VERIFICATION.md, not a fresh execution. Only the argument covers arbitrary n.

## originality

FAIL

An earlier dated, distinct Resultary record gives the same count for every three-marker circle, with the same conventions, as its equation (1). The frozen extremal conclusion is a direct integer optimization of that exact prior formula and does not leave a materially distinct contribution. This is established coverage, not a negative search or an assertion about Simpson's historical priority.

## value

FAIL

The fixed-content family and its extremizers are worthwhile objects. But the frozen per-gap invariant is already known, and the rest is the direct largest-gap minimization and residue arithmetic of that identical formula; no independently useful unknown exact fact survives in this record. No repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
