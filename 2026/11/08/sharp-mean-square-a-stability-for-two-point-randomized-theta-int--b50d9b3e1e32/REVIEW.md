# Scientific review: Sharp mean-square A-stability for two-point randomized theta integration

## Correctness — PASS

The theorem is proved from an exact one-step mean-square identity, an imaginary-axis two-atom numerator affine in frequency squared, the subharmonic maximum principle, and strict covariance monotonicity. The inclusion of the critical probability follows because the high-frequency limit equals one while every fixed open-half-plane point remains a strict contraction. The fourth-order boundary follows by a local analytic implicit-function argument. All 396 exact-rational verifier assertions passed; finite checks do not replace the proof.

## Originality — PASS (with precedence risk)

The primary 2024 randomized implicit RK2 paper fixes a uniform coefficient distribution and obtains its non-A-stability, while the new result classifies **all two-atom frequencies** and **every centered nonconstant distribution**. Earlier published uniform-case results and their fourth-order constant are expressly not claimed as new. Related 2020 explicit randomized RK and 2026 algebraically stable randomized SDIRK schemes use genuinely different updates. A specialist earlier equivalent law remains possible.

## Value — PASS

The phase transition gives the maximal allowable probability of selecting a less-than-midpoint implicitness coefficient while retaining full mean-square A-stability. It shows why coefficient centering alone is insufficient even for arbitrarily small randomness, and quantifies the sharp weak-damping stability notch. This is a complete natural classification of a reusable integrator family, not an arbitrary numerical example.

## Closest literature and limits

- Bochacik–Przybyłowicz, arXiv:2404.19059, sections 1.2 and 3.2, fixed uniform-law randomized implicit RK2.
- Bochacik et al., arXiv:2006.12131, sections 2 and 5.1, different explicit randomized RK rule.
- Lie–Stahn–Sullivan, arXiv:2103.16506, additive random perturbation model.
- Eisenmann et al., arXiv:2607.18928, separately algebraically stable randomized SDIRK scheme.

The conclusions are for the scalar linear test equation with fresh iid random coefficients. They do not show nonlinear, correlated-randomness, almost-sure, or convergence-rate results. No independent scientific audit is asserted.

Self-review: passed. Independent audit: not yet performed.
