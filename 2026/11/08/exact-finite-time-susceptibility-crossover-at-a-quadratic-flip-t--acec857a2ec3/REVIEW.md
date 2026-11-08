# Self-review

**Correctness — PASS.** The exact two-step recursion can be checked by direct expansion. The inverse-square coordinate has a linear-in-parameter affine leading recurrence, with accumulated \(O(\sqrt N)\) error; differentiating its exact expression gives the sensitivity convergence and controls the early-time layer. The explicit small-\(z\) series gives the exact constants; the two-step Jacobian product gives the Lyapunov coefficient. Symbolic verification checks the critical identities, and finite-trajectory tests reproduce the integral profile but are not infinite proofs.

**Originality — PASS within inspected evidence.** Martin–Tang–Chialvo (arXiv:2505.24673, Methods and Appendix) introduced the same map and the susceptibility with exponent \(N^2\) and numerical collapse. The present result does not appropriate these ingredients; it proves the entire susceptibility response profile and the derivative limit, critical amplitudes, and a signed Lyapunov coefficient. Corral (arXiv:2405.19947) proves related state scaling at nonoscillatory transitions. Other indexed claims were compared by mathematical implication. Historical priority remains provisional, especially for work outside indexed search.

**Mathematical value — PASS.** The source identifies critical finite-time response and a peak in parameter space as a potential diagnostic; this theorem computes the full analytic curve and rigorously identifies its positive-side displacement, as opposed to giving a mere exponent. A singular early-time sensitivity layer is controlled and the exact amplitude is observable-independent within the stated canonical normalization.

**Scope and limitations.** Only the canonical polynomial quadratic-flip map with \(0<Qx_0<1/4\), fixed \(Q>0\), and parameter scalings \(\mu=z/N\) is covered. The right-hand peak is not claimed unique. Numerical tests are not independently certified.

Self-review: passed. Independent audit: not yet performed.
