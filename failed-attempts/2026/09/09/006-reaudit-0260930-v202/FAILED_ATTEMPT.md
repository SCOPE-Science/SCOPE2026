# FAILED ATTEMPT — NOT A VALIDATED FINDING

Independent reassessment on 2026-09-30 UTC did not validate this finding because not all C/O/V axes passed.

Correctness: PASS. Fresh reconstruction of the Petersen, Clebsch, Shrikhande and 4-by-4 rook adjacency matrices reproduces the stated singleton vertex-deletion behavior and exact card characteristic polynomials. The Shrikhande and rook cards have identical characteristic polynomials, while direct exact checks give clique numbers 3 and 4, K4 counts 0 and 6, and spanning-tree counts 2177280000 and 2176782336. These values are internally correct.

Originality: FAIL. The record’s context overstates the gap. Before this record, Delta-DRESS had already applied a single level of vertex deletion and reported separation of the classical rook L_2(4) and Shrikhande pair. More fundamentally, the exact equality of their vertex-deleted characteristic polynomials follows from standard spectral reconstruction: the derivative of a graph characteristic polynomial is the sum of the characteristic polynomials of its vertex-deleted subgraphs. Because both graphs are vertex-transitive, every card within each deck has the same characteristic polynomial; because the parents are cospectral, the card polynomials must coincide. Thus the headline spectral persistence is a textbook implication, while deck-level separation was already reported.

Scientific value: FAIL. The exact numerical certificates are reliable, but the main phenomena do not open a new mathematical gap: singleton decks follow from vertex transitivity, card cospectrality follows from the characteristic-polynomial derivative identity and parent cospectrality, and prior deletion-fingerprint work already separates the pair. The extra clique and tree counts are useful diagnostics but do not supply a new structural result or a motivated unknown invariant sufficient to rescue the standalone claim.

The original research files and computational evidence are retained for traceability; this marker does not alter their historical content.
