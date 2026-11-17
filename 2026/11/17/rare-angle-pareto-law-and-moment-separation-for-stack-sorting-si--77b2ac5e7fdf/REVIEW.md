# Scientific review: rare-angle law for stack-sorting simplices

## Correctness

**PASS.** The published orbit description supplies the permutation vertices. Independently, direct stack sorting gives \(e+d_k\), and the explicit orthogonality \(d_j\cdot d_k=0\) when \(j\ne k\) determines the facet normals. A telescoping sum gives their exact angular cosines without a numerical approximation. The probabilistic statement follows from a uniform exceptional index and the continuous-mapping theorem away from a zero-probability endpoint. Uniform harmonic comparison and a square-summable majorant establish both moment asymptotics. The finite checker reconstructs the source orbit and normals separately. The Euclidean realization and all dimensions are explicit.

## Originality

**PASS under best-knowledge source comparison; priority provisional.** The 2023 original paper provides the orbit and simplex and the 2025 follow-up provides Euclidean volume and altitude geometry. Those premises are prior work. Inspection of their geometric sections does not identify the precise ridge-angle multiset or conditional Pareto limit. Searches of published-finding corpus for the object, the finite-angle formulas, equivalent orthogonal-corner descriptions, and the Pareto/moment law revealed generic solid-angle results for other right simplices, not the same claim. The angle computation uses elementary normals, so there is a residual risk of an equivalent observation in unindexed geometry literature.

## Mathematical value

**PASS.** A natural finite family arising from stack sorting has an exact metric ridge invariant that sharply distinguishes almost-all right angles from \(n-1\) exceptional acute ones. The uniform-ridge and conditional-ridge laws have different scales, and a heavy-tailed Pareto limit coexists with a rare-event-dominated variance coefficient. This is more informative than the already-known simplex, volume, or edge-length data and makes an exact, reusable reference distribution for geometric sampling of those polytopes. No claim of general method novelty or downstream theorem is required.

## Closest literature and limitations

The initial stack-sorting simplex construction and its explicit orbit are attributed to Lee--Mitchell--Vindas-Meléndez (arXiv:2308.16457). The later Euclidean-volume formula is attributed to Ake--Lewis--Louie--Vindas-Meléndez (arXiv:2508.00219). Orthogonal-simplex vertex *solid angles* concern a different angular observable. The proof concerns the canonical ambient Euclidean embedding and uniform unoriented ridges only. Incomplete historical indexing leaves priority uncertainty; external independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
