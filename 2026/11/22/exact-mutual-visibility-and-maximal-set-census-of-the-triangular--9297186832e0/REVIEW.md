# Scientific review

## Correctness — PASS

The claimed finite census has a rigorous exhaustiveness argument. In \(C_3\square C_8\), every geodesic consists of a shortest arc of \(C_8\), with a unique row change at an arbitrary point only if the endpoint rows differ. Both checker implementations independently generate all possible shortest-path interiors. The vertex-subset predicate tests whether each selected pair has an interior-disjoint geodesic. It is hereditary. The increasing-index recursion consequently lists each feasible subset once and excludes nothing feasible, and the one-vertex-extension criterion decides inclusion-maximality exactly. Compiled C++ BFS/path enumeration and Python Cartesian-arc enumeration agree in all ten coefficients, maximal counts, and two totals when executed from the package. No extrapolation from test widths or finite sampling is used. The specific seven-set is checked as an attaining witness.

## Originality — PASS, provisional

Brešar and Yero introduce the lower invariant and pose the torus problem, rather than solve this case. Korže and Vesel determine the maximum visibility number for \(C_3\square C_8\) (nine), not its minimum inclusion-maximal number or either counting polynomial. The published odd-three-row-torus result is mathematically close but expressly assumes an odd cycle of length at least five and excludes even widths. Its full available RESULT.md was read; the odd proof relies on unique shortest arcs, unlike this antipodal even case. Queries against mathematical research records using the graph, invariant and equivalent descriptions, and searches of primary literature found no covering even-width theorem or existing table of these coefficients. Exact priority remains provisional because nonindexed computations and inaccessible literature may exist. The known maximum nine is explicitly not claimed as novel.

## Mathematical value — PASS

The lower mutual-visibility invariant measures how few vertices a greedy maximal visible placement can have, distinct from its well-studied maximum. A 2023 open problem explicitly asks for toroidal Cartesian graphs, and prior work settles odd three-row circumferences at five. This natural first nontrivial larger even eight-column benchmark gives the exact lower size seven, counts all 4,608 smallest maximal sets, and finds all maximal cardinalities and multiplicities. The complete polynomial data reveal the distribution of greedy outcomes on a symmetric torus, not a cosmetic reparametrization of the known upper value. A broader even-width formula is neither asserted nor needed for this self-contained benchmark.

## Closest sources and limits

Primary comparators are Brešar–Yero (2023, arXiv:2307.02951, concluding Problem 1), Korže–Vesel (2024, DOI:10.1007/s00025-024-02139-x, Section 3 and Proposition 3.9), and the published 2026 odd-three-row-torus theorem (https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-lower-mutual-visibility-number-of-odd-three-row-tori--543189f5b94a). A recent fault-tolerant-visibility paper was available only through a theorem excerpt; it treats maximum k-fault-tolerant configurations and not this stated minimality criterion. The result is finite and fully enumerated, with reproducible source and outputs, but not independently audited by a separate mathematician.

Self-review: passed. Independent audit: not yet performed.
