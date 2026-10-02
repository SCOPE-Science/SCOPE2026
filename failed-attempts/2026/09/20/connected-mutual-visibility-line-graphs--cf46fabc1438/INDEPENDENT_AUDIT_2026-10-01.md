# Independent mathematical audit — SCOPE-20260920-cf46fabc1438

Final disposition: **FAILED**.

## Correctness
**PASS** — The saturation-connectivity argument is correct. Under the established translations, an inclusion-maximal mutual-visibility set in \(L(K_n)\) is a \(K_4\)-saturated spanning subgraph of \(K_n\), and in \(K_m\square K_n\) it is a \(C_4\)-saturated spanning subgraph of \(K_{m,n}\). If two nontrivial components existed, adding a host edge between them could not create the connected forbidden graph, contradicting saturation; in the bipartite case an isolated vertex is likewise impossible. Thus the selected-edge graph, and hence its line graph, is connected. The stated Turán and saturation values then follow from the prior forbidden-subgraph correspondences.

## Originality
**FAIL** — The rook-graph half is exactly covered by an earlier September 19 published finding that proves every inclusion-maximal rook mutual-visibility set connected and \(\mu_c(K_m\square K_n)=z(m,n;2,2)\). The triangular half is a direct application of the same elementary saturation-connectivity observation to the already-published \(K_4\)-free characterization of mutual visibility in \(L(K_n)\); the numerical values are classical Turán and saturation numbers. Under an implication-based originality bar, no substantial final claim remains original.

### Equivalent formulations
Both connected-mutual-visibility claims reduce exactly to connectivity of saturated forbidden-subgraph hosts.

### Broader coverage
Prior results either exactly cover or mechanically imply the assigned conclusions.

### Exact database or table
The exact values/reductions do not constitute a new database fact once the prior correspondence is fixed.

### Claim versus prior implication
The assigned final theorem is covered by exact prior work plus a routine corollary.

## Value
**FAIL** — The graph-theoretic transfer is correct and useful expositionally, but the rook theorem is duplicated and the triangular theorem is a short mechanical consequence of the prior forbidden-subgraph characterization plus a generic fact about saturation by a connected forbidden graph. It does not provide a surviving structural gap beyond those ingredients.

## Source inspections
- **Connected mutual visibility of rook graphs is exactly the Zarankiewicz number** (https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-connected-mutual-visibility-rook-graphs--529e09d087e2): complete published RESULT.md Method: published-record full-text inspection. Assessment: EXACT_PRIOR_COVERAGE_FOR_ROOK_GRAPHS. Evidence: It states every inclusion-maximal rook mutual-visibility set is connected and derives exactly the same Zarankiewicz identity.
- **Mutual-visibility problems on graphs of diameter two** (https://doi.org/10.1016/j.ejc.2024.103995): bibliographic and theorem-level material identifying the \(K_4\)-free characterization used by the assigned package Method: primary-source theorem comparison. Assessment: PRIOR_STRUCTURAL_INPUT. Evidence: The ordinary mutual-visibility problem on \(L(K_n)\) is reduced to \(K_4\)-free selected edges.

## Residual risks
- No correctness defect is asserted; rejection is scientific coverage/routine implication.
- The very recent connected-mutual-visibility literature may contain further parallel statements, but additional coverage would not alter the rejection.
