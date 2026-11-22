# Review: sharp cutwidth-constrained order reconfiguration on stars

## Correctness — PASS
The statement fixes individually labelled stars, integer cutwidth budgets and swaps of neighboring *positions*. The cutwidth identity \(\max(c,r-c)\) follows from every prefix's actual crossing-edge count. At the unique balanced hub position, no legal hub move exists, giving exactly the stated Cartesian-product components. At two or more feasible hub positions, the interval-position lemma proves that every non-target order has a legal adjacent target inversion; therefore no routing detour is needed and the exact pairwise distance is Kendall inversion distance. Reversal remains feasible and witnesses eccentricity \(\binom{r+1}{2}\) for every vertex. Counting leaf-only and hub-moving edges completes the theorem. Independent enumeration of actual star cuts, components and distances in the included `verify.py` passed for 35 parameter pairs, including \((r,k)=(8,5)\). Finite checking is corroboration, not the all-order proof.

## Originality — PASS, with historical-priority risk
Arrighi, Fernau, de Oliveira Oliveira and Wolf [1,2] establish general adjacent-order reconfiguration with permitted cutwidth increasing to twice its initial budget, but do not give an exact within-budget star threshold or full Kendall-isometry statement. The classical unrestricted adjacent-transposition metric does not by itself ensure the same path remains inside a constrained induced subgraph. Related indexed permutation problems [3,4] respectively impose forbidden fixed points and describe a partial-permutohedral facet; neither statement contains the fixed-hub rank-window theorem. Searches for star cutwidth reconfiguration, one-letter positional intervals, geodesic adjacent sorting and their implication-equivalent formulations identified no covering publication. An older equivalent under different terminology cannot be ruled out, and this review does not imply an independent priority assessment.

## Value — PASS
The original work motivates studying *reachability under a fixed cutwidth budget*, where a general twofold width allowance was previously sufficient. A star is the smallest nontrivial family for which optimal cutwidth itself can create multiple components. The exact theorem determines a sharp all-order phase transition: even stars at optimum width have exponentially many components, but at optimum plus one all states become reachable with zero Kendall-metric overhead. Odd stars already have this shortest-path property at optimum. This yields a complete optimal-routing algorithm, exact diameter, component census and edge counts for the entire infinite star family. The metric conclusion is stronger than merely proving a permissible sorting sequence exists.

## Closest literature and limits
[1] E. Arrighi, H. Fernau, M. de Oliveira Oliveira, P. Wolf, *Order Reconfiguration Under Width Constraints*, MFCS 2021, https://doi.org/10.4230/LIPIcs.MFCS.2021.8.

[2] Same authors, *Order Reconfiguration under Width Constraints*, JGAA 27(6) (2023), https://doi.org/10.7155/jgaa.00628.

[3] *Component signatures for permutations avoiding selected fixed points*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-component-signatures-for-permutations-avoiding-selected-fixed-po--79c08e75f702.

[4] *Geodesic rigidity of the permutohedral facet in partial permutohedra*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-geodesic-rigidity-of-the-permutohedral-facet-in-partial-permutoh--7910cdad70d2.

The claim is restricted to unweighted stars and cutwidth, not weighted trees or pathwidth. Independent mathematical audit and exhaustive historical-priority review remain unperformed.

Self-review: passed. Independent audit: not yet performed.
