# Scientific review

## Correctness
PASS. The exact Rayleigh-to-Dirichlet normalization gives a marginal density with linear vanishing at zero and bounded two-coordinate density. A direct small-argument expansion of the empirical discrepancy, a one-large-coordinate tail lemma and a Laplace asymptotic establish the three pieces of the stated theorem for every fixed integer sample size at least two. The off-diagonal expectation estimate uses integrable inverse-coordinate products, explicitly treating the exceptional two-coordinate simplex separately. The attached checker independently reproduces 25 finite numerical comparisons for the two-sample case. Those checks corroborate but do not substitute for the proof.

## Originality
PASS on the compared sources, subject to historical-priority risk. The principal 2022 paper defines the statistic and studies its large-sample law at fixed bandwidth, whereas this result holds sample size fixed and changes the bandwidth. The 2018 distributional fixed-point framework and the related Gamma and Gaussian tests do not give the displayed Rayleigh endpoint tail or logarithmic mean coefficient. Nearby published research records involving inverse-Rayleigh tails concern distinct models, and available prior findings on heavy-tail goodness-of-fit statistics concern different statistics. Absence in these sources is not a proof of global uniqueness; a broader older Tauberian or singular-discrepancy theorem could subsume a component, although the exact normalized-Rayleigh coefficients still require model-specific verification.

## Value
PASS. Tuning sensitivity matters for the finite-sample calibration of weighted goodness-of-fit tests. The theorem shows an unexpected conflict: almost-sure normalization yields a finite random limit, but the same normalization gives a divergent expectation with a sharp coefficient. The limiting variable has exactly the critical \(z^{-1}\) tail, quantifying the rare-event mechanism and warning against using a naive moment calibration at large tuning parameter. The result is not a power-optimality claim.

## Limitations and sources
The result is strictly fixed-sample and concerns the maximum-likelihood scale fit. The primary paper is Grobler–Bothma–Allison (2022), https://www.mdpi.com/2227-7390/10/8/1316 , Sections 2–4; the closest broader framework is Betsch–Ebner (2018), https://arxiv.org/abs/1810.06226 , particularly its application section. The Gamma and Gaussian characterization-based tests provide further context. Wider historical priority requires independent verification.

Self-review: passed. Independent audit: not yet performed.
