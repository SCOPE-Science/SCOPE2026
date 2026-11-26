# Independent mathematical audit

## correctness

PASS

Uniform marginals force the diagonal masses u/2 and off-diagonal masses (1−u)/2. The four affine multipliers are 79,37,97,91 divided by 100. Bounded offsets and products bounded by (97/100)^k make the stationary backward affine series converge absolutely. A common fresh pair sequence contracts discrepancies and yields second-moment convergence for finite-second-moment initializations. The moment equations use freshness and give the stated mean and risk about zero. Reviewer-authored `python3 /workspace/independent_reproduction.py affine` (SymPy 1.14.0) reconstructed the maps, rational risk and three comparison values; its critical points were about 0.718624522 and 2.078872634. The derivative has sign opposite to the stated strictly decreasing quadratic with endpoint signs + and −, proving exact strict global optimality. Smooth dependence retains the endpoint signs under small perturbations. With equal slopes, centering at the mean root gives contraction 1−t+t² and centered noise td(S_J−tS_I) with E[S_IS_J]=2u−1. Its variance and hence risk decrease strictly in u for 0<t<1 and distinct roots; coincident roots tie. These are fixed IID stationary-risk conclusions, not adaptive or root-convergence claims.

## originality

PASS

Optimization over within-step uniform-marginal couplings is already present for homogeneous bilinear stochastic extragradient, and stagewise noise-coupling optimization appears for a different noisy two-step algorithm. Credit those precedents. The supported distinct result is an interior minimizer of genuine nonzero stationary affine root risk for strongly monotone components, with a contrasting equal-slope boundary and persistence under perturbation.

## value

PASS

A strict interior risk optimum rules out the common design shortcut of considering only reuse, independence or maximal antithetic pairing, even with scalar strong monotonicity and contraction under every pair. The nonzero stationary bias at the optimum, the equal-slope obstruction, and a perturbation-stable example establish a meaningful boundary of the heuristic; the contribution does not need a universal nonlinear classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
