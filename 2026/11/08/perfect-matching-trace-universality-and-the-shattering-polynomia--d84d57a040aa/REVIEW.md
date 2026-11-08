# Review of perfect-matching trace universality

## Correctness — PASS

The restriction from any derangement graph to a support is a matching. For a proposed matching trace on at most \(n-2\) cells, the residual \(k\)-by-\(k\) board has at most \(k-2\) extra forbidden cells beyond a partial diagonal matching. Complete that partial diagonal to one full matching; the other \(k-1\) disjoint factors ensure a factor avoiding all extra forbidden cells. The \(n-1\) obstruction has two exhaustive cases according to whether the unused row and column coincide. Inclusion-exclusion counts the remaining matchings. The sampling limit follows from a full-board birthday calculation and the \(O(m/n)\) diagonal conditioning error. An independently written script performs direct trace tests; the calculations are not used to infer the infinite theorem.

## Originality — PASS within researched comparisons

Bucić et al. (arXiv:1906.05908) study intersection proportions of perfect matchings and counting derangements, not the VC shattering complex of graph-incidence positions. Johnson–Wickes (arXiv:2112.01946) study order-pattern shattering of symbol subsets, not Boolean traces on pairs \((i,j)\). Searches for edge-incidence VC dimension, crown graph perfect-matching traces, derangement shattering, rook-polynomial matching complexes and equivalent parameter \(n-2\) returned no matching published statement. The preclusion/factorization and rook enumeration ingredients are classical; the proposed novelty is their sharp *trace-family identity*, including its exact failure layer. This is qualified historical priority, not independence or an exhaustive uniqueness assertion.

## Mathematical value — PASS

The result connects a natural definable concept class (incidence of a position in a fixed-point-free permutation) to a matching complex **on every sufficiently small support**, a stronger fact than computing its VC dimension. It determines the entire shattered-support distribution, identifies the sharp difference between unrestricted and fixed-point-free assignments at the largest support sizes, and exhibits a birthday-scale random-shattering threshold \(\sqrt n\) despite worst-case VC dimension \(n-2\). These are unrestricted-in-\(n\), exact structural statements, not a recomputation of a numerical table.

## Risks and limits

The extension property uses the special complete off-diagonal board; general bipartite graphs may fail. Related results could be catalogued under matching preclusion or partial Latin transversals. A complete historical-priority audit and independent proof review have not been performed.

Self-review: passed. Independent audit: not yet performed.
