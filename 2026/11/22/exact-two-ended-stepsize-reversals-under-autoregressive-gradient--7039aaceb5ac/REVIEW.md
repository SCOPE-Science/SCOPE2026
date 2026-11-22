# Self-review

**Correctness — PASS.** The terminal risk is exactly the strictly convex quadratic \(D^2(1-\mathbf1^\top w)^2+\sigma^2 w^\top Cw\). Inverting the known positive-definite AR(1) Toeplitz matrix gives a positive interior global minimizer, and the sequential weight-to-step map uniquely realizes it. The two edge comparisons and the unique root separating unconditional terminal upturn were derived with strict equality cases. The accompanying standalone exact-rational verifier corroborates the formulas. Finite tests do not establish universal statements.

**Originality — PASS, qualified.** Grimmer–Shen's 2026 exact optimal schedule uses martingale-centered noise, while this result allows temporally AR(1)-correlated noise and fixes a scalar quadratic. Hermans et al.'s AR(1) generalized-least-squares weights are explicitly prior and not claimed as new. Published heterogeneous-variance SGD, spectral-step rearrangement, correlated-heavy-ball, and Markov-stepsize analyses address different hypotheses or objectives. The claimed addition is the complete sign-dependent first/last upturn phase diagram for the exact finite-horizon sequential learning-rate optimum. An earlier equivalent derivation may remain undiscovered.

**Value — PASS.** The classification answers a motivated robustness question about decreasing schedules when oracle noise is colored but its variance does not change. It isolates the only two possible locations of reversals and shows precisely how signal-to-noise ratio and time horizon determine each. No extension to nonlinear or multidimensional objectives, unknown covariance or adaptive learning rates is claimed.

**Limitations.** The proof is for known unit curvature, stationary AR(1) second moments, deterministic rates in \([0,1]\) and terminal mean-square risk. It does not provide empirical training gains or independent certification. Classical estimation theory supplies essential ingredients.

Self-review: passed. Independent audit: not yet performed.
