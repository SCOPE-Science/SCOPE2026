# Scientific review

## Correctness (PASS)

The inverse problem is reduced exactly by the linear flux equation to a scalar cosine equation. For any fixed nonzero coupling, the residual target function and its derivative vanish at infinity at rates \(O(x^{-1})\) and \(O(x^{-2})\); hence each sufficiently high flux cell contains exactly one simple inverse. The proof separately treats the possibility of near-zero accumulation, establishes the precise linear cell count, and obtains the lattice correction by a local sine expansion. The Jacobian equals the reduced scalar derivative times \(-k_2\), and the zero-coupling endpoint is a strictly unimodal exponential term. The symbolic check and 558 numerical large-cell examples corroborate—but cannot replace—the analytic argument. Nonstandard calculations are explicitly reconstructed in RESULT.md.

## Originality (PASS, provisional historical assessment)

Kumar and Chandramouli, arXiv:2605.00442v1, give the exact neuron map and investigate local fixed points, bifurcations, coexistence of attractors, and networks; the inspected full-text material does not provide the all-target inverse-valence and density theorem. Han et al. (2022), doi:10.3389/fphy.2022.911144, investigate a different cosine memristor map. Broader theories of infinite-degree cosine functions and of noninvertible maps do not automatically imply the present restricted-positive-input, real two-dimensional formula with exact linear inverse density and a zero-coupling discontinuity. Actual bibliographic and mathematical-record searches found no direct covering statement. Absence from those searches is not a uniqueness certificate; additional historical papers may exist.

## Value (PASS)

Inverse multiplicity controls backward branching and distinguishes proper finite-to-one and surjective infinite-to-one dynamics. The natural physical question is whether adding a very weak cosine memristor term merely perturbs the reduced Chialvo map or changes its global geometry. The theorem supplies an exact, discontinuous qualitative answer, shows every remote branch is regular, and identifies a parameter-independent asymptotic inverse density. It simultaneously warns against extrapolating bounded-neuron simulations to arbitrary states. This is a structural global result, not a parameter substitution or a sampled table.

## Closest literature and limits

Primary arXiv:2605.00442v1; a different 2022 two-dimensional memristor cosine map; general theory of noninvertible maps. The analytic theorem is not a statement about bounded attractor geometry or positive forward invariance. The historical-priority conclusion remains provisional and is not independent scholarly certification.

Self-review: passed. Independent audit: not yet performed.
