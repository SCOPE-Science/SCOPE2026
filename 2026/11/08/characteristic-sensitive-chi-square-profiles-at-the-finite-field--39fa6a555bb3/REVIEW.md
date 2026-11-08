# Review of the finite-field Wishart mixing statement

## Correctness — PASS

The claim specifies a uniform-vector rank-one walk on the additive group of symmetric matrices over a fixed finite field. Plancherel reduces chi-square to a sum of powered one-step Fourier magnitudes. Odd characteristic requires the symmetric-matrix rank count; even characteristic requires the polar-rank decomposition of homogeneous quadratics and a count of refinements vanishing on their radical. Both multiplicities were derived explicitly and tested by exhaustive enumeration, including the nonprime field of four elements. Dominated Gaussian-binomial asymptotics give the fixed-offset series; the low-rank support test and the spectral chi-square bound establish both sides of the total-variation cutoff. No fixed-offset total-variation limit is asserted. Risks: the proof relies on classical Gauss sums and classical finite-group mass formulas; these are explicitly named and checked in small cases but not independently certified.

## Originality — PASS under bounded source comparison

The exact walk-specific chi-square series and the characteristic-separated fixed-offset profiles were compared with the closest relevant primary sources and semantically related research records. Schmidt's association-scheme eigenmatrices cover much of the required one-step spectral machinery, and Fulman–Goldstein supply classical symmetric-rank counts. Neither inspected statement directly gives the particular unscaled Gram-matrix walk's full time-dependent divergence and both cutoff sides. Pak–Vu treat a scalar-randomized walk with a different holding probability, including in characteristic two for dimensions exceeding one, and do not supply the asserted chi-square profiles in inspected sections. Thus this is a bounded, not absolute, priority conclusion. Residual risk: older implicit eigenmatrix consequences or an unlocated finite-field Wishart mixing theorem could subsume part of the claim.

## Mathematical value — PASS

The comparison is motivated by deciding how many random outer products are needed to make a finite-field sample-covariance matrix indistinguishable from a uniform symmetric matrix. It gives an exact answer for each finite dimension and step count, a sharp mixing threshold at the minimum sample-size scale, and two distinct, explicit boundary-window chi-square laws. It is not merely an enumeration of small cases: the rank-sector dichotomy and the uniform limiting argument are structural and apply to all fixed prime powers.

## Independent status

Self-review: passed. Independent audit: not yet performed.
