# Self-review

## Correctness (C): PASS

The argument specifies the entire family of open neighborhoods on \(\square_i P_{n_i}\), with all side lengths at least two, and shattering of unordered sets of vertex queries. Bipartiteness and the one-or-two common-neighbor rule prove that there are no shattered quadruples, and the pair test has an explicit necessary-and-sufficient private-neighbor condition. For three-query supports the proof first forces three different coordinate axes, then separates the singleton-trace obstructions at an interior versus boundary center, accounting for every possible number of interior coordinates. Counting centers uses uniqueness of the containing open neighborhood, preventing duplicate counts. The standalone checker uses independently constructed graph traces, reproducing all coefficient vectors through degree four for 21 parameter boxes; it is evidence for the finite cases, not the proof of unbounded parameters. The only limitation on C is that it applies to the stated Cartesian path products, not arbitrary induced subgraphs.

## Originality (O): PASS (historical priority qualified)

Adler, Benediktsson and Macpherson (arXiv:2007.16042, first posted 2020-07-31), Section 4, establish the open-neighborhood VC-dimension upper bound three for Hamming graphs and their induced subgraphs, but not the rectangular Cartesian-path support counts. The public exact full-Hamming coefficient census explicitly does not claim induced-subgraph formulas: its all-binary special case is already prior art. An inspected path-grid profile counts *geodesically convex subsets*, not the open-neighborhood concepts. A separate rank-three first-order theory classification of path boxes neither gives shattering traces nor their coefficients. The closest results were compared by mathematical implication rather than title or numerical degree; none inspected supplies the displayed boundary-sensitive cubic coefficient for arbitrary path boxes. Residual historical-priority risk persists for unindexed equivalent formulas or uninspected papers. No independence is claimed.

## Value (V): PASS

The previously known uniform VC upper bound does not count which supports are shattered after boundary truncation. The new exact polynomial solves the complete finite support census for any number of nontrivial path factors, with a genuinely different boundary phase in dimension three: two specific box types have dimension two while all other three-dimensional boxes have dimension three. The formula additionally distinguishes spaces with the same scalar VC dimension, giving a motivated model-theoretic/neighborhood-complex invariant beyond routine scalar dimension evaluation.

## References and limits

- Adler, Benediktsson and Macpherson, arXiv:2007.16042, Section 4, first posted 2020-07-31.
- *Coefficientwise VC-shattering census of open neighborhoods in Hamming graphs*, public research record (2026), full scientific statement and proof inspected, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-coefficientwise-vc-shattering-census-of-open-neighborhoods-in-ha--c2c444ddd1a2.
- *Exact VC-shattering polynomial of rectangular path grids*, public research record (2026), geodesic-convexity result compared, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-vc-shattering-polynomial-of-rectangular-path-grids--dd0fe3219184.
- Coudert, Csikós, Ducoffe and Viennot, *Practical Computation of Graph VC-Dimension*, SEA 2024, DOI:10.4230/LIPIcs.SEA.2024.8, closed-neighborhood computational context.

Self-review: passed. Independent audit: not yet performed.
