# Scientific review: exact damping offset in Brownian gyrator precision

## Correctness — PASS

Under the stated strict stability and nonequilibrium assumptions, the Ornstein–Uhlenbeck drift is Hurwitz. The full stationary covariance is independently verified through all entries of the Lyapunov equation. Gaussian fourth-moment contraction gives the one-time variance, and the derivative has precisely one positive zero with a sign change from positive to negative. The strict optimizer comparison follows from positive temperature product and positive temperature contrast. `verify_gyrator.py` independently replays 219 symbolic/rational tests. The proof is finite-dimensional and exact; no unproved asymptotic extension is used.

## Originality — PASS (qualified)

The full motivating arXiv:2603.18818 source publishes the mean angular-momentum maximum and covariance but does not optimize the one-time stationary mean-to-standard-deviation objective. Bae et al. (arXiv:2012.12713) provide long-time **integrated-current** fluctuation coefficients, not the **instantaneous** Gaussian-product variance or damping peak in this claim. The 2026 Dutta–Saha ellipsoidal model discusses related signal-to-noise performance and finite-inertia optima. Its full paper could not be examined, so possible coverage of this exact spherical-limit optimizer remains an explicit publication-priority risk. The claim is restricted to the previously unlocated full analytic all-parameter closed-form optimizer and its strict damping offset, not to the general observation that fluctuations can be optimized.

## Value — PASS

The mean heat-flow and entropy-production maxima measured in the recent gyrator experiment need not coincide with the damping that maximizes standardized single-frame rotation. A universal exact separation and sharp contrast-dependent bound give a natural, measurable design comparison over the complete stable unequal-temperature regime, not a chosen numerical slice. The result is useful even though the equilibrium Gaussian covariance formula is already known. Single-frame precision is **not** a replacement for trajectory-level measurement precision.

## Closest prior work and remaining limits

- Martins et al., arXiv:2603.18818, complete accessible HTML Methods and main text, Eq. (7) covariance and Eq. (5) mean.
- Bae et al., arXiv:2012.12713, full original PDF, Eqs. (11)-(16) and Appendix C on time-integrated current.
- Dutta and Saha, arXiv:2606.17554, abstract and secondary summary only; full text inaccessible. The broader model presents a plausible residual priority comparison, not a demonstrated identical exact theorem.

The result requires a strictly confining linear trap and two positive unequal Gaussian bath temperatures, and addresses instantaneous—not time-averaged—angular-momentum SNR. No independent scientific audit was conducted.

Self-review: passed. Independent audit: not yet performed.
