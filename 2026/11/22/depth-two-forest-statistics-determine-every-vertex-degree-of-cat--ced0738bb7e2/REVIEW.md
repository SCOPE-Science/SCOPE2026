# Scientific review: Catalan-matroid one-skeleton degree spectrum

## Correctness — PASS

The statement is quantified for every positive semilength, and the adjacency notion is the ordinary matroid base-polytope one-skeleton. The proof separately counts root–descendant node pairs, pairs internal to one depth-two subtree, ordinary disjoint pairs, and swaps of the matching \(UD\) pair itself. The two exceptional counts cancel, leaving precisely \(\binom n2+\sum_i\binom{s_i}{2}\). The formal series follows from the ordered-sequence decomposition of the Dyck forest. Disjointness of depth-two subtrees and strict convexity of binomial coefficients establish all extrema and their complete equality cases. Independent exhaustive swaps and a separately constructed recurrence agree for every word of semilength at most nine. The theorem does not extrapolate from enumeration.

## Originality — PASS (historical priority provisional)

The original Catalan matroid presentation and the general matroid-base adjacency criterion are established prior work. Published treatments give lattice-path-polytope edge counts (Bidkhori; An–Jung–Kim) and the Dyck-word random-transposition walk with negative correlation and mixing results (Cohen–Tetali–Yeliussizov). These are the closest objects: the former have aggregated one-skeleton counts; the latter uses exactly the same moves. Neither inspected primary text evaluates the degree at each vertex, the full depth-two block degree polynomial or the minimizing/maximizing forest configurations. Indexed results on a Dyck deletion ambiguity graph concern a different move relation. Unknown unindexed equivalent statements remain a residual risk; comparison is by mathematical implication, not just titles.

## Mathematical value — PASS

The complete degree enumerator refines the known total-edge count into all local exchange possibilities, with an explicit two-variable Catalan generating series and rigid extremal configurations. The result is a natural structural graph invariant useful for studying inhomogeneity of basis-exchange networks, and it reveals the unusual contrast between the \(2^{n-1}\) minimum-degree vertices and the \(C_{n-2}\) maximum-degree vertices for \(n\ge3\). It is not a finite-sample recomputation or a renaming of existing graph-edge totals.

## Limits and closest literature

Published general edge enumerations and mixing results are not being claimed as new. Full-text comparisons cover arXiv:1701.00362, arXiv:1212.5705 and arXiv:1505.06710. The standalone exact enumeration reaches \(n=9\); the proof treats all \(n\ge1\). Unindexed equivalent results remain possible, and no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
