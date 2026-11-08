# Scientific review: extreme-displacement velocity and reset age

## Correctness — PASS

The proof derives the exact stationary exponential-age/Gaussian mixture for complete Poisson resetting. Gaussian conditioning gives the mean terminal velocity \(3x/(2t)\), conditional variance \(Dt/2\), and posterior age density proportional to \(t^{-3/2}\exp[-rt-3x^2/(4Dt^3)]\). The strict saddle at \(\tau_x=(9x^2/(4Dr))^{1/4}\) yields a full coercive joint large-deviation principle and a unique outward most-probable velocity. Minimizing the exponent over non-outward velocities gives the exact rate \(4(\sqrt2-1)/3\). Joint Gaussian age and velocity fluctuations follow from the exact conditional normal representation, with limiting covariance \(-\operatorname{sgn}(x)/4\) in the stated normalization. The standalone Python checker has been run successfully; its finite quadrature is corroboration, not an infinite-domain proof.

## Originality — PASS, qualified

Singh's 2020 complete-reset paper already establishes the exact underlying joint stationary mixture and the marginal position tail; those are not claimed as new. The inspected pertinent material in that paper does not state the full extreme-position-conditioned terminal-velocity LDP, its sharp non-outward exponent or joint age–velocity fluctuation limit. Montero, Palassini and Masoliver study a related position tail and crossing-rate observable; velocity at a crossing is flux-weighted, unlike a stationary snapshot. Related Brownian-area and velocity-only-reset sources were also compared, with limited full-text access noted. Research-index comparisons, including nearby age-saddle findings and exact velocity formulas in different models, yielded no covering result. The underlying published complete-reset mixture logically permits these new asymptotic deductions, so priority risk remains; missing a result in the searches does not establish global novelty.

## Mathematical value — PASS

At a very large observed displacement the inertial particle ordinarily moves outward with speed of order \(|x|^{1/2}\), while the conditional velocity spread is only order \(|x|^{1/4}\). The theorem quantifies the exceptional returning population by its sharp stretched-exponential rate and describes a nontrivial coupled age–velocity Gaussian law with universal correlation \(-\operatorname{sgn}(x)/\sqrt3\). These address an observable distinction between occupation-conditioned stationary measurements and level-crossing measurements; they are not isolated numerical constants.

## Limits and nearest literature

The statement requires simultaneous resets of both position and velocity, positive fixed diffusion and reset rates, and extreme-position conditioning in stationarity. It is not a first-passage or partial-reset theorem; finite-parameter errors and a closed elementary rate function are not established. Most relevant: Singh (2020), arXiv:2007.05576v1; Montero–Palassini–Masoliver (2023), arXiv:2312.13968v1; Meerson (2019), arXiv:1903.03963v1; Olsen–Löwen (2024), arXiv:2401.12685v1. The latter two were assessed at abstract level only. Independent scientific audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
