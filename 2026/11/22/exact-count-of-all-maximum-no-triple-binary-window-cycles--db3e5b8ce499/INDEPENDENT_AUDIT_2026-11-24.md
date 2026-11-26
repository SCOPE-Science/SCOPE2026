# Independent mathematical audit

## correctness

PASS

In the full no-triple overlap graph, the vertices of out-minus-in degree +1 begin with an equal pair and end with an unequal pair, and the −1 vertices have the reverse predicate. Any balanced edge set omits at least one outgoing edge from each +1 vertex. Equality requires the deletions to run directly from +1 to −1 vertices, forcing precisely the equal-pair-at-both-ends edges: a +1 vertex has only one such outgoing extension. These deletions do balance the graph. Appending alternating bits reaches a branch, and an alternating vertex with an unequal junction to a target can append all its letters while the first pair of each traversed edge differs. This proves attainability and rigid support independently of the cited premise. In the resulting graph, only the 2F_(n−2) vertices unequal at both ends branch (choose the initial bit and compose n−3 into ones and twos). All other vertices have one outgoing edge and reach a branch in at most n−1 shifts. Their forced exits give a bijection of in-arborescences before and after contraction, with parallel arcs kept distinct. The directed last-exit/BEST count with one fixed initial labeled edge counts each rotation class once and has unit factorial factor; the outgoing matrix-tree cofactor is consequently exactly the asserted count. Independent replay: python3 /workspace/review_checks/1.py (SymPy integer determinants) reproduced the table through n=11, with full graph cofactors through n=9 and direct rotation-class optimization at n=4,5. These checks do not replace the all-n proof.

## originality

PASS

Credit the sharp length, canonical support, classical Euler-tour/tree methods, and the strong one-sided methodological antecedent. The distinct result is the explicit branch-sized determinant and maximal-cycle census for the two-sided support. The uncompressed cofactor follows directly from the older support and BEST, so that alone would not justify a pass.

## value

PASS

Knowing one optimal schedule or its window set does not identify how many schedules achieve it. The reduced determinant gives a concrete exact census for the entire natural two-sided run-limited family, with a computational reduction from 2F_n−1 to 2F_(n−2)−1 and exact counts far beyond direct listing. The value is the explicit efficient population count, not an advance in the optimum length or in abstract Euler-tour theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
