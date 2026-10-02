# Independent mathematical audit — 2026-10-01

## Final claim assessed

Connected mutual visibility of rook graphs and the Zarankiewicz number

## Correctness — PASS

PASS. The mathematical reduction is correct. A selected cell set in the rook graph is mutually visible exactly when its row-column incidence graph is C4-free, and the induced rook subgraph is the line graph of that incidence graph. If an edge-maximal C4-free bipartite graph had two edge-containing components, adding an edge from a row in one to a column in the other could not create a C4, contradicting maximality. Hence every inclusion-maximal set is connected and the two maxima agree. The pair-budget calculations for the displayed thin-side cases are also correct. The saved finite enumeration is consistent with, but is not needed for, this proof.

## Originality — FAIL

FAIL. The final connected-visibility identity is mechanically implied by two ingredients that are already available: the published classical rook-graph mutual-visibility/Zarankiewicz correspondence and the elementary saturation observation that an edge-maximal C4-free bipartite graph cannot have two edge-containing components. The latter requires only the one-edge cross-component argument given in the record and is not a new nonstandard lemma. Under the required implication standard, applying a newly named connected parameter to this immediate maximality consequence does not create an original theorem. The later 20 September 2026 published record that repeats the rook-graph statement is follow-up, not the basis of this failure.

### equivalent_formulations

Searches: Resultary semantic search: connected mutual visibility rook graphs Zarankiewicz maximal mutual visibility connected; Cicerone Di Stefano Klavzar mutual visibility Cartesian products rook graph Zarankiewicz

Evidence: The classical Cartesian-product work identifies ordinary mutual visibility in the rook graph with the C4-free bipartite Zarankiewicz problem. The audited connected statement is equivalent to asking whether a maximum C4-free incidence graph has its edges in one component.

Reasoning: Maximum C4-free graphs are edge-maximal, and the cross-component edge argument forces a single edge-containing component. Thus the connected formulation is an immediate equivalent consequence.

### broader_coverage

Searches: arXiv:2112.13024; C4-saturated bipartite graph connectivity Bryant Fu 2002

Evidence: The ordinary rook-graph value is already covered by the classical Cartesian-product theorem; the connectivity step is a generic saturation observation rather than a rook-specific new structure theorem.

Reasoning: The stronger prior coverage of the ordinary maximum plus the elementary maximality implication dominates the new connected maximum.

### exact_database_or_table

Searches: Resultary semantic search for exact rook-graph connected mutual visibility value

Evidence: No numerical database is the relevant prior-art mechanism; the value is inherited from the classical Zarankiewicz extremal function.

Reasoning: A table lookup is specifically inapplicable because the claim is parameterized for all m,n, but the exact classical extremal function already supplies the value once the elementary connectivity implication is applied.

### claim_vs_prior_implication

Searches: arXiv:2609.18877 connected mutual visibility; arXiv:2112.13024 ordinary mutual visibility Cartesian products

Evidence: The 2026 connected-mutual-visibility paper introduces the parameter; the older Cartesian-product result supplies the ordinary rook-graph/Zarankiewicz identity. The remaining step is the one-edge maximality argument.

Reasoning: The final claim is a mechanically implied corollary of prior theory plus an elementary saturation fact, so originality fails even though the exact connected wording is recent.

## Scientific value — FAIL

FAIL. The rook-graph identity is natural, but the claimed contribution is a routine two-line transfer from an established exact correspondence plus an elementary saturation fact. The extra thin-side formulas are equally direct pair-count consequences of the classical Zarankiewicz formulation. This does not clear the stated value bar against textbook deductions and mechanically implied renamings.

## Source inspections

- **Connected Mutual-Visibility in Graphs** — https://arxiv.org/abs/2609.18877. Material read: Primary-source abstract and indexed statement material. Assessment: BACKGROUND_DEFINITION. Evidence: The source introduces the connected mutual-visibility number but its accessible abstract does not provide a rook-graph theorem.
- **On the mutual visibility in Cartesian products and triangle-free graphs** — https://arxiv.org/abs/2112.13024. Material read: Primary-source indexed statement material and the theorem as cited in the audited record; an ar5iv full-text retrieval attempt was unavailable. Assessment: DECISIVE_PRIOR_INGREDIENT. Evidence: It establishes the ordinary rook-graph problem as the C4-free Zarankiewicz problem; the audited connectivity conclusion then follows by the elementary maximality argument.
- **C4-saturated bipartite graphs** — https://doi.org/10.1016/S0012-365X(02)00371-0. Material read: Bibliographic/abstract-level material only. Assessment: RESIDUAL_BACKGROUND. Evidence: Full text was not inspected, but originality already fails without relying on this paper.

## Limitations and residual risks

The correctness proof determines only the connected parameter through the classical Zarankiewicz function; it does not solve the open Zarankiewicz problem.

- The 2002 saturation paper was not inspected in full text; this does not affect the originality failure because coverage is already mechanically implied by the classical rook-graph theorem and the elementary maximality argument.

## Disposition

**failed**
