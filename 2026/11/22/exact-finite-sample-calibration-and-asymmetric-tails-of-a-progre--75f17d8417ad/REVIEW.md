# Scientific review

## Correctness — PASS
The result is quantified for all fixed integers \(0\le r<m\le n\) with \(m-r\ge2\), a fully exponential null and independent noninformative removals. The argument decomposes the first observed risk-normalized gap into independent scaled exponentials, applies a one-sided partial-fraction survival formula, derives the lower tail from an exact product and the upper tail by a dominated simplex small-ball calculation. The strict stochastic comparison uses an explicit almost-sure coupling. Replayed exact rational checks and separate direct lifetime-censoring simulations passed 413 comparisons. Numerical checks are supplementary, not substitutes for infinite-family proofs.

## Originality — PASS (qualified)
The closest source, Qin–Yu–Gui (2020), defines the same statistic and recognizes difficulty of its exact null distribution, using normal or simulation approximations. Huffer–Lin (2001) already gives a universal recursive algorithm for arbitrary rational linear combinations of independent exponentials, and so the *availability in principle of exact computation is prior art*, not a new assertion. The investigated contribution is instead the specified single-sum rational closed form, paired exact left/right tail exponents and constants, and stochastic dominance against an Irwin–Hall benchmark. The 2025 exact-inference article addresses different location/scale/prediction pivots; 2026 documentation still uses normal/simulation calibration. Direct targeted research-index, prior-ledger, and literature searches did not show the exact same analytic package. Generic-algorithm derivability and incomplete historical indexing remain specific originality risks; no independent priority certification is claimed.

## Value — PASS
The observation is substantive for the originally published test: its CDF can be evaluated exactly at finite sample sizes, while the disparity in censoring-induced tail powers explains how two-sided extreme significance thresholds differ. This is a structural calibration result for a natural published statistic rather than an arbitrary model slice, code exercise or restatement of the generic exponential-spacing representation.

## Limitations and closest literature
The original 2020 paper and the broader 2001 Huffer–Lin computational method are the closest references, followed by the 2025 exact-inference article. No claim is made beyond the exponential null and noninformative removals. Floating-point cancellation in the signed partial fractions requires rational or high-precision evaluation for extreme tail quantiles. A domain expert should independently check priority and the interpretation of general-algorithm coverage.

Self-review: passed. Independent audit: not yet performed.
