# Self-review

## Correctness — PASS

The domain is the complex Schur multiplier of the rectangular incidence matrix obtained by deleting one line row but keeping all point columns in \(\mathrm{PG}(2,q)\), \(q\) a prime power. The proof explicitly checks the weighted trace-dual reduction, affine-collineation orbits, three eigenspace multiplicities, strict concavity, and the sign of the uniform-weight first variation. An expansion of the critical equation produces the exact weight and norm asymptotics, including the two different gap exponents. Finite-field spectral checks support but do not replace the proof.

## Originality — PASS, qualified

Levene (arXiv:2611.08419v1) supplies the existing duality and concavity tools, but its inspected main results concern trees on symmetric cores and do not calculate this punctured projective family. Davidson–Donsig (arXiv:math/0506073) gives symmetry-based Schur multiplier computations for other patterns; its inspected material does not imply the exact formula or rigidity here. Earlier full-incidence design results concern a square balanced matrix with a uniform optimizer, unlike the present rectangular, orbit-asymmetric mask. Related published Schur examples based on complete bipartite graphs, stars or Walsh–Hadamard sign defects have different support and do not imply the stated coefficients. Search incompleteness, especially older unindexed graph-specific formulas, remains a live limitation.

## Mathematical value — PASS

Deleting just one line destroys the complete-design symmetry and changes the norming distribution. An exact parameter-free characterization over every prime-power order quantifies both the full-mask norm loss and the subtler gain from reoptimizing column weights. The theorem identifies a natural family invariant and a structural rigidity statement, not merely another algebraic expression for a known constant.

## Limits and evidence

The claim does not classify every maximizing weight individually, does not assert the result for non-Desarguesian planes, and does not use finite experiments as proof. The standalone numerical checker compares sixteen weighted Gram spectra against direct finite-field matrices, tests the critical equation and probes large-order asymptotic laws. No independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
