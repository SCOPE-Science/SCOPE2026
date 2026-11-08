# Self-review

## Correctness — PASS

For a real \(2\times2\) positive-definite quadratic and independent isotropic directions, the rank-one whitened projection formula follows exactly from directional line minimization. The two diagonal second moments close under reflection symmetry, with all three entries computed by differentiation of a verified angular integral. The characteristic trace and determinant are rational in \(t=\sqrt\kappa\); the strictly positive transfer matrix has a simple Perron root reached with positive coefficient from every nonzero deterministic starting point. The explicit strict improvement and high-contrast coefficient follow by algebra and Taylor expansion. `verify.py` checks the formulas and representative exact arithmetic; it is not used as a substitute for the infinite proof.

## Originality — PASS, with specialist precedence risk

The most pertinent earlier result is Gower and Richtárik, arXiv:1506.03296, Appendix B: it gives the normalized Gaussian projection's **first moment** in two dimensions. Section 4.4 proves the iterated one-step upper bound on the expected squared error. Neither that first moment nor the generic bound implies an exact closed formula for \(\mathbb E[f(x_n)]\) and its sharp Perron factor without the additional fourth-projection-moment computation and covariance recurrence. Gower et al., arXiv:1905.10874, supply the underlying Gaussian subspace Newton method and general linear convergence theorem, not the exact planar law. Stich et al., arXiv:1111.0194, discuss the equivalent random pursuit method and general convergence. A Gaussian regularized subspace Newton variant, arXiv:2209.04170, uses a different update. No exact equivalent or stronger direct claim was identified in the inspected primary full-text materials or literature comparisons. This is not proof of absolute uniqueness; other planar random-product literature could conceivably cover it.

## Value — PASS

The exact long-run objective rate is a natural benchmark for the independently resampled, rank-one Gaussian Newton/sketch-and-project method. Unlike a one-step estimate, it measures the feedback from the distribution of error directions over many iterations, and its leading high-anisotropy contraction coefficient is \(3/2\) rather than \(1\). This is a mathematically motivated exact characterization, not a selected numerical curiosity or a recomputation of the earlier first-moment projection identity. The result is strictly limited to the explicit planar model, and does not assert a new general complexity theorem.

## Residual limitations

Only independent uniform (or isotropic Gaussian) directions, exact line minimization, real SPD order-two Hessians and expected objective are covered. No claim is made for almost-sure decay, higher dimensions, approximate line search or nonlinear objectives. Prior work remains a specialist-precedence risk despite the inspected primary sources and implication comparisons.

Self-review: passed. Independent audit: not yet performed.
