# Scientific review

## Correctness
**PASS.** The claim is derived from the specified positive-definite, orientation-dependent Stratonovich mobility model. Converting to Itô form yields the exact drift and an orthogonal split of thermal noise. Integrating *within* each independent Poisson reset interval avoids the false positional jump that would arise from integrating the angular coboundary across reset events. The independent-cycle renewal-reward formula yields both the centered covariance per unit time and the Gaussian central limit theorem. The complete cycle calculation uses exponential angular Fourier moments of orders one and two, plus the mixed time transform. Symbolic identities in the accompanying executable confirm the full covariance formulas and factored extremality derivative; the sign argument proves the universal maximum over the entire positive reset-rate axis, not merely a finite grid. The strictly positive mobility hypothesis is independently feasible, as demonstrated by the explicit matrix in the result.

## Originality
**PASS, qualified.** The 2026 primary paper by Cleuren and Eichhorn introduces the correlated translation–rotation colloid and determines periodic-reset mean drift, but does not present the Poisson resetting covariance tensor or its optimal anisotropy rate. Chaki, Olsen and Löwen's 2024 orientation-reset tensor presupposes independent translational and rotational thermal noises, so its isotropic translational specialization has no counterpart to the nonzero off-block mobility mechanism here. Ghosh and Mandal's 2025/2026 orientation-reset analysis instead uses active propulsion and diagonal body-frame noise. Published research-record searches using the source identifier, mobility aliases, anisotropy and sharp optimum returned no matching claim; their closest hits concerned different covariance, random sensor, and geometric problems. This supports originality relative to inspected sources, not proof of global publication priority. The residual risk is an unlocated general homogenization or correlated-colloid formula implying this sharp specialization.

## Value
**PASS.** The motivating paper identifies diffusion changes and stochastic nonpositional resets as natural open directions for sorting and mixing. The new theorem determines a measurable, physically motivated covariance-rate anisotropy for that same correlated-mobility model. It proves that isotropic translation does not rule out anisotropic long-time spreading, identifies the drift-aligned principal axis, and gives a sharp protocol-independent optimizer \(r=2\alpha\) for the absolute principal-rate gap. The optimum and amplitude furnish a finite-rate experimental design benchmark, rather than an arbitrary numerical slice. A sorting signal-to-noise optimum is not claimed.

## Closest literature and residual limits
- B. Cleuren and R. Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1, https://arxiv.org/abs/2603.19430 (the exact Brownian mobility model; periodic resetting and mean motion).
- S. Chaki, K. S. Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550, https://arxiv.org/abs/2406.17550 (independent angular and translation noises; orientation-only resetting diffusion).
- A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149, https://arxiv.org/abs/2501.05149 (explicit active propulsion and diagonally driven orientation).

The statements concern ideal instantaneous orientation jumps at independent Poisson times and an isotropic translational mobility block. Independent experimental validation and independent mathematical or priority review have not been performed.

Self-review: passed. Independent audit: not yet performed.
