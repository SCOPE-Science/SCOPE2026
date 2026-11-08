# Scientific review

## Correctness — PASS

The claim is proved for the exact family \(F_r(y)=(1-e^{-e^y})^r\), all positive real \(r\), and all interior quantile intervals. The direct derivative identity is valid on that full domain. The integral representation of \(g(t)=-\log(1-t)/t\) establishes strict monotonicity without numerical assumptions. The integrated-quantile characterization then yields centered convex order, and the double-quantile variance identity provides an independent strict-variance proof. The checker supplies separate finite diagnostics only. No extrapolation from computations or asymptotics is made.

## Originality — PASS, qualified

The full text of Mesfioui–Trufin (2021), especially Proposition 4.1 and Section 4, supplies a general sufficient *log-convexity* condition for sample-size dispersive ordering; the present baseline cdf is strictly log-*concave*, so that theorem does not cover this case. Doumas (2022, 2026) develops the coupon-collector variance and its logarithmic exponential representation, and Giam (2026) already proves its strict decrease in the integer parameter. This known variance monotonicity is excluded from the novelty claim. The new assertion is strictly stronger: it orders all quantile widths and all centered convex losses continuously in the parameter. Related published records on other exponential-order-statistic quantities do not imply it.

The abstracts of two particularly plausible comparison papers—Alimohammadi–Esna-Ashari–Cramer (2021) and Giam (2026)—were available but their respective complete texts were not. The former is about increasing-reversed-hazard-rate inputs, whereas the present input has decreasing reversed hazard; the latter explicitly establishes variance monotonicity but its abstract does not assert full quantile contraction. There is consequently a nonzero historical-priority risk, not a proof of uniqueness.

## Value — PASS

Coupon-collector fluctuation coefficients motivated a long-standing monotonicity question, already answered for the second moment in later work. The new strict dispersive comparison controls every fixed-confidence quantile width, a genuinely stronger uncertainty statement unavailable from variance alone; the accompanying centered convex order simultaneously controls the entire family of convex dispersion losses. The continuous parameter result and one monotonic kernel explain the geometry of this classical exponentiated extreme-value family. This is a motivated structural inequality, not a numerical re-evaluation of a known coefficient.

## Limitations and closest literature

The family is highly specific; the theorem does not assert a general ordering for arbitrary distributions, noninteger sample sizes as literal samples, or finite-coupon completion times. Exact historical coverage remains subject to independent full-text review of the inaccessible comparison papers.

Self-review: passed. Independent audit: not yet performed.
