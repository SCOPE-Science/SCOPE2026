# Scientific review

## Correctness — PASS
The proof exactly characterizes positive moment feasibility as the membership of \((0,\tau)\) in the polygon spanned by sampled parabola points, yielding two opposite-sign extremal products. Exact joint extreme-pair densities give an identity for every finite sample size. Local Laplace analysis at two corners and one interior saddle gives both constants, exponential bases, and the critical \(\alpha=\sqrt2\) crossover. The standalone checker confirms separately computed exact-rational witness equivalences, probability decompositions, finite \(m=3,4\) formulas, and representative sharp asymptotics. Numerical checks are supporting tests, not substitutes for the proof.

## Originality — PASS, with residual historical-priority risk
The two inspected recent primary papers on randomized quadrature and positive exact weights prove general constructive high-probability guarantees, but do not give the exact success probability or the two competing sharp failure equivalents for fixed uniform sampling and varying symmetric Jacobi targets. General random-convex-hull coverage in arXiv:2101.04250 and polynomial cubature sample-complexity coverage in arXiv:2210.05787 supply the formulation and existence bounds but not the explicit Jacobi phase-transition calculation. Earlier sampled-node quadrature work, along with indexed findings on degree-one least-squares weight positivity and random spherical affine quadrature, covers different estimators, moments, or sampling laws; none of these statements implies the explicit quadratic moment-convex-hull probability. Primary-source inspection was possible, and several exact mathematical-alias queries were compared, although not all older scattered literature can be ruled out.

## Mathematical value — PASS
Positive quadrature with random prescribed nodes is a motivated numerical integration problem. Exact minimal-size success probabilities and a sharp, parameter-dependent sampling law quantify the sample cost hidden by general high-probability existence theorems. The crossover distinguishes the two naturally separate design failures, with a meaningful change in the leading prefactor and exponent. The result does not claim improved general construction algorithms, arbitrary moment order, or automatic weight conditioning.

## Closest sources and limitations
- Bělík–Narayan–Turnage, arXiv:2609.09506v1 (2026-09-08), full text inspected: constructive randomized least squares and positive quadrature existence under sufficient conditions; not the explicit uniform random quadratic Jacobi probability law.
- Neumayer–Schäfer–Ullrich, arXiv:2610.32699v1 (2026-10-23), full text inspected: a high-probability general Lewis-density-based positive quadrature theorem; the exact two-mechanism sampling law is not derived.
- Hayakawa–Lyons–Oberhauser, arXiv:2101.04250v1 (2021-01-12), main results inspected: generic convex-hull probability bounds, not an exact parabola-specific law. Hayakawa–Oberhauser–Lyons, arXiv:2210.05787v1 (2022-10-11): polynomial hypercontractivity and cubature sample complexity rather than the two sharp event equivalents.
- van den Bos–Sanderse–Bierbooms–van Bussel, arXiv:1809.09842 (2018): accessible paper introduction and construction description inspected; algorithmic positive quadrature, with full-document comparison still a priority risk.
- Residual priority risk: equivalent calculations may exist in literature on random moment-curve polytopes or interpolatory quadrature; index searches and the two full-text comparisons do not establish absolute priority.
- Scope: iid uniform nodes, symmetric Jacobi targets, degree at most two, exact arithmetic, fixed target parameter in the asymptotics. A method for selecting all weights and their stability is not analyzed.

Self-review: passed. Independent audit: not yet performed.
