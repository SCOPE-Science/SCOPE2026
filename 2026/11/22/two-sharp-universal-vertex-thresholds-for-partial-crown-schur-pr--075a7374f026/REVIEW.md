# Self-review

## Correctness — PASS

The finite-dimensional Schur norm has the exact dual weighted trace-norm representation used here. Its joint concavity justifies symmetry averaging, including rectangular masks, and equal universal rows/columns have an exact unitary compression. The stated eigenvalues and singular values reduce the global optimizations to two strictly concave one-variable functions; the derivative cutoffs and stationary values give all five branches. Polar-decomposition witnesses attain the upper bounds. The bundled finite diagnostic reports `PARTIAL_CROWN_SCHUR_DIAGNOSTIC_OK 1371`; its finite sampling is not an infinite proof.

## Originality — PASS, qualified

Levene (2014) already proves the small \(9/7\) three-by-three value and implies the \(2/\sqrt3\) two-by-three value, and neither is claimed as new. Levene (2026) gives the core norm and develops tree-attached norm problems; it does not state the all-parameter universal-row/column formula. Published signed-diagonal-mask and star-ball-mask records describe different support patterns or signs. Full-text comparisons include the papers identified in `AUDIT.json`, with actual statement-level differences rather than title-only comparisons. General γ2 machinery could make this an implicit specialization; Christensen (2025) was compared only at abstract level. Independent priority checking is outstanding.

## Mathematical value — PASS

The object is a canonical partial-crown incidence mask and the parameter operation (adding complete-bipartite universal vertices) is a natural test of norm stability. The result answers completely, in arbitrary finite dimensions, whether added rows alone, columns alone, or both alter the Schur projection norm; it identifies two different sharp transition sizes and explicit values/witnesses. This is stronger than knowing individual small matrices or the underlying variational characterization, and is not dependent on an unproved downstream conjecture.

## Scope and risk

The theorem concerns one deleted matching in an otherwise complete bipartite graph, not arbitrary graph deletions. General previous norm-factorization principles and the known \(k=2\) cases are credited. An older exact formula under different vocabulary could exist, and independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
