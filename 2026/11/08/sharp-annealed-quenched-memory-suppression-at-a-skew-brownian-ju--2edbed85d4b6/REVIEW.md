# Scientific assessment

## Correctness: PASS

The transition kernel explicitly accounts for the mass on both sides of the skew point. The proof derives the one-time survival probability from this kernel and the two variance conventions from independent Bernoulli indicators. The strict-convexity conclusion is valid because the reflected Gaussian image integral has nonzero spatial variance for every finite time. The derivative-at-the-boundary argument rules out a zero gap at any admissible bias. The short-time argument isolates the two disjoint Gaussian boundary layers; the long-time argument expands the Gaussian kernel uniformly in the compact parameter range and computes a rational variance polynomial. Finite tests in `verify.py` check this derivation without replacing the analytical argument.

## Originality: PASS, with risk

Biswas et al., arXiv:2404.13988, Eq. (13), (21) and Sections III.1–III.2, already supply the general variance decomposition and the reflecting/open endpoint examples. These are expressly not claimed as new. The paper and its Appendix A were inspected: their discussion of asymptotic equality of variances has leading \(t^{-1/2}\) order, but the text does not derive the optimized continuous-skew family, its strictly positive exact gap, the sharp \(t^{-3}\) coefficient \((61\beta^2+2\beta+1)/11520\), or the reversal of optimum. Lejay and Gairat–Shcherbakov give classical skew Brownian transition densities; the coefficient is not implied as a stated corollary without applying the separate counting variance framework and a new asymptotic optimization. Bressloff, arXiv:2211.12460, studies local-time semipermeability with a physical permeability parameter, which is a different stochastic interface. Search coverage is incomplete, and an unindexed mathematical-physics extension could include the result. Originality therefore remains self-review, not independently established.

## Mathematical value: PASS

The variance difference quantifies how much of the observed counting noise arises from uncertainty over *initial particle positions*, rather than Brownian trajectory randomness. It is natural to ask which local junction bias hides that initial-condition memory most effectively. The resulting bias has a nontrivial time-dependent reversal; the exact \(t^{-3}\) law refines previously known convergence of variances, and the 64-fold endpoint contrast provides an interpretable benchmark. The result is for a concrete continuous physical parameter family, not an arbitrary finite parameter slice.

## Risks and limitations

The skew point is scale-invariant; a physical membrane with a finite permeability requires a different model. The counting observable is current occupancy outside the initial interval, not irreversible first-passage losses. Finite-particle independence and uniform initial positions are essential. Only at least one reversal is proved, not a unique crossing or monotonicity. Numerical tests are reproducibility diagnostics, not infinite-time certificates. A complete independent literature-priority assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
