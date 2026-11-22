# Scientific review: sharp graded-type reconstruction boundary in finite two-graphs

## Correctness — PASS

The one-point extension classification follows from the four-set parity axiom: the \(n-1\) triple values with the distinguished old point uniquely determine all other newly incident triples. Graph lifting proves existence for every binary assignment, and homogeneity identifies diagrams with complete singleton types. The polynomial formula therefore counts exactly \(2^{n-1}\) types at every parameter size. The finite census uses all \(2^{\binom{n-1}{2}}\) rooted graph encodings and a complete isomorphism action, not samples. A separate all-encodings polynomial count and the direct 21-fiber certificates independently corroborate the decisive calculations. Replay commands and exact outputs are in VERIFICATION.md. The assertion is explicitly confined to parameter order at most eight.

## Originality — PASS, provisional historical priority

The switching correspondence and the numbers of two-graph isomorphism classes are prior results. Bussemaker–Mathon–Seidel's full 1979 report classifies the original objects and their Seidel spectra, not the new one-point-type grade polynomials or the latter's collision fibers. The 2009 Andrén–Markström bivariate Ising polynomial records magnetization and cut sizes for ordinary graphs; it is not the one-variable cut-coset grade of a two-graph. The three displayed collision witnesses have different ordinary-graph edge counts and different Seidel characteristic polynomials, confirming a nontrivial distinction between the invariants. Greaves et al. provide subsequent Seidel-theoretic classifications without the claimed extension-type reconstruction result. Actual source and equivalence checks are recorded in AUDIT.json. Historical priority remains qualified by possible unindexed signed-cut weight enumerators.

## Mathematical value — PASS

The statistic is the complete grade distribution of all atomic singleton extensions in a natural homogeneous ternary structure, not an arbitrary graph encoding. The finding establishes the smallest parameter size at which that distribution loses the underlying configuration, enumerates the complete failure fiber structure, and identifies a natural local incidence refinement that restores reconstruction at the boundary. The three-member collision has pairwise different Seidel spectra, so even standard spectral comparison does not explain it. The result is finite and self-contained; no higher-order or asymptotic extension is claimed.

## Closest literature and limits

- Bussemaker, Mathon, Seidel (1979), *Tables of two-graphs* — complete small two-graph and Seidel-spectral tables, not this grade invariant.
- Andrén, Markström (2009), *The bivariate Ising polynomial of a graph* — ordinary-graph cut and magnetization enumerators with different isomorphism equivalence.
- Greaves et al. (2014), *Equiangular lines in Euclidean spaces*, arXiv:1403.2155 — Seidel matrices and equiangular systems, not the present type-grade fibers.

There has been no independent audit. The exact reconstruction result is proved only through eight parameters; source coverage cannot exclude every unindexed equivalent formulation.

Self-review: passed. Independent audit: not yet performed.
