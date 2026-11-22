# Scientific review: conditional stabilization-time bottleneck

## Correctness — PASS

The conditional absorption-time transform is the top-right cofactor of the killed birth–death resolvent. The tridiagonal determinant recurrence gives the two explicit rate-ratio polynomials. Their derivative numerator has coefficients of one sign through degree \(m-4\), one zero coefficient, and the opposite sign thereafter, proving exactly one positive critical point for every threshold \(m\ge4\), with the two smaller thresholds classified separately. Reciprocal symmetry puts the optimum below balanced rates. Exact derivatives at rate ratio one, a uniform third-derivative bound from the explicit tridiagonal eigenvalues, and Taylor expansion prove the constants \(15\) and \(5/8\). The standalone code checks independent rational first-passage systems and finite polynomial identities. Risk: no computational test replaces the stated all-size algebra or uniform spectral estimate.

## Originality — PASS, with priority risk

Wu's 2026 initiating paper gives the constant-ratio success probability and the conditioned backward equation, and its Figure 3 visibly illustrates a peak near equal rates. Nonmonotonicity as such is not new. Ashcroft–Traulsen–Galla's 2015 full-text spectral construction is more general than the distributional starting point here; it does not itself assert the exact minimum threshold, a unique maximum for every threshold, or the sharp location/gain constants. The present content is the global all-threshold sign theorem plus \(m^2(1-\rho_m)\to15\) and peak gain \(5/(8\lambda)\), not a new spectral representation. The older 1984 conditional-passage paper was available only in abstract; an implicit derivation elsewhere remains possible. Absence from a search is not proof of priority.

## Value — PASS

The exact smallest cluster size allowing a dissociation-induced delay, the absence of multiple peaks, and the sharp large-size position of the delay maximum directly sharpen the model's rate-identification discussion. They separate an outcome-selection artifact from a genuine increase in stable-capture yield and quantify how near-neutral the bottleneck becomes for large thresholds. This is a motivated complete classification for the baseline bond-kinetic model, rather than a parameter substitution or a numerical reproduction of the published figure. Scope excludes state-dependent rates and physical spatial coupling.

Self-review: passed. Independent audit: not yet performed.
