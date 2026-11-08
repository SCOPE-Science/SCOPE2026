# Mathematical review

## Correctness

**PASS.** The source formula is conjugated exactly to \(y_{n+1}=y_n+a[(1+e^{y_n})^{-1}-b_n]\); its derivative has absolute value strictly below one after integration over any nondegenerate interval for \(0<a\le8\). The bounded inwards drift and strict inter-trajectory distance decrease supply the compactness and convergence arguments needed for all quantifiers. At \(a=8\), the periodic return multiplier can have modulus one only on the centered constant input; the cubic normal form proves the explicit inverse-square-root coefficient away from finite preimages. For \(a>8\), the centered fixed point is repelling. The checker confirms formal identities and finite samples, but the infinite claims rest on the proof.

**Limits.** No global-rate bound uniform in all periodic inputs is claimed, and no convergence theorem for arbitrary time-varying normalized learning intensities is asserted. Boundary initial states are excluded; preimages of the centered critical equilibrium are separated.

## Originality

**PASS within inspected evidence.** Chotibut et al. already prove the centered autonomous threshold and the autonomous mean law; Kryzhevich et al. and Falniowski–Mertikopoulos analyze stationary parameters. The complete closest report on asymmetric replicator two-cycles concerns a fixed equilibrium target and cannot imply the switched-target result. Vlatakis-Gkaragkounis et al. analyze a *variable learning rate* with fixed target and a different nonautonomous evolution. The new assessed claim is the globally attractive response under arbitrary periodic target switching at a sharp input-independent threshold, the single exceptional nonhyperbolic schedule and exact critical slowdown, and bounded-input same-input synchronization. Generic contraction arguments explain subcritical behavior but do not directly address the nonuniform endpoint multiplier or its normal-form constant.

**Residual risk.** Complete historical priority remains unverified; some related older literature was abstract-only, and a general nonautonomous contraction result might dominate the simpler qualitative subclaims. This does not amount to a verified exact implication of the complete theorem.

## Mathematical value

**PASS.** The phenomenon is a natural complete regime classification for learning under shifting target equilibria: periodic forcing cannot destroy unique attraction below the sharp uniform intensity, while the critical relaxation is rigid to just one constant schedule. An exact calibration identity persists above the synchronization threshold, separating two different statistical and dynamical notions of adaptation. This boundary classification is meaningful independently of large-scale algorithmic claims.

## Reproducibility and prior work

The accompanying `RESULT.md` gives all definitions, hypotheses, strict inequalities and limit arguments; `verify.py` checks symbolic identities and targeted diagnostics. The exact model and the autonomous cases are attributed to arXiv:2603.20685, arXiv:1807.06831, arXiv:2412.16379 and arXiv:2402.09824; nonautonomous adaptive-step context is arXiv:2306.01032. These sources do not constitute exhaustive bibliographic certification.

Self-review: passed. Independent audit: not yet performed.
