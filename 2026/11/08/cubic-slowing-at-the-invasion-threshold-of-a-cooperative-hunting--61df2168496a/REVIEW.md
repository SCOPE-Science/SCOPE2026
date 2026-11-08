# Scientific review: critical extinction and local coexistence in a refuge map

## Correctness

**PASS.** The recurrence and critical parameter domain are copied from the source's normalized model (equation (2)). At \(\beta\gamma(\lambda-1)=1\), the boundary equilibrium has multipliers \(1/\lambda\) and \(1\). Expanding the exact nonlinear map on its attracting center manifold yields \(y'=y+(c-c_*)y^2+O(y^3)\), with at \(c=c_*\) the explicitly checked negative cubic coefficient \(-b\). Reciprocal-coordinate telescoping gives the precise \(n^{-1}\) and \(n^{-1/2}\) clocks. An implicit-function argument and both multipliers establish the small positive stable branch. The algebraic identities were reproduced by a standalone exact-rational power-series verifier and original-map numerical trajectories. These are local statements only; finite computations are not used as infinite-time proofs.

## Originality

**PASS on a best-knowledge basis.** Jang–Yousef (2023), Theorem 2.4, already places the cooperation cutoff at \(2c_*=[\lambda(2\gamma+1)-1]/(\lambda-1)\); that previously known threshold is not the contribution. The comparison instead asks whether prior results imply the *actual nonhyperbolic convergence exponents and constants*, or the stability/slope of the branch right above that cutoff. The complete accessible source's model and theorems, related 2025 delayed-cooperation work, accessible earlier-work descriptions, targeted mathematical record searches and local records did not yield such a model-specific theorem. General one-dimensional parabolic iteration would imply the rates once the coefficient and cancellation are established, but does not supply that nontrivial model-dependent calculation. A possibly unindexed related paper or inaccessible earlier manuscript is a residual priority risk; a negative search is not a proof of uniqueness.

## Value

**PASS.** The boundary reproduction number being exactly one leaves linear stability inconclusive. This model's ecological cooperation threshold coincides with cancellation of the first nonlinear restoring term, leading to a measurable transition in predator extinction time and a quantitative stable coexistence branch. The result sharpens an existing equilibrium-count threshold with explicit *dynamical* information for a natural ecological parameter boundary; it does not rest on an arbitrarily selected numerical slice. The restricted local domain and exact tuning limit empirical generalization.

## Closest literature and residual limits

Jang, S. R-J., and Yousef, A. M. (2023), *Effects of prey refuge and predator cooperation on a predator–prey system*, https://doi.org/10.1080/17513758.2023.2242372 : equation (2), Proposition 2.3, and Theorem 2.4 are closest. The source gives equilibrium nonexistence in the relevant parameter domain but no cubic slowing clock. Peng and Jiang (2025), https://doi.org/10.3390/modelling6030084 , concern a delayed continuous-time system with a different functional response, so their center-manifold/Hopf results do not establish this claim. Related records on cubic slowing in other ecological flows were also considered and do not imply the coefficients for this discrete refuge map. Incompleteness of exhaustive literature indexing remains a limitation. Independent external verification is absent.

Self-review: passed. Independent audit: not yet performed.
