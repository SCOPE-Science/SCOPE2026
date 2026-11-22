# Review of the Gaussian coupling threshold

## Correctness — PASS

For a real scalar bilinear game, the exact two-step recurrence has scalar deterministic multiplier \(1-r^2\) and innovation \(h(\xi_1-(I+rS)\xi_0)\), where \(r=h\sigma\), \(S^2=I\), and \(0<r<\sqrt2\). An independent-pair geometric sum reduces the finite-horizon and invariant second moments to minimizing the one-pair innovation. In the two eigenvectors of \(S\), each marginal coordinate has variance \(v\); Cauchy–Schwarz gives the attainable lower bounds \(v(|1+r|-1)^2\) and \(v(|1-r|-1)^2\). Equality is unique away from \(r=1\) and is achieved by identical noise or coordinate-swapped noise on the respective sides. All stationary formulas and asymptotics follow algebraically. `verify.py` supplies 5,676 exact-rational comparisons over 129 admissible step pairs and five exact witnesses. Finite checks support, rather than replace, the proof for real parameters.

## Originality — PASS, with residual priority risk

Shugart and Altschuler, *Negative Stepsizes Make Gradient-Descent-Ascent Converge*, arXiv:2505.01423, §§1.2, 3.1 and 6 and Appendix A, give the deterministic alternating schedule and discuss open stochastic-robustness issues; these inspected parts do not provide the fixed-Gaussian-marginal coupling optimizer or its sharp threshold. Gorbunov et al., arXiv:2111.08611, compare stochastic extragradient sampling rules; Vlatakis-Gkaragkounis et al., arXiv:2306.16502, treat stochastic dynamical limits. Neither constitutes a covering theorem for paired signed GDA. Published results on optimal noise coupling in normal extragradient and on sample coupling of stochastic bilinear extragradient are mathematically adjacent, but have different iteration matrices, conditions and stochastic models. The fundamental covariance-alignment inequality itself is classical, and is expressly not claimed as new. Targeted source and mathematical-record searches found no equivalent explicit phase diagram, but publication priority is not thereby proved.

## Value — PASS

The motivating work explicitly raises the robustness of paired negative steps to stochastic gradients. The exact result isolates an operationally meaningful failure mode of independent observations: a nonzero stationary error floor persists as the learning rate vanishes. It also identifies a sharp point at which reusing the same noise ceases to be optimal even within the fixed-marginal correlated-oracle model. This is a finite-dimensional benchmark with clearly stated oracle-information limits, not a claim that standard conditionally unbiased oracles allow such coupling.

## Limitations and additional scrutiny

The result is specific to one scalar bilinear singular mode and isotropic Gaussian marginals with user-controllable dependence. Shared or swapped oracle noise generally violates conditional unbiasedness at the intermediate adaptive evaluation point. Mathematical-record summaries cannot guarantee exhaustive literature coverage. No independent mathematical review has been conducted.

Self-review: passed. Independent audit: not yet performed.
