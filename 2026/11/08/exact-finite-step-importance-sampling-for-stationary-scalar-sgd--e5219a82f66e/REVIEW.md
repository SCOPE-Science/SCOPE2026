# Scientific review: exact finite-step importance sampling for stationary scalar SGD

## Correctness — PASS

The unbiased scalar update yields an exact independent affine recursion. Its second-moment multiplier is \(1-2\eta\bar a+\eta^2 m^{-2}\sum_i a_i^2/p_i\), which determines the sharp finite-variance stability region. The invariant mean-square error is the positive ratio of residual and curvature harmonic sums; the root equation has exactly one positive solution by monotonicity, and Cauchy–Schwarz gives a **global lower bound with uniquely attained equality**. The explicit three-component witness has stationary errors \(1/15\) and \(1/3\). The packaged independent-from-formula rational checker tests finite identities, not the universal proof. Mathematical boundary cases \(\sum_i r_i^2=0\) and \(\eta\ge2/\bar a\) are explicitly separated.

## Originality — PASS, qualified

The closest source is El Hanchi–Stephens (arXiv:2103.12293, sections 1–2), whose optimized quantity is the instantaneous gradient-estimator variance rather than the unaveraged stationary error with state-dependent multiplicative curvature. Its related arXiv:2103.12243 Appendix D contains only experimental fixed-step adaptations. Défossez–Bach (arXiv:1412.0156, section 4) treat averaged LMS and explicitly turn to a small-step limit for optimizing resampling. Liu–Ziyin–Ueda (arXiv:2012.03636, section 4.1) solve a fixed-additive-noise stationary covariance problem but not the state-multiplier sampling optimization. Other related sampling and stochastic-optimization findings were compared by the implications of their claims, not by titles alone. Publication precedence under classical fractional-programming or scalar-random-recurrence terminology remains a residual risk; this self-review is not independent certification.

## Value — PASS

The result gives a natural, exact, computable design benchmark for the standard conflict between noise reduction and mean-square stability when importance weighting changes component curvature. It determines the **entire admissible step-size interval** and the unique optimal probability law, not an arbitrary finite numerical example. The exact example shows a factor-five stationary-risk improvement and the counterintuitive need to sample a zero-gradient component with majority probability. This answers a motivated design question complementary to the instantaneous-variance criterion in importance sampling literature. Implementing it requires unknown problem-specific quantities at the optimum.

Self-review: passed. Independent audit: not yet performed.
