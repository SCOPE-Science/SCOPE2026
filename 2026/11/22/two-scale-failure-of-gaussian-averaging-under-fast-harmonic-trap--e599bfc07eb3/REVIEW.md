# Scientific review

## Correctness — PASS

Conditioning on the two-state trap path gives an exact bounded random stationary variance. The coupled zero-flux transport equations yield a properly normalized, positive beta-weighted Gaussian mixture. For fixed rare displacement \(y\), the phase diverges at the variance endpoints, has a strictly positive second derivative, and therefore has precisely one interior minimizer. The Stirling-normalized Laplace expansion produces the claimed prefactor, and the posterior normal limit and state-selection law follow by the same calculation. The inequalities, quartic expansion, remote-saddle expansion, and fixed-rate endpoint power were independently derived. A reproducible checker supports, rather than substitutes for, these infinite-parameter proofs.

## Originality — PASS, with residual risk

Alston, Cocconi and Bertrand (2022, arXiv:2202.02630) establish the two-state fluctuation model and rapid-switching thermodynamics, not the rare-scale rate profile. Biroli, Kulkarni, Majumdar and Schehr (2023, arXiv:2312.02570) explicitly provide the full stationary Gaussian mixture; that formula is prior knowledge, not a new result here. Their main text analyzes fixed-parameter stationary statistics and large-population extreme values, rather than the nested quartic crossover and the rapid-switching single-particle saddle with full prefactor, hidden-state selection and inverse reconstruction. Two additional materially examined published switching-harmonic-gas findings give sharp empirical-energy tails at speed N, and Gumbel maximum edge layers at scale log N, always with fixed switching rate. Their rare-event variance selection applies to large particle populations rather than the present joint fast-switching, single-position regime. The remaining publication-priority uncertainty includes related supplemental materials and later broad variance-mixture analyses.

## Mathematical value — PASS

Fast-switching homogenization gives the correct stationary central Gaussian but can drastically understate rare displacements on the natural square-root-rate scale. An explicit global strict-rate inequality, prefactor and selected hidden-trap posterior quantify exactly how the approximation fails and how atypical positions encode both trap stiffnesses. The two exact nested displacement scales and the ability to reconstruct the two trap stiffnesses are natural structural phenomena, not an arbitrary parameter slice or restatement of the known finite-parameter mixture. The result does not purport to be a new finite-parameter stationary distribution or an independent certification.

## Scope and residual risks

The theorem is limited to two strictly confining and distinct stiffnesses, symmetric Markov switching and common Brownian diffusivity. The exact stationary mixture predates this work; the novelty assessment rests on the singular two-scale joint limit, conditional state selection and nonuniform-Gaussian inverse signature. A 2026 age-structured switching-trap article was available at abstract level only. The full supplements to the 2023 primary article were not independently checked for an implicit equivalent asymptotic theorem.

Self-review: passed. Independent audit: not yet performed.
