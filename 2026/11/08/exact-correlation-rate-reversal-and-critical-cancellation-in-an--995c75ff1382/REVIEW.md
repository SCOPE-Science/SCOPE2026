# Scientific assessment: OU-squared covariance rate reversal

## Correctness — PASS

The statement is limited to the square-integrable stationary causal solution with \(\kappa>2D_K/\mu^2\). Reconstructing the two-sided stochastic convolution and applying conditional Itô isometry leaves precisely the Brownian increments shared by \(X_0\) and \(X_t\). The two adjacent Gaussian stiffness integrals have variance \(2q[s-(1-e^{-\mu s})/\mu]\) and cross-covariance \(b(1-e^{-\mu u})(1-e^{-\mu t})\); the cross term is essential. A positive substitution reduces the result to \(J_\lambda(c)\). Differentiating gives the exact logarithmic rate. Its sign relative to \(\kappa-q\) is the sign of a strictly increasing exponential-tilt mean minus one-half, proving existence, uniqueness, all endpoint regimes, and the critical asymptotic coefficient. The stationary derivative \(C'(0+)=-D\) and 96 reproducible numerical checks independently corroborate the normalization. None of the numerical checks is treated as an infinite proof.

## Originality — PASS (best-knowledge comparison)

The 2024 motivating paper's Eqs. (30)–(34) derive the stationary variance, not the two-time particle-position covariance, so they do not imply the new rate-crossing phase classification without a new two-interval calculation and monotone-tilt argument. The related 2023 article's Eqs. (B8)–(B9) concern a decoupled *constant*-stiffness ordinary OU coordinate, while Eqs. (B13)–(B20) give only the OU-squared one-time variance. The 2022 fluctuating-potential article concentrates on entropy production and stationary statistics. The 2025 OU-stiffness article focuses on position moments and work/heat and is a potential related-work priority risk. Related published findings on Poisson-reset energy correlations, intermittently switched two-state stiffness and active-particle covariances have different stochastic generators and do not imply this continuous-Gaussian-stiffness theorem. Search results did not reveal exact prior coverage, which alone is not proof of global novelty.

## Mathematical value — PASS

The result supplies a physically interpretable, exactly classifiable temporal memory signature absent from single-time moments: the measured instantaneous correlation decay can approach its asymptotic rate from above, below, or reverse direction at a unique lag. The critical curve where the first relaxation correction disappears forces a sharp second-harmonic temporal scale, giving a nontrivial structural boundary in experimentally motivated fluctuating traps. The exact phase boundary and crossover time are not arbitrary parameter tuning or merely numerical curve-fitting; they follow from strict convexity of a natural tilted occupation-weight integral.

## Principal limitations and residual priority risks

The theorem applies to square-integrable stationary OU-squared position dynamics with independent noises, not general random environments. Finiteness of variance is known prior work. Unindexed broad Gaussian filtering or Feynman–Kac theory might dominate the formula or classification. A full independent literature and scientific audit is not claimed. The checker tests finite parameter sets and cannot certify the universal quantifiers.

Self-review: passed. Independent audit: not yet performed.
