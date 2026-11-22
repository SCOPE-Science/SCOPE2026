# Scientific review: frozen-rate microscopic window in Brownian-squared confinement

## Correctness — PASS

The claim is a joint weak limit in the uniform path topology at fixed finite rescaled horizons and its exact bounded sign-correlation consequence. The conditional-Gaussian integrating-factor formula is exact. Brownian scaling and a deterministic endpoint-localization lemma show that the appropriately scaled thermal variance tends to \(D/(bG^2)\) off the null event \(G=0\). On a subsequent interval of physical width \(H/T\), the environmental coefficient freezes uniformly in probability at \(bG^2\), and independent future thermal increments converge to a fresh Brownian driver. Tightness and Gronwall control the replacement of the time-varying coefficient. The Gaussian-quadrant identity yields the arcsine mixture. Dominated convergence and a positive Taylor series determine the sharp \(u^{-1/2}\) coefficient. The package checker passed 26 consistency checks. The work does not infer process convergence from one-time convergence alone; it proves the required conditional time-window argument.

## Originality — PASS, qualified

The exact Brownian-square stochastic-stiffness model and its one-time moments are in Gupta–Klapp (arXiv:2609.33751v1). Their 24-page full primary text, including the model, thermal-moment section, thermodynamics, summary and appendix, was inspected. No microscopic-time trajectory limit or sign-correlation calculation appears in the inspected results. Gupta–Klapp (arXiv:2507.20915v2) treat an OU-driven stationary stiffness; their full accessible HTML text and model sections were inspected. The published result *Brownian-powered stochastic traps have sharp heavy-tailed scaling laws* explicitly proves the one-time Cauchy limit but states that multitime/pathwise limits remain open. The published *Rare-excursion intensity in Brownian-squared harmonic confinement* concerns fixed-threshold displacement tails, not temporal dependence. Both complete published scientific results were inspected. Searches of the research index and broader literature for random-rate OU, quadratic Brownian confinement, arcsine sign laws and microscopic path scaling found no theorem containing the composite statement. Absence of a hit is not uniqueness proof: a general unpublished quasi-static diffusion theorem might imply part of the result.

## Value — PASS

The physically motivated microscopic time scale \(1/T\) is forced by a stiffness of typical order \(T\). Knowing the one-time Cauchy law cannot tell whether nearby observations share the same thermal noise, trap rate, or hidden environment. The process theorem determines that dependence for every bounded observation window. It then identifies a sharp, non-integrable \(u^{-1/2}\) sign-memory tail despite conditional exponential relaxation, linking slowly fluctuating low-stiffness realizations to an observable position-only correlation. This is a structural dynamical fact rather than a finite-moment recomputation, arbitrary slice, or small numerical improvement.

## Closest work and limitations

Sources: Gupta and Klapp, arXiv:2609.33751v1 (first public 2026-09-27), https://arxiv.org/abs/2609.33751 ; Gupta and Klapp, arXiv:2507.20915v2, https://arxiv.org/abs/2507.20915 ; published Brownian-power scaling result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-brownian-powered-stochastic-traps-have-sharp-heavy-tailed-scalin--0700df2bd162 ; published rare-excursion result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-rare-excursion-intensity-in-brownian-squared-harmonic-confinemen--ac0f8defa0e9 .

The large-rescaled-lag tail is sequential, not a claim of uniform physical-time asymptotics. The theorem is not a convergence-of-moments result, and it does not cover correlated thermal/environmental noise or random stiffness processes other than Brownian-squared confinement. No independent scientific audit is asserted. An unindexed general diffusion averaging theorem remains an originality risk.

Self-review: passed. Independent audit: not yet performed.
