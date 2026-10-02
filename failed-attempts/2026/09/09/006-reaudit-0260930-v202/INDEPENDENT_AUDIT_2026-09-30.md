# Independent audit — SCOPE-20260909-006

Audited at: 2026-09-30T22:14:07Z

Disposition: **failed**

## Correctness

**PASS** — Fresh reconstruction of the Petersen, Clebsch, Shrikhande and 4-by-4 rook adjacency matrices reproduces the stated singleton vertex-deletion behavior and exact card characteristic polynomials. The Shrikhande and rook cards have identical characteristic polynomials, while direct exact checks give clique numbers 3 and 4, K4 counts 0 and 6, and spanning-tree counts 2177280000 and 2176782336. These values are internally correct.

## Originality

**FAIL** — The record’s context overstates the gap. Before this record, Delta-DRESS had already applied a single level of vertex deletion and reported separation of the classical rook L_2(4) and Shrikhande pair. More fundamentally, the exact equality of their vertex-deleted characteristic polynomials follows from standard spectral reconstruction: the derivative of a graph characteristic polynomial is the sum of the characteristic polynomials of its vertex-deleted subgraphs. Because both graphs are vertex-transitive, every card within each deck has the same characteristic polynomial; because the parents are cospectral, the card polynomials must coincide. Thus the headline spectral persistence is a textbook implication, while deck-level separation was already reported.

### Equivalent formulations

The equal card polynomial for the cospectral vertex-transitive Shrikhande and rook graphs is forced without the record’s computation.

Evidence: A standard theorem states phi_G prime equals the sum over vertices of phi_(G-v). For a vertex-transitive graph all terms agree, so one card polynomial equals phi_G prime divided by the number of vertices.

### Broader coverage

Prior work already establishes a deletion-based distinction of the same pair, although with a different invariant.

Evidence: The 2026 Delta-DRESS work applies a vertex-deletion fingerprint to these same two SRGs and reports that it separates the pair, within a much broader benchmark study.

### Exact database or table

The exact numbers may be newly tabulated, but the central spectral equality is a direct consequence of a standard identity and the separation question was already answered by prior deletion-based work.

Evidence: No earlier table with the exact displayed card polynomial and both spanning-tree counts was found.

### Claim versus prior implication

The main advertised deck-spectral persistence is prior-theorem implied, and the broad separation narrative is not new.

Evidence: Parent cospectrality and vertex transitivity imply card cospectrality; Delta-DRESS predates the record and separates Rook L_2(4) from Shrikhande after one deletion level.

## Scientific value

**FAIL** — The exact numerical certificates are reliable, but the main phenomena do not open a new mathematical gap: singleton decks follow from vertex transitivity, card cospectrality follows from the characteristic-polynomial derivative identity and parent cospectrality, and prior deletion-fingerprint work already separates the pair. The extra clique and tree counts are useful diagnostics but do not supply a new structural result or a motivated unknown invariant sufficient to rescue the standalone claim.

## Sources inspected

- **Breaking Hard Isomorphism Benchmarks with DRESS** (arXiv:2603.18582): Primary arXiv record and relevant paper material describing Delta-DRESS and its separation of the SRG(16,6,2,2) pair. Assessment: PRIOR_DELETION_SEPARATION. Evidence: The paper states that Delta-DRESS, which runs on vertex-deleted subgraphs, separates the classical rook/Shrikhande pair.
- **Graphs Having Most of Their Eigenvalues Shared by a Vertex Deleted Subgraph** (Symmetry 13 (2021) 1663, Section 5, Theorem 11): The reconstruction section and theorem stating that the derivative of the characteristic polynomial equals the sum of the vertex-deleted characteristic polynomials. Assessment: BROADER_SPECTRAL_IDENTITY. Evidence: Combined with vertex transitivity, the theorem makes each card polynomial equal to one-nth of the parent derivative.

## Residual risks

- The exact spanning-tree numbers were not located in prior literature, but they are ancillary to a headline whose main spectral and separation phenomena are already implied or previously demonstrated.
