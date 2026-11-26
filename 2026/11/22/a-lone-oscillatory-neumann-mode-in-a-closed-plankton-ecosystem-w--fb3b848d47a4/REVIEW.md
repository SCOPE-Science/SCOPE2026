# Scientific assessment

## Correctness — PASS

At the explicitly positive equilibrium of mean biomass density \(35/2\) and integrated biomass \(35\pi\), each reaction residual vanishes exactly. The Jacobian, quartic dispersion polynomial, and both Routh–Hurwitz determinants were reconstructed from the original reaction equations, rather than numerical eigenvalues. The homogeneous cubic is Hurwitz on the conserved-mass hyperplane. The \(n=1\) mode satisfies all strict Hurwitz inequalities. At \(n=2\), the quartic Routh sign variation counts two right-half-plane roots while positivity of all polynomial coefficients excludes nonnegative real roots; the instability therefore is an oscillatory pair. For every \(n\geq3\), strictly positive coefficients after the \(q=9/4+u\) shift prove all Hurwitz inequalities simultaneously. The cubic discriminant rules out \(b_0\leq0\) on the positive continuum. `verify_npzd.py` exactly recomputes the algebraic spectral certificate. Risks: no nonlinear stability/instability of patterned states is proved.

## Originality — PASS (literature-bounded)

Xu–Campbell–Poulin (2026), arXiv:2611.10221v1, establishes the precise NPZD kinetics, conservative linearization, and examples of diffusion-driven instability, and emphasizes the \(b_0<0\) real-mode criterion with separated diffusion coefficients. The full model, analysis, numerical results and appendix were inspected. The present exact one-diffusion-contrast example has \(b_0>0\) for all positive squared wavenumbers and a unique oscillatory unstable harmonic, which is not stated or dominated by those explicit examples. Earlier NPZD Hopf work (Macdonald–Gulbudak, 2023) treats different kinetics and chiefly temporal stability. Villar-Sepúlveda and Champneys (2023) give general wave-instability existence conditions for reaction–diffusion matrices, but no model-specific, one-harmonic closed NPZD classification. Other ecological systems have isolated oscillatory modes, but their kinetic matrices are different. A previously derived same-model stationary-determinant example changes a different diffusion coefficient, produces a real instability, and does not imply this oscillatory spectral claim. Searches do not prove uniqueness; unindexed special cases remain a residual priority risk.

## Value — PASS

The example resolves a motivated qualitative distinction in a recently analyzed ecological model: an exact Fourier mode can oscillate unstably even when the standard stationary-mode determinant is positive everywhere. It additionally identifies an admissible single-diffusion-contrast mechanism and isolates exactly one physical Neumann harmonic, with an infinite-mode proof rather than finite numerical scanning. These are direct mechanistic and spectral conclusions, not arbitrary numerical precision or a routine reproduction of the original paper's simulations.

Self-review: passed. Independent audit: not yet performed.
