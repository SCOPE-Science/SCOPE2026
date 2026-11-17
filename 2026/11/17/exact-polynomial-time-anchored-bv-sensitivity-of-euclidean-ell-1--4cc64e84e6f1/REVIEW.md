# Self-review

## Correctness — PASS
The proof uses the signed threshold formula, explicit strict chamber realizations, an exact linear isometry between anchored path variation and coordinate \(\ell_1\), and an integer dynamic-programming invariant. Integrating affine derivatives proves the global sharp coefficient, and local finite-pair witnesses prove attainment. A balanced alternating active support yields \(n-O(1/n)\) lower amplification; Hilbert nonexpansivity and the exact difference-matrix norm give the upper bound. The standalone exact-rational checker verifies dimensions 2 through 15 and finite chambers, but these finite computations do not prove statements in unbounded dimension.

## Originality — PASS, with priority qualification
Duchi and collaborators establish Euclidean \(\ell_1\)-ball soft-threshold projection, not the stated path-BV norm. Three closely related published projection results were compared by full claim and proof; their coordinate \(\ell_p\) or \(\ell_1\)-metric stability conclusions do not imply the signed, ordered anchored-BV maximum. Historical own-claim IDs were compared only for deduplication. The exact algorithm and near-dimension amplification were not found in queried published-finding corpus records or inspected primary literature. Unindexed historical work and unexamined portions of a PDF remain priority risks; a search failure is not uniqueness proof.

## Mathematical value — PASS
The finding quantifies failure of structured perturbation stability for a canonical sparse projection: the sharp coefficient is already 3 in dimension 3 and grows at least \(n-4/n\). Computing the exact all-dimensional invariant through a polynomial signed-support dynamic program is a useful alternative to exponential face enumeration. The result is not merely a thresholding formula or a normalization check.

## Scope and evidence limitations
The norm is anchored to remove the constant-direction degeneracy; it is not the unanchored BV seminorm. The exact all-dimensional coefficient is algorithmic, not a closed formula. The upper leading constant may be improved, and neither weighted nor periodic variants are proved. Independent audit and comprehensive historical priority verification are outstanding.

Self-review: passed. Independent audit: not yet performed.
