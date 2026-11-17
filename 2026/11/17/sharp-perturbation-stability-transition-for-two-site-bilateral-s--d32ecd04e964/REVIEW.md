# Scientific review

## Correctness — PASS
The operator is exactly a mean-preserving two-site contrast transform. The necessary-and-sufficient kernel criterion is obtained without derivatives; differentiation of the inverse-power and Gaussian contrast functions then determines their unrestricted global moduli. Explicit derivatives and unique maxima are verified analytically. Every coordinate \(\ell^q\) norm follows from a swap-matrix decomposition; the finite checker independently corroborates the constants and tests. Nonattainment in the amplified regime follows from isolation of the derivative maximizer.

## Originality — PASS, qualified
The closest examined literature is Tomasi–Manduchi (1998), Pianykh (arXiv:1007.1016v1), and Pan–An–He (2014). Pianykh's Abs/Frac/Quad/Exp kernels directly match exponent-one, exponent-two, exponent-four and Gaussian affinities; his response statistic is a one-input deviation ratio for modeled distributions, not the sharp two-input perturbation quotient proved here. Tomasi–Manduchi supplies the foundational filter definition; Pan–An–He treats fast computation for arbitrary kernels. published-finding corpus and accessible record-overlap queries did not identify a theorem covering the sharp all-exponent and Gaussian conclusions. This is evidence of an unresolved gap, not proof that no earlier unindexed result exists.

## Mathematical value — PASS
The exact if-and-only-if criterion and sharp critical power-tail exponent \(p=1\) distinguish kernels that are genuinely nonexpansive under adversarial perturbations from kernels that merely reduce each signal's contrast. The closed sharp amplification factor and Gaussian maximizer give precise worst-case benchmarks for natural nonlinear edge-preserving filters. The two-site restriction is an explicit boundary, not a claim about complete images.

## Limitations and historical-priority risk
The proof applies to symmetric unit-self-weight bilateral filtering of two real observations after one simultaneous update. Unequal self-weights and larger grids remain open in this treatment. The nearest historical paper already explores the same kernel families for a different observable; an unindexed exact derivative analysis could overlap the result. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
