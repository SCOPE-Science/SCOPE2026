# Scientific review: rank-one idempotent sum fibers

## Correctness — PASS

The claim is valid for all finite fields and matrix sizes \(n\ge2\). The trace/rank screen is necessary. Rank-one decompositions are partitioned exhaustively into common-image and common-row cases, with exact characteristic-dependent intersection. In rank two there is a bijection between ordered decompositions and rank-one projectors on the image satisfying one scalar equation; the projector count is an exact rational-eigenline count. Zero, rank-one, and rank-two cases cannot overlap. The global sum-rank identity is reconstructed independently by directly counting common image/row relations. Full-domain checks on seven prime-field test cases and one nonprime-field test case agree at every target. They corroborate the proof, not establish the infinite-parameter claim.

## Originality — PASS (provisional historical priority)

The closest inspected archival work is C. de Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field*, arXiv:0907.4436 (2009-07-25), whose Theorems 3–6 and subsequent proof concern **existence** of decompositions by unrestricted idempotents. The full work was checked for rank-one constraints, fiber cardinalities and incidence formulas; it neither states nor directly yields the exact ordered rank-one fiber law. De Seguins Pazzis's arXiv:0907.5360 concerns existence/minimal number of summands; arXiv:1109.2255 concerns another quadratic-sum existence classification. Semantic searches of mathematical research records and web literature found related idempotent decompositions and rank-one geometry, but no equality of claims or stronger stated counting result. The rank-two formula is not a restatement of the general existence theorem. Risk: a general, presently unidentified additive-convolution theorem for rank-one idempotent conjugacy classes could subsume the census. Historical novelty is not independently certified.

## Value — PASS

The result gives a complete, invariant, target-dependent *witness count* for a classical decomposition at the first nontrivial rank budget, in arbitrary ambient dimension and across all finite fields. It reveals a precise projective-line/eigenvalue transition and the exceptional characteristic-two scalar-image obstruction, including nilpotent rank-two targets in dimension four. Its global rank spectrum has a characteristic-independent rank-two count but a characteristic-dependent zero fiber. These are structural distinctions not supplied by the classical existence statements. The theorem is self-contained and not predicated on a downstream conjecture.

## Verification and residual risks

The provided exact-arithmetic programs reproduce all stated finite checks. Odd-prime and binary tests include higher ambient dimensions; an additional GF(4) checker exercises nonprime characteristic-two arithmetic. No computation was extrapolated to all fields. Higher-rank idempotent summands and unspecified convolution formula literature remain outside scope. The source-precedence risk and absence of independent validation remain explicit.

Self-review: passed. Independent audit: not yet performed.
