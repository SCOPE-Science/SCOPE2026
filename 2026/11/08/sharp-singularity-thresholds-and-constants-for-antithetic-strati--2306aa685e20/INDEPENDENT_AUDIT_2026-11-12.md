# Independent mathematical audit

## correctness

PASS

Unbiasedness uses uniform marginals, and inter-panel independence yields n^(-2beta-2) times the sum of exact nonnegative within-panel variances. For beta>-1/2, a centered midpoint Taylor expansion gives v_k = beta^2(beta-1)^2 (k+1/2)^(2beta-4)/720 + O((k+1/2)^(2beta-6)), where Var((U-1/2)^2)=1/180. Summation proves convergent series for beta<3/2, (log n)/(1280n^5) at beta=3/2, and beta^2(beta-1)^2/[720(2beta-3)] n^-5 above it, excluding the identically zero beta=0,1. The first panel gives infinite second moment for -1<beta<=-1/2. Independent-point comparator has first-derivative coefficient beta^2/12 and crossover beta=1/2. Strict countermonotone rearrangement proves optimal within independent two-uniform-marginal equal-weight panel couplings, not across panels. Uniform C^2 Taylor error gives curvature integral /720. Source verify.py checks exact beta=0,1,2,3 finite-n identities plus deterministic sampled large-cell coefficients; these do not prove all-beta limits.

## originality

PASS

PASS best-of-knowledge for the SHARP power-family variance identities and constants, not for the antithetic quadrature algorithm, critical test exponents, or generic smooth n^-5 rate. Yue Wu (2020 preprint; 2021 published) defines the same randomized complementary rule and numerically studies beta=5/4,3/2,7/4; its general fractional Sobolev error bounds and numerical exponents do not explicitly state the exact log-critical coefficient 1/1280, the full beta phase diagram, or the independent-pair equal-budget comparison. Other sibling cusp work studies a different centered |x-1/2|^gamma integrand and distributional phase transition. A stronger unlocated quadrature asymptotic theorem remains a named residual risk.

## value

PASS

The exact singularity threshold beta=3/2 (versus beta=1/2 for independent stratified points), nontrivial logarithmic critical constant, smooth curvature-energy saturation, and exact equal-budget comparison give a motivated sharp quantitative numerical-analysis classification, including finite/infinite variance boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
