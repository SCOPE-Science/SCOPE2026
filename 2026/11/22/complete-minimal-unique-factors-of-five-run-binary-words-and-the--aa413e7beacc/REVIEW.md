# Independent mathematical audit

## correctness

PASS

For positive a,b,c,d,e and overlapping occurrences, a unique factor of length at least two is minimal iff both one-letter deletions repeat. A pure power can be unique only at a unique longest run of that symbol, and then it is minimal. A one-transition factor is counted by two boundary rectangles of run lengths: a factor with both exponents at least two and both deletions repeated lies in their intersection, so cannot itself be unique. With one exponent one the other must be one above the corresponding minimum; the other deletion is pure and rules out exactly the unique-maximum-zero collision or the unit gap between one-run lengths. A zero–one–zero factor fixes a full one-run length; if the lengths differ, only unit zero flanks around the shorter run can be minimal, and if equal, repeated end deletions force both flanks to fit at both runs even when one deletion removes a flank. A one–zero–one factor fixes the sole internal zero run, so only 10^c1 can be minimal; both deleted factors repeat iff a and e are at least c. Every factor spanning four or five runs properly contains the unique 10^c1. The eight templates give distinct words (where symbol patterns coincide, the longer exponent lies on opposite sides), so realizing all eight forces b+d≥4, a,e≥c+1 and, by the unique maximum without bridge suppression, max(a,e)≥c+2. Hence n≥10. The tuple (2,1,1,3,n−7) satisfies every condition for n≥10; at 10 its eight windows of length three are the eight binary triples. Independent replay: python3 /workspace/reviews/check_mathematics.py 5 compares complete MUS sets computed by pairwise suffix common-prefix tests for every positive composition of 5≤n≤21 into five parts. It found four attaining tuples at n=10 and none earlier. This finite check is supplementary, not the universal proof.

## originality

PASS

The strongest overlapping exact result is the separated five-run table. The contribution supported here is the unrestricted table, especially the equality and unit-gap cases and the sharp unrestricted length threshold; the separated list and the exactly-two-ones subcase are not new.

## value

PASS

Five alternating runs introduce three competing zero runs without losing the two competing one-runs and boundary pairs. The complete symbolic classification resolves the resulting collisions, sharpens a general bound of nine to eight, and lowers the first feasible length for eight from thirteen in the separated regime to ten. An exact factor list, not just a count or an algorithm on a fixed input, supplies a useful small-run benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
