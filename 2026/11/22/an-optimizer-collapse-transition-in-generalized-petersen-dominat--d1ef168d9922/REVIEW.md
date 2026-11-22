# Scientific review

## Correctness — PASS

The statement fixes the exact graph adjacency and [1,2]-domination predicate. The 2019 source and complete enumeration prove the minimum cardinality is six for each order. Separately implemented Python and C++17 exhaustive checks establish both optimum counts, complete shattered-support coefficients and exact online ranks. Python enumerates every smaller cardinality; both programs enumerate every size-six candidate, all supports to the first vanishing coefficient, and the recurrence over every reachable online residual state. For order eight, the two 16-member maximum-support orbits, 660 maximal four-faces and 32 maximal five-faces are tested; for order nine, all nine optima match the explicit three-by-three phase family. Full depth-six and depth-two online trees are checked from nonempty leaves upward. Neither finite testing nor a time limit is used to claim an infinite-order theorem.

## Originality — PASS, with historical priority caveat

Beggas et al., arXiv:1906.11966 (first public 2019-06-27), establishes minimum cardinalities for the family but no minimum-set counts, membership trace complexes or Littlestone ranks. Its original accessible full text, including the relevant small-order base cases and the conclusions, was read. Chen et al. (2018), DOI 10.1016/j.amc.2018.01.013, has a closely relevant title and determines optimum cardinalities, but its full text was not accessible, so no assertion of whole-document noncoverage is made. Relevant published-search and mathematical-record comparisons show different domination notions or different underlying graph/concept classes, not stronger covering results. Unindexed equivalents remain possible.

## Value — PASS

The published period-six minimum cardinality formula gives equal optimizer budgets of six at adjacent residues eight and nine. Yet the optimizer count drops from 248 to 9, the VC dimension from five to two, and the adaptive dimension from six to two. The exact three-by-three phase description at order nine and the two dihedral maximum-face orbits at order eight explain the contrast in optimizer geometry. This is a motivated boundary between optimizer diversity and optimal cardinality, not a generic enumeration of an arbitrary graph or a restatement of a domination-number theorem.

## Remaining limitations

The result does not classify all generalized Petersen orders or the full integral topology of the order-eight shattering complex. The exhaustive programs are executable proof certificates for the specified finite orders, but do not replace an independently conducted external mathematical audit. Historical priority is qualified by the inaccessible 2018 full text and by the ordinary incompleteness of research indexing.

Self-review: passed. Independent audit: not yet performed.
