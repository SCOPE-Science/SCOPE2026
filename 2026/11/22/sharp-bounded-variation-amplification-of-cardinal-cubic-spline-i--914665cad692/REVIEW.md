# Self-review

## Correctness — PASS

The result is reconstructed from the cardinal cubic spline tridiagonal second-derivative recurrence with its exact bilateral Green kernel. The unit-step second-derivative solution, positivity of the center-cell derivative, two symmetric alternating-sign tails and exact cubic peak height yield the stated constant. Every BV nodal sequence decomposes into a summable series of translated steps, providing the general upper bound and a single-step attaining witness. The accompanying standard-library checker validates identities and finite reproducibility checks; the infinite result is justified by the proof, not computation.

## Originality — PASS, subject to historical-priority risk

Percan–Zellmann–Lang (online 2014, DOI 10.1007/s11075-014-9941-x) provide the matching cubic B-spline prefilter, but study asymptotic reconstruction error. Zhang–Martin (1997, DOI 10.1016/S0377-0427(97)00199-4) study step-data cubic Gibbs overshoot with finite complete-spline boundary conditions. Neither inspected result asserts the bilateral all-input sharp BV stability coefficient, its exact radical, or the variation-contributing infinite overshoot sum. Relevant indexed spline findings are about finite 3-knot range defects, linear-spline orthogonal projections and other norms. Unindexed or historically implicit equivalent formulas remain a residual risk; this assessment is not an independent historical priority certification.

## Mathematical value — PASS

Continuous variation is a natural stability benchmark in edge, jump and oscillation-sensitive reconstruction. The exact 1.5891089959... multiplier quantifies how a smooth \(C^2\) interpolant creates oscillation even from monotone nodal data. The unbounded-grid sharp calculation, attained step witness and complete all-input extension distinguish the result from a local overshoot computation or a routine three-knot example. It is useful for auditing cubic prefiltering when BV stability matters, without requiring a downstream theorem.

## Limits

Real unit-spaced bi-infinite cardinal interpolants only; other spline end conditions, meshes and degrees are not addressed. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
