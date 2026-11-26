# Independent mathematical audit

## correctness

PASS

Normalize the four single-prime classes to coordinate zeros in the CRT product. In the surviving core, replacing an empty pair cylinder by a nonempty one cannot reduce the union. Let k be the number of active cylinders at a core point. Its contribution to B minus the union size is max(k-1,0). On the six cylinder indices draw a graph joining each pair of complementary edges of K4; this is a matching. If p=3, also join one pair of edges at vertex 0 whose assigned labels agree (such a pair exists because three edges share two available labels). The new edge joins distinct matching components, so the graph is still a forest. Its induced graph on the active cylinders has at most max(k-1,0) edges. Summing gives a deficit of at least 3 (one point for each complementary pair), or at least 3+m1 for p=3 (the forced pair intersection frees the remaining coordinate, of size at least m1). Distinct incidence labels throughout, or the lone repetition on pr and ps at p=3, respectively, realize these bounds: the only simultaneously active pairs are those counted, and they form no triangle, so no triple contributes. This gives 323 and 2519 for the displayed examples. Independently rechecked the finite symbolic certificate via direct core-point unions at a base point and unit shifts of the parameters: B-U is affine because any intersection of two distinct pair cylinders has at most one free coordinate. All coefficients are therefore recovered exactly by differences; all 625 and 500 signatures passed, with example union maxima 361 and 157 respectively. Replay: python3 /workspace/independent_replays.py 4.

## originality

PASS

The checked exact counterpart is the identical assigned record. The closest separate Resultary theorem is on all seven nontrivial divisors of three primes; it does not give the six-cylinder extremum of a four-coordinate core. Quantitative complete-covering restrictions in the inspected primary literature are not sharp partial-union optimizations. No dominating claim was identified in the compared evidence.

## value

PASS

The first two nontrivial divisor levels are a natural fixed family in the squarefree covering problem, and a sharp residual count gives information even when noncoverage is already known. The p=3 threshold detects a specific obstruction from the smaller coordinate alphabet, with an attainable loss increasing with q, rather than a table of isolated tuples. The pointwise collision argument also identifies what drives the optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
