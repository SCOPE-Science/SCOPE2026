# Self-review

## Correctness — PASS

PASS: The monomial projection formula follows from normalized area integrals; direct two-step composition gives a single nonzero anti-diagonal at each monomial degree sum, with only a possible central zero. Polynomial-pencil row reduction isolates a unique top-degree pair, yielding a triangular minor of size r+s−1 (odd sum) or r+s−2 (even sum). The bilinear harmonic pairing makes the finite matrix skew-symmetric after positive diagonal scaling, so the even-sum upper bound matches the minor. The centered Wronskian degree equals r+s−1. The commutator annihilates analytic vectors and maps anti-analytic vectors into analytic polynomials, proving square zero. The direct-composition checker passed 1305 exact-rational cases, independently forming the Wronskian; these are supplemental only.

The proof is an infinite-dimensional operator proof based on finite-dimensional supports for each polynomial pair. Its matrix triangularity and even-rank argument cover all degrees and all complex coefficients. The 1305 exact diagnostics are reproducibility support, not an infinite verification.

## Originality — PASS with qualification

PASS with a bibliographic reservation: Cui–Huang–Lu–Zu (2026), Theorem 2.8, classifies when such commutators are finite rank, and their Corollary 3.1 gives square zero, but the complete polynomial-pair exact rank is not stated. Dong–Zhou treats quasihomogeneous symbols and determines individual monomial ranks, whereas a general two-polynomial pencil includes interacting monomial degrees and potential top-degree cancellation. Chen–Koo–Lee (2013) proves evenness and realization of even ranks according to the accessible abstract, but the full article was unavailable for checking. No searched indexed claim explicitly supplied or logically dominated the new exact formula; absence from an index alone does not establish priority.

The closest literature is Cui–Huang–Lu–Zu (2026), arXiv:2611.08988v1, especially Theorem 2.8 and Corollary 3.1; Dong–Zhou (arXiv:1411.0213v3), Theorem 4.4; and Chen–Koo–Lee (2013), doi:10.1007/s00020-012-2020-6. In particular the monomial rank formula and square-zero property are previously known, whereas the complete centered-Wronskian degree law for arbitrary polynomial pairs is the claimed contribution. The unavailable full 2013 text is an explicit priority risk.

## Mathematical value — PASS

PASS: Finite-rank classification and even-rank realizability leave the actual rank of an arbitrary polynomial pair undetermined. A natural invariant—the centered Wronskian degree—gives a complete exact rank formula, invariant under changes of basis of the polynomial pencil. The law identifies when lower-degree perturbations preserve rank and when cancellation of equal-degree leading terms shifts it, providing a structural classification rather than a single computed example.

## Limits

The analytical claim is for unweighted disk harmonic Bergman space and pairs of analytic polynomials. It neither classifies nonpolynomial rational symbols nor gives singular spectra. Search and source inspection cannot prove universal priority, and one relevant original article remained unavailable in full. Computations are finite diagnostics, not a universal proof.

Self-review: passed. Independent audit: not yet performed.
