# Scientific review: exact antithetic-stratified variance laws

## Correctness

**PASS.** The exact variance is a sum of independent panel variances scaled by \(n^{-2\beta-2}\). Symmetric Taylor expansion about each panel midpoint gives the large-cell coefficient \(\beta^2(\beta-1)^2/720\) and a summably controlled remainder. Integral/power-series comparison establishes the three regimes, including \((\log n)/(1280n^5)\) at the critical exponent. Unbounded power moments explain the infinite-variance boundary. The comparator follows from the ordinary first-order midpoint expansion; rearrangement gives the sharp within-panel coupling inequality. Uniform \(C^2\) Taylor remainders prove the curvature-energy limit. Exact polynomial identities and 552 verifier assertions independently check finite instances. The proof explicitly establishes the infinite limits without inferring them from experiments.

## Originality

**PASS, with qualification.** Yue Wu (2020; arXiv:2011.15086) introduced exactly this randomized complementary trapezoid and published numerical rates for powers \(5/4,3/2,7/4\). The algorithm, these experimental exponents, general Sobolev error bounds and the generic smooth rate are not claimed new. Owen (2008; arXiv:0811.0528) covers antithetic sampling and the smooth root-mean-square \(n^{-5/2}\) rate. The compared texts did not state the full exact finite-panel power variance, the three-regime sharp constants (notably the critical logarithmic coefficient), the equal-budget independent-pair phase boundary, or their joint classification. Relevant public Romberg results concern deterministic extrapolation rather than antithetic randomization. These comparisons are not a uniqueness proof; broader specialist priority is unresolved.

## Value

**PASS.** The critical exponent \(3/2\), including its exact logarithmic law, determines when a singularity prevents the usual curvature-energy saturation; the independent-pair comparator has a distinct critical exponent \(1/2\) at equal evaluation budget. This matters for benchmark construction and understanding when a randomized quadrature rule gains rather than loses its variance advantage. It also supplies exact finite-sample polynomial checks and a canonical optimal within-panel coupling. The precise constants quantify an experimentally studied but previously only numerically indicated transition.

## Closest literature and limitations

Wu, *A randomised trapezoidal quadrature* (arXiv:2011.15086; 2020) and Owen, *Local antithetic sampling with scrambled nets* (arXiv:0811.0528; 2008), are most directly related. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals* (arXiv:2309.09059; 2023), addresses stratified sampling under function-class confidence goals. The theory here is limited to one-dimensional independent equal panels and, for singular asymptotics, pure powers. Arbitrary couplings among panels, nonuniform allocations and finite-sample tail guarantees are not classified. Historical independent expert confirmation remains pending.

Self-review: passed. Independent audit: not yet performed.
