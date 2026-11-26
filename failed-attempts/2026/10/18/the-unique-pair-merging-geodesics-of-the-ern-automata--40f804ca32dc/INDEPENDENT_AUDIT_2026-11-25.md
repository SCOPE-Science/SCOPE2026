# Independent mathematical audit

## correctness

PASS

Translation of {0,d} has orbit size n except at even antipodal d=n/2, when it has size n/2; the gap classes exhaust distinct pairs. With R=n(d−1)+j+1, rotation reduces R by one for j>0 and increases it at wraparound. A b-move fixing the pair leaves R unchanged; b at {0,d} merges for d=1 and otherwise goes to {1,d} on the previous gap layer at index n−1, reducing R by one. The remaining zero-containing pair {n−d,0}, present only for 2d<n, moves to a larger gap layer, except at the top odd gap where its index instead increases to n−1. Thus exactly one letter drops R by one and no letter drops more; iterating the descending moves gives exactly the displayed word, and every geodesic must make those moves. The ranks fill contiguous disjoint layers, hence the spectrum, maximum, mean and composition follow. An independent reverse BFS enumerating inverse-letter images directly (including the single edge into the merged sink) checked ranks, unique optimal successors, and the resulting word for all 85,319 pairs with 3≤n≤80.

## originality

FAIL

Two distinct indexed records cover the frozen result under the state shift x↦x−1 mod n: one treats all positive letter costs, including unit costs; the other gives the same distances and unique geodesics as suffixes of its master word. This is demonstrable statement-level coverage, not a claim of priority between records.

## value

FAIL

Pointwise geometry of the natural extremal automaton would be useful beyond a bound, but the exact pointwise geometry, the spectrum and unique words are already covered, even under a stronger cost model. The mean, counts and enumerator are direct arithmetic summaries of those results, not a separate valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
