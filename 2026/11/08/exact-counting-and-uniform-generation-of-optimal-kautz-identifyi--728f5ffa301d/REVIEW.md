# Review of the Kautz identifying-code enumerator

## Correctness — PASS

The prefix-twin lower bound and equality case are proved directly, yielding a cycle cover on the lower-order Kautz digraph. The two-cycle-free condition follows from the exact singleton and two-element closed incoming signatures. For orders at least four the three forbidden directed digons constrain disjoint vertex pairs of the next-lower Kautz graph, leaving three of four independent local switch assignments in each pair. Orders two and three are handled separately. The standard-library finite enumeration and independent C++ signature computation reproduce counts 2, 4, 27, 1728 through length five. Finite outputs support, but do not replace, the all-order combinatorial argument.

## Originality — PASS (qualified)

The original directed de Bruijn identification source (Boutin, Horan Goliber and Pelto, arXiv:1412.5842, 2014) gives the foundational prefix identification argument, not the Kautz extremizer census. The closest strong antecedent is Martínez Barona (doctoral thesis, 2020), which proves the Kautz minimum size and provides a general line-digraph arc-identification characterization. The known minimum size is explicitly excluded from the claimed contribution. The exact all-order number of *labeled* minima and direct uniform generation via three disjoint switch exclusions are not stated in the inspected relevant passages. The antecedent is sufficiently close that independent historical-priority checking remains material.

## Value — PASS

This resolves the enumerative and uniform-sampling problem for every order of a canonical constant-degree network. It distinguishes how often the known minimum is attained and permits rejection-free sampling of optimal sensor placements. The exceptional short orders matter because the forbidden cycles share switches there. The result is a motivated algorithmic classification, not a table recomputation or a purported improvement to the known minimum size.

## Closest literature and limitations

Boutin et al. (2014), arXiv:1412.5842, and Martínez Barona (2020), relevant Chapter 4, are the closest inspected treatments. The theorem is restricted to ternary degree-two Kautz graphs, radius-one closed incoming signatures and labeled optima, and does not enumerate codes up to symmetry. The programs verify finite examples, while the mathematical proof handles infinitely many orders. Historical priority and the infinite proof have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
