# Self-review

## Correctness — PASS

The exact stationary variance follows from the quadratic generator identity, and the two-time covariance follows from the linear Markov semigroup. Integration of this covariance yields the exact time-average variance. Optimizing the resulting positive Laplace quotient gives a derivative with precisely one sign change. The normalized Laplace weight has strictly positive variance, so its mean decreases with multiplier-transformed variable; a strict likelihood-ratio ordering as the observation window grows proves that the unique optimizer changes monotonically. A strict exponential reweighting bound locates it between zero reset and a one-third sign reversal. First-order expansions at both observation-duration endpoints and direct cubic maximization of the long-window rate agree with the boxed claim. The standalone checker passes 83 assertions, including Monte Carlo integration of Brownian bridges; no finite computation is treated as an all-duration proof.

## Originality — PASS, qualified

Biroli et al., arXiv:2406.08387v1 (2024-06-12), give the identical signed partial-resetting dynamics and optimize first passage. Their findings do not compare stationary finite-window signed-position time-average fluctuations across all signed multipliers. Di Bello et al., arXiv:2305.13722, Tal-Friedman et al., arXiv:2205.03363, and Olsen–Löwen, arXiv:2406.10039, provide various marginal, positive multiplier and refractory-process formulas. Closest published published-finding corpus findings provide linear conditional-moment rates, positive-multiplier long-time signed-area variance in a refractory extension, fourth-order time asymmetry, or quadratic reset-work fluctuations; none of their inspected statements or implications subsumes the unique strictly negative finite-window optimum and its monotonic evolution. Conventional covariance integration and semigroup methods are explicitly prior technique. Remaining publication-priority risk is a general or unindexed parameter-optimization theorem. The structured scientific comparison is in AUDIT.json.

## Mathematical value — PASS

Sampling noise of a signed physical position average is a natural temporal measurement. The exact all-window optimal protocol yields a sharp and counterintuitive distinction: complete resets minimize one-time variance, whereas strictly reflected partial resets minimize every positive-duration time-average variance. The global uniqueness, strict duration monotonicity, endpoint laws, and exact long-time improvement of 5/32 provide an interpretable stochastic-control principle with clear experimental timescale dependence.

## Scope and limits

The theorem is for one stationary symmetric scalar diffusion with independent Poisson events and constant deterministic signed contraction. It does not address nonstationary initial laws, multi-particle interactions, energy dissipation, first passage, refractory times or nonsymmetric noise. Checked numerical instances do not establish the infinite theorem and literature searches cannot certify priority absolutely.

Self-review: passed. Independent audit: not yet performed.
