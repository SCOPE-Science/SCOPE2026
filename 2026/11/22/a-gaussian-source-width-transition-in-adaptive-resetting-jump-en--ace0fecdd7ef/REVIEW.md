# Review

## Correctness — PASS

The stationary inverse hazard follows by differentiating the Gaussian density in the Ornstein–Uhlenbeck adjoint and setting the Fokker–Planck flux balance to zero. The minimum admissible reset flux is obtained by a one-variable exact maximization. The jump entropy reduces to a covariance of the reset-flux ratio; its positive tail is a Gamma-half exponential transform with a calculated regular-variation constant. Mellin integration gives the subcritical amplitude, a truncated-second-moment argument gives the critical \((\log R)^{5/2}/R\) factor, and dominated convergence gives the supercritical amplitude and the uniform critical window. The independent finite computations verify the algebraic moments and representative limiting trends, not the infinite asymptotics.

## Originality — PASS (qualified)

The accessible full texts of Farago (2026), Keidar et al. (2025), Mori et al. (2023) and Chu et al. (November 2026, Supplement S2–S3), along with relevant existing mathematical research claims, were compared by implication. Chu et al. already give the generic inverse stationary reset policy and jump entropy covariance, so these are explicitly prior. Farago addresses different reset-clock/endpoint-KL protocols, Mori et al. analyze constant-hazard resetting and time-large-deviation entropy, and the closest available research records treat constant-hazard Gaussian engineering or endpoint Jeffreys divergence. No exact three-regime *stationary state-dependent jump-entropy* asymptotic with the uniform width window was identified. General formulas can in principle be specialized, so implicit prior derivations remain the principal originality risk; search noncoverage alone is not a proof of novelty.

## Value — PASS

An experimentally motivated Gaussian reset-source width controls whether high reset flux suppresses the jump-channel entropy at an ordinary inverse-rate scale or much more slowly. The sharp half-width boundary and its uniform \(1/\log R\) rounding quantify that design transition, including constants; this is not merely recalculating a low-order moment. The finding deliberately distinguishes the jump entropy from total thermodynamic costs, and does not claim a finite-hazard or finite-time implementation theorem.

## Scientific limits and comparison risks

Gaussian one-dimensional compression, unbounded state-dependent hazard, exact NESS, and asymptotic high reset flux are essential. A broad inverse-resetting thermodynamic theorem could contain an equivalent formulation not captured by the available comparisons; journal-level priority review is necessary. No independent scientific audit or experimental validation has occurred.

Self-review: passed. Independent audit: not yet performed.
