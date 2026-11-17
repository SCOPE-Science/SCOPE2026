# Self-review

## Correctness — PASS
The critical exponential-risk map has multipliers \(1,e^{-m},e^{-m}\), and its quadratic center coefficient is \(\kappa^2\Psi(p)/(p^2h)\). Explicit differentiation gives \(\Psi'(p)<0\), hence a unique nonlinear transition, and one-dimensional reciprocal differences give \(n a_n\to-1/c_2\) in the attracting regime. Nonlinear instability on the opposite side follows from the positive biological center branch. The standard-library checker independently evaluates the exact map and coefficient identities; finite checks alone do not establish the theorem.

## Originality — PASS (provisional historical priority)
Muñoz, Nuño, and Meacci derive the exact map and linear invasion threshold (arXiv:2611.08353v1, Sections 4–5), while Katriel's related threshold analysis is continuous-time (arXiv:1812.08867). Neither inspected source supplies the finite-round center coefficient and sharp critical-time amplitude. Related published mathematical records describe different nonlinear epidemic models; general center-manifold theory by itself does not supply the model-specific expression. Broader priority remains open.

## Mathematical value — PASS
The nonhyperbolic invasion boundary needs a quadratic nonlinear test. The new scalar probability threshold gives a complete local stability-direction classification away from its unique equality case and determines the measurable \(1/n\) adopter relaxation coefficient for positive seeds. The finite-round shift of the threshold is meaningful for adoption rules in which updates occur in discrete rounds.

## Scope and risks
The equality \(p=p_*\), global attraction and finite-population extinction times are not established. The mathematical claims use a local deterministic map and an analytic proof with finite algebraic checks; there is no independent audit.

Self-review: passed. Independent audit: not yet performed.
