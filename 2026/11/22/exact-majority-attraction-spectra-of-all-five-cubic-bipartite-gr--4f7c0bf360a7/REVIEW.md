# Scientific review: all connected cubic bipartite twelve-vertex majority dynamics

## Correctness: PASS

The claim is a finite complete-class result. The proof exhaustively enumerates all connected cubic bipartite graphs on twelve vertices as six-by-six degree-three matrices, proves the normalization and isomorphism relation, and verifies that precisely five types remain. For all five types, every one of 4096 states is checked against the exact binary majority rule. Two different implementations agree on the sharp identity \(F^4=F^2\), every first-entry/period count, and every orbit-basin multiplicity. Each class has states first becoming periodic at step two. The graph names are verified with explicit isomorphism searches. All scripts and graph data are included.

## Originality: PASS (historical-priority qualification)

Goles and Olivos give a general eventual two-period theorem. Kaaser, Mallmann-Trenn and Natale provide general upper bounds on majority voting time, including their bound 13 for the present graph order and degree, but not the two-update equality or the complete five-class basin census. A published five-graph domination classification concerns a different invariant. Relevant search results for Heawood and dodecahedral majority dynamics concern other graphs. Searches for Franklin, hexagonal-prism and cubic-bipartite majority basins yielded no covering table. An unindexed equivalent or inaccessible graph-specific full text remains a risk, not a claim of guaranteed priority.

## Value: PASS

The five connected cubic bipartite graphs of the same minimal natural order provide a complete controlled comparison of local degree and graph order under identical majority dynamics. The precise clock is universal but orbit/basin populations vary by more than thirtyfold (six to 231 primitive two-cycles), and two graphs with the same number of squares have distinct attraction spectra. The hexagonal prism uniquely maximizes oscillation likelihood, while the Franklin graph uniquely maximizes the largest individual basin; these are exact, interpretable finite dynamical invariants, not arbitrary isolated samples.

## Closest sources and limitations

Relevant references: Goles–Olivos (1980), DOI 10.1016/0012-365X(80)90121-1; Kaaser–Mallmann-Trenn–Natale (2015), arXiv:1508.03519v1, inspected definitions, theorems, general bounds and appendix passages; MathWorld's Franklin-graph description; and a recent published comparison on five cubic bipartite graphs addressing paired domination rather than majority. The general majority results have a broader graph domain but do not imply the new exact finite table. Mathematical scope is exactly twelve vertices. Historical-priority and external-validation uncertainties are retained.

Self-review: passed. Independent audit: not yet performed.
