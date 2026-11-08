# Scientific review: Gaussian stationary fluctuations in rightmost-reset Ornstein–Uhlenbeck groups

## Correctness — PASS

The exactly sampled Ornstein–Uhlenbeck group maximum yields the affine reset-epoch recursion with independent exponential intervals and independent Gaussian maxima. The stationary perpetuity is contractive for every positive rate and confinement. Beta integrals independently establish exact finite-rate first and centered second moments. With reset rate tending to infinity at fixed finite particle number, centering the recursion gives a triangular martingale array with limiting innovation variance \(2D(\nu_N-\pi\mu_N^2/4)\), predictable weight decay \(e^{-ks}\), and a uniformly controlled infinite tail. Its Gaussian limit has variance \(D(\nu_N-\pi\mu_N^2/4)/k\). Ordinary-time particle deviations from the most recent reset location vanish in probability. The included checker passed 52 finite assertions; the analytical proof, not the simulations, supports the infinite-rate statement.

## Originality — PASS, qualified

The full papers arXiv:2412.02524v3 and arXiv:2604.24406v2 were compared with the exact claim. The former gives a renewal framework, stationary mean and variance/scaled variation using large-group Gumbel approximations, but not the explicit fixed-particle-number high-reset Gaussian limit and clock-corrected coefficient. The latter concerns absorbing-boundary first-passage behavior rather than the unabsorbed stationary law. The full paper arXiv:2602.21635v1 concerns frequent small proportional reset maps rather than jumps to the evolving rightmost group member. Searches of mathematical research records and indexed literature did not locate an equivalent result; that absence does not establish uniqueness. Classical martingale limit theory is acknowledged as a proof tool, and an unindexed specialization may exist. The difference between a kernel equation and an evaluated scaling law is explicit.

## Mathematical value — PASS

The recent group-resetting studies emphasize that the distributional shape, not merely stationary means and coefficients of variation, controls group avoidance. This result supplies a complete nondegenerate high-frequency central law with explicit, directly computable finite-group constants, exact two-particle values and a whole-group collapse statement. It reveals a positive contribution from randomness of reset intervals that would be lost by replacing them with average intervals. Fixed-quantile predictions follow, while exponentially small fixed-boundary probabilities are expressly outside scope. A specialized theorem of this precision is motivated by the stationary reference system rather than an arbitrary parameter slice.

## Closest literature and limits

Sources: Lee et al., arXiv:2412.02524v3 (full §§II–IV and appendices); Lee et al., arXiv:2604.24406v2 (full model, results, appendices); Galla, arXiv:2602.21635v1 (full diffusion-approximation construction and supplement); Majumdar et al., arXiv:1509.04516 (distinct historical-maximum lattice model); Biroli et al., arXiv:2211.00563 (fixed-origin Brownian gas). Remaining risk: an unindexed earlier or broader random-affine-recursion theorem that explicitly evaluates this rightmost-reset variance. The claim does not cover absorption, large deviations or simultaneous growth of group size and rate.

Self-review: passed. Independent audit: not yet performed.
