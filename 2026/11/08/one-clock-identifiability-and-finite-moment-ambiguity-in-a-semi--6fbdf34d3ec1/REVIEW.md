# Scientific review

## Correctness — PASS

The exact release-start perpetuity, Gaussian variance mixture, and renewal-reward age integration give Eqs. (1)–(2) in RESULT.md. They are triangular in two different orders: known release moments give each confinement Laplace moment, while known confinement moments plus the release mean give each successive release power moment. The compact Hausdorff moment problem makes the first inversion injective; the specified moment-determinacy assumption makes the second injective. An explicit nonzero kernel in a matrix with one extra column proves matched-mean ambiguity for every finite depth. A Chebyshev zero-count argument gives the matching sharp support lower bound of \(K+3\) distinct durations. Positive finite means and positive durations ensure contraction of the affine recursion and strictly positive denominators. Tests are finite corroboration, not infinite proofs.

## Originality — PASS (qualified)

The closest result is Frydel's 2026 paper (arXiv:2607.05173, DOI:10.1103/7pxv-tg3b), whose Sections VI and VII and Eqs. (52)–(59), (66)–(70) explicitly provide the forward variance-mixture and moment relations. The paper does not state the one-clock global inverse-uniqueness theorem or the same-mean finite-moment aliasing classification, including the sharp minimal number of distinct clock durations. The former follows by a nontrivial reverse triangular argument plus Hausdorff determinacy; the latter uses an independently motivated interpolation kernel and yields an exact physical counterexample. The older 2024 fluctuating-trap model is principally Markovian. A pre-existing broader inverse moment/renewal identifiability result could subsume the inverse theorem; this is a priority risk, not an assertion of proof of uniqueness across the literature.

## Value — PASS

This solves a precise experimental-identification boundary: infinite-resolution phase-conditioned stationary imaging is theoretically identifying when one residence clock is independently calibrated, while finitely many even spatial moments cannot uniformly identify the other clock, even when its mean is separately measured. The constructive inverse recursion and arbitrarily-high-order matched-mean alias families turn forward formulas into a complete structural answer about what stationary observables can and cannot determine. Neither statistical consistency under noise nor an estimator with controlled conditioning is claimed.

## Remaining scientific limitations

The inverse of the released clock needs its mean and determinacy. The theorem does not recover two unknown clocks simultaneously and does not cover finite-noise identification. Classical moment determinacy and the forward trap equations are prior mathematics. One broader, presently unlocated inverse-theorem implication remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
