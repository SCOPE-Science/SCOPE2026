# Scientific review: Radau IIA on triangular graphs

## Correctness — PASS

The theorem is supported by an explicit three-eigenvalue graph decomposition, a rational interpolation identity, and three entry formulas. The diagonal and edge thresholds are proved using exact rational witnesses, coefficient-sign counting and the strictly negative cubic discriminant at the sharp last edge-positive dimension. Reconstructed formulas satisfy the matrix polynomial identity, conservation of mass and the required boundary signs. The standalone exact-rational `check.py` passed 3,770 comparisons, including 25 complete-matrix identities. This is self-review; neither exhaustive finite computation nor independent verification is claimed.

## Originality — PASS on currently inspected evidence

Relevant primary literature treats general SSP/absolute monotonicity, diagonally balanced Padé approximation, or TR-BDF2. These results do not imply the evaluated two-stage Radau IIA phase thresholds on \(J(n,2)\). A search under the aliases triangular graph, Johnson graph \(J(n,2)\), and line graph of a complete graph did not disclose the same pair of thresholds. Related graph-specific Radau positivity work for paths, cycles, Hamming graphs and complete multipartite graphs concerns different families; for instance \(J(4,2)\) overlaps the last family, but the infinite triangular-graph classification for \(n\ge5\) does not. Search absence is not a uniqueness proof. Residual priority risk remains from older or unindexed numerical-analysis, graph-filter and association-scheme research.

## Value — PASS

A graph-heat integrator may be algebraically stable while its finite-step propagator temporarily loses positivity. The theorem locates **two different, sharp dimension thresholds** (\(6\) and \(75\)) for distinct entry types, fully characterizes every sign interval by small-degree polynomials and proves unconditional positivity of all nonadjacent transitions. These are natural and consequential invariants for third-order diffusion on an infinite distance-regular graph family, rather than isolated numerical samples.

## Scope and limitations

Only completed endpoint maps on unweighted triangular graphs are covered; internal stages, weighted graphs and other numerical filters are excluded. Exact arithmetic verifies algebraic formulas on finite samples but is not used as a substitute for the symbolic proof. Older equivalent work may exist despite the inspected comparisons.

Self-review: passed. Independent audit: not yet performed.
