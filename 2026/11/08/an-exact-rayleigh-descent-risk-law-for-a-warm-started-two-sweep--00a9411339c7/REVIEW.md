# Research review

## Correctness — PASS

The numerator in the exact Rayleigh-quotient subtraction is positive times \(a^2b^2-(\beta u)^2\); its denominator is strictly positive for a non-eigenvector start, including when one transformed coordinate vanishes. This proves the exact strict-decrease condition and the two robust parameter caps. Haar sampling gives the classical \(\operatorname{Beta}(1/2,1/2)\) coordinate mass, so the full probability and quantile inversion follow analytically. Both endpoint constants follow by a square-root expansion. The bundled checker reproduced the exact factorization, direct step behavior, probability grid, and endpoint constants; finite checks are corroborative rather than infinite proofs.

## Originality — PASS, with residual historical-priority risk

The originating 2026 two-sweep paper's Methods 2 and 3 and its convergence analysis establish update definitions and asymptotic performance criteria, not the precise first warmed step's Rayleigh-sign criterion, the all-parameter Haar-start probability law, or its inverse risk cap. Relevant earlier momentum power papers discuss acceleration, convergence and different coefficient constructions. Mathematical implication was checked: convergence for an admissible parameter sequence does not furnish a sharp one-step all-initialization probability formula for arbitrary \(\beta\); general power-method monotonicity does not apply to the additional previous-iterate term. An equivalent first-step identity or distribution in older unindexed momentum literature remains possible and is not claimed impossible.

## Value — PASS

The failure event is an operational numerical quantity for a spectral solver: deterioration of the Rayleigh estimate immediately after the first parameterized two-sweep update. The exact zero-to-one phase law, sharp universal safety cap, and probability-constrained parameter inversion distinguish guaranteed-safe, mixed-risk and universally-decreasing regimes. They provide a mathematically motivated tuning benchmark for the newly proposed method, rather than an arbitrary example or a mere restatement of general power iteration. The result does not establish that the full safeguarded or regression-enhanced algorithm fails.

## Closest literature and limitations

The closest primary source is Sun, Peng, Zhang and Vong, arXiv:2610.41627, especially Section 2's normalized two-sweep recurrence and Section 3's convergence theorems. Also inspected were Rabbani et al., arXiv:2108.09264, and Austin, Pollock and Zhu, arXiv:2403.09618. Scope is an SPD two-mode, one-step warm-start model with fixed real coefficient. No statement about longer iterations, full parameter-learning behavior or roundoff follows. Exhaustiveness of all historical literature is not asserted.

Self-review: passed. Independent audit: not yet performed.
