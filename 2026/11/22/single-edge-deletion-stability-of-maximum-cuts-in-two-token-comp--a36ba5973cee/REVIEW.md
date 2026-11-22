# Scientific review of a one-edge perturbation theorem

## Correctness: PASS

The exact two-token cut identity partitions the Johnson graph's edges into the cliques of token states sharing one base vertex and deducts only the edges induced by the missing base edge. The upper bound is proved independently by maximizing local degree terms and imposing the handshake parity obstruction. Four separate all-order red-graph constructions have the stated degree patterns and synchronize the deleted edge's endpoints, so they attain that bound at every nonexceptional order. At order five, the handshake lemma forbids a Johnson cut one unit below the upper bound, and a five-cycle cut loses exactly two crossing token edges; a complete degree-pattern count gives 32 ordered optima. An independent direct adjacency enumerator agrees for all two-colourings at orders three through six; construction checks cover every order from three through 100.

Risk: The finite tests cannot replace the all-order constructions; the upper bound is proved directly, and every construction is explicitly stated in the proof. There are no additional computational assumptions in the theorem.

## Originality: PASS, with priority limitations

The motivating 2025 study by Apte, Parekh and Sud (arXiv:2506.03441v1, first posted 2025-06-03) relates token-graph spectra to cut parameters and explicitly identifies complete-graph token graphs with Johnson graphs; it does not study the objective maxcut of an edge-deleted token graph. A separately inspected, later 2026 paper by Alejandro-Soto et al. (arXiv:2611.25153v1, first posted 2026-11-18) establishes the maximum cut of the intact triangular Johnson graph and a local balancing condition. The new theorem instead determines the maximum cut after removal of a base edge, which deletes a matching of \(n-2\) token-graph edges, and characterizes the resulting optimizers and exceptional five-vertex census. Matching wordings are not sufficient for this distinction: the later intact-graph result supplies an upper bound, but not a synchronized, degree-balanced construction in the edge-deficient graph. The source comparisons read material sections of both primary articles (including original v1 of the 2025 paper and the full relevant Section 3.1 of the later 2026 paper), not only their abstracts. Additional direct and alias literature searches found no equivalent theorem, and searches across relevant publicly indexed prior claims found no covering comparison.

Risk: There may be an unindexed older result about the triangular Johnson graph after a matching deletion; one older Johnson-graph eigenvalue paper was surveyed only at abstract level. This qualification is not a claim of independent validation or historical uniqueness.

## Value: PASS

The result establishes a sharp stability threshold for maximum cuts under a minimal perturbation of an explicitly studied class: deleting an entire matching of \(n-2\) token edges has zero effect on the optimum at every order other than five, where the deficit is exactly two. It provides a construction in every parity class, a necessary and sufficient characterization of optimal cuts and an exact small exceptional census. This is more informative than applying the known Johnson upper bound, and the parity-sensitive failure identifies the precise first obstruction to simultaneous local balance and endpoint synchrony.

Limitations: Only the two-token graph and a single deleted base edge are treated; no uniform multi-edge deletion statement or all-order optimal-cut enumerator is asserted.

Self-review: passed. Independent audit: not yet performed.
