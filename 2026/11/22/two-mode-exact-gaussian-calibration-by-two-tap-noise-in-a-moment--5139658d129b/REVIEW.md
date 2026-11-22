# Self-review

## Correctness (PASS)

Schur/Jury conditions hold for \(0<\eta,t<1\). Stationary Yule–Walker equations give normalized variance (sigma²/alpha)(A+Bt)/D_eta(t); the mode-wise Gaussian law is unique. The interpolating line through two distinct modes is K+Gt. Real-tap realizability reduces to -1<=G/K<=1+2eta and both inequalities hold strictly by explicit positive factorizations. The difference has exact factor eta(1+2eta)(t-t_-)(t-t_+), proving sign and excluding three distinct zeros. The necessary independent 3x3 Lyapunov solve, interpolation and rational example were reproduced with 1679 exact checks by embedded verify.py. Finite tests supplement, do not prove, the arbitrary-dimensional statement.

The claim assumes a real symmetric positive-definite quadratic Hessian and the displayed stability interval. The full stationary covariance proof, root-boundary inequalities, feasibility construction and sign factorization can be reconstructed from `RESULT.md`. The rational checker is a supplement to those proofs, not an infinite-domain certificate. The method does not establish exact joint kinetic dynamics or generic nonlinear invariant laws.

## Originality (PASS, qualified)

Direct claim-to-implication comparisons of complete accessible motivating and colored-noise papers, a closely related later stochastic Nesterov article, published-finding corpus semantic records found no statement entailing the arbitrary-real-two-tap positive-momentum two-eigenvalue classification and exact signed bias. The \(\eta=0\) all-mode equality, general ARMA identities, and exact harmonic integrators are explicitly credited. Full repository texts/unindexed ARMA sources remain priority risks; this is a qualified same-model best-knowledge assessment, not independent novelty certification.

The closest inspected literature is Schuh (2026, arXiv:2605.24070), whose exact harmonic splitting is not the stated polynomial two-step update; Leimkuhler–Matthews (2012, arXiv:1203.5428), whose zero-momentum colored-noise construction is credited; and a related subsequent Nesterov-type stochastic recurrence (arXiv:2611.26575v1), whose fixed-tap Gaussian error estimates do not state the complete arbitrary-tap two-mode calibration. Published published-finding corpus record similarities concern different samplers and were only inspectable as titles and summaries, so their whole texts cannot be ruled out. See `AUDIT.json` for actual queries, scientific implication comparisons and explicit residual priority risks.

## Value (PASS)

Gaussian invariant covariance is a natural accuracy criterion for unadjusted kinetic/momentum samplers; the question is whether one-step-cost temporal correlation can repair spectral bias without full mode-dependent harmonic integration. The result gives the complete two-eigenvalue attainability frontier (both feasible, three impossible), the only feasible noise-power/correlation invariants, and a strict underdispersion/overdispersion map, including a quantified interior deficit. This is a motivated structural design boundary, not a selected small numerical example or table; no general nonlinear sampler guarantee is claimed.

The result is structurally useful at the smallest number of distinct Gaussian curvatures where a single common colored-noise filter must trade off errors. Two modes are matched exactly and the systematic bias at any intermediate mode has a sharp sign and formula. It does not claim the more expensive harmonic matrix exponential is unnecessary or that all practical samplers are covered.

Self-review: passed. Independent audit: not yet performed.
