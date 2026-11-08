# Scientific review: exact four-cycle locking boundary

## Correctness

**PASS.** The theorem concerns the whole real plane in \(3/2<t<2\), with exact tie conventions inherited from the continuous max operator. The global trapping rectangle for periodic states and the exclusion of first-coordinate self-delay are proved without finite sampling. After this reduction, all 81 words of length four in the exhaustive three-mode alphabet are handled by an exact rational parametric linear-system calculation; only `HHHH` and the cyclic rotations of `HSDD` and `HSHD` survive, with the latter feasible exactly at and above \(t=5/3\). The two displayed primitive cycles satisfy the original map directly. The strict-region Jacobian products are zero and have eigenvalues \(\{4,0\}\). At the boundary, smooth differentiation is correctly withheld. The standalone `check_exact_phase.py` is a full finite branch certificate, not a sampled extrapolation.

## Originality

**PASS within inspected primary sources and indexed work.** Yamazaki and Ohmori (2023, arXiv:2306.00733, equation (8) and associated text) define exactly the same max-plus model and numerically observe locking. They do not provide a symbolic global least-period-four census, the ratio \(T/B=5/3\), or the exact fourth-return matrices. The earlier max-plus model in Ohmori and Yamazaki (2023, arXiv:2305.05908) is the \(T\to\infty\) limiting model, and the generalized oscillator of Ohmori and Yamazaki (2024, arXiv:2402.06230) uses a different piecewise-linear equation. Closest indexed quantitative max-plus recurrence results concern different reset and generalized oscillator maps and do not imply the present all-state phase boundary. The 2015 biological-feedback precursor is known from its abstract and citations but its full text was not inspected; publication-priority risk remains.

## Mathematical value

**PASS.** The originating dynamical literature specifically uses finite-step max-plus phase locking to understand how discrete four-state oscillations emerge. A complete exact onset threshold and strict two-orbit census answer a natural unresolved quantitative question in that same system. The distinction between an identically-zero fourth-return matrix and a \(4\)-eigenvalue unstable return reveals a nonsmooth border collision rather than a smooth fold. This is not a mere normalization or isolated arbitrary parameter evaluation; it classifies all primitive period-four orbits throughout the first locking window.

## Scientific limits

Only the strict region \(3/2<t<2\), the exponent \(m=2\), and primitive period four are classified. No conclusion is drawn for higher primitive periods, complete basins, or the smooth model's threshold. Exact classical Floquet spectra are not asserted at the switching collision. Equivalent older or unindexed accounts remain possible, and no independent review has occurred.

Self-review: passed. Independent audit: not yet performed.
