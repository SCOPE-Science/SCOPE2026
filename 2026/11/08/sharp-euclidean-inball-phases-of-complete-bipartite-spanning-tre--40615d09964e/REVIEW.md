# Review of sharp Euclidean inball phases of complete-bipartite spanning-tree polytopes

## Correctness

PASS. The statement applies to the intrinsic Euclidean metric on the affine span of the canonical edge-indicator spanning-tree polytope, for integer \(2\le p\le q\). The proof invokes Edmonds' complete rank inequalities (not a conjectural facet enumeration), calculates the projected normal of every allowed rank subset, and proves a global minimum over all integer pairs of subset cardinalities. The two-case inequality for \(2\le r<p\) and the exceptional \(r=s=1\) calculation are crucial: merely inspecting high-symmetry degree constraints would not establish the theorem. The center-locus dimensions follow by active-constraint ranks and strict slack for all other inequalities. The outer radius follows from the constant Hamming weight of all vertices. Exact rational and numerical LP spot checks are recorded in `VERIFICATION.md`; no finite test substitutes for the general proof.

## Originality

PASS under available-source evidence, with historical-priority limitations. Edmonds' inequality description is explicitly credited and not claimed new. The inspected open-access 2021 paper on spanning-tree polytope extension complexity (arXiv:2106.11945; definition, complete inequality description, proofs and communication protocols) does not state these Euclidean inball values, a scalar crossover, or optimal-center dimensions. The inspected 2021 paper by Dong and Ge (arXiv:2103.05294; abstract, introduction and main counting theorem) instead counts spanning trees containing prescribed forests. A previously published result for the same biclique spanning-tree polytope determines Minkowski asymmetry, a different affine-invariant question; its summary does not entail the Euclidean distances or their competition. An equivalent earlier Chebyshev-center formulation may exist in polyhedral-optimization literature. Lack of a match in searches is not treated as a proof of global novelty.

## Mathematical value

PASS. The full family of graphic-matroid base polytopes of complete bipartite graphs is natural and has exponentially many rank constraints, so locating the smallest Euclidean distance to *any* constraint is not automatic. The theorem proves that just two graphically meaningful types control all nontrivial cases, identifies exceptional low dimensions, and classifies the entire locus of optimal ball centers. The dimension changes from zero to a positive order-\(pq\) number across a sharp metric transition. The asymptotic scaling boundary \(q\asymp p^{3/2}\) is a structural distinction between balanced and elongated bipartitions, not a numerical table or arbitrary slice.

## Closest literature and limitations

Principal sources are Edmonds (1971), Aprile–Fiorini–Huynh–Joret–Wood (arXiv:2106.11945; v1 June 22, 2021), and Dong–Ge (arXiv:2103.05294; v1 March 9, 2021). The contemporary published Minkowski-asymmetry result on complete-bipartite spanning-tree polytopes has the same vertex model but controls containment under reflection and translation rather than the intrinsic Euclidean norm. Its original complete text was not available for this comparison, which remains an originality risk. The proof addresses only the canonical unweighted edge-indicator embedding and does not provide a weighted-graph counterpart. The critical asymptotic scaling constant itself is not classified in finite dimensions.

Self-review: passed. Independent audit: not yet performed.
