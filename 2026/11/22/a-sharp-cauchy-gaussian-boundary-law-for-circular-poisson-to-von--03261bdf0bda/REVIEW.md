# Scientific assessment

## Correctness — PASS

The claim distinguishes finite-radius existence and unique center alignment from the asymptotic concentration law (finite-radius concentration uniqueness is not asserted). Exact Fourier positivity forces alignment; Bessel norm growth gives finite-parameter attainment. Strong rescaled \(L^2\) convergence yields the explicit Cauchy–Gaussian error function. A positive Laplace representation proves strict monotonicity of its stationary function, establishing a unique limiting optimizer. Two escape-of-scale arguments give equicoercivity and transfer the unique limit to every minimizing concentration. The first circular-moment comparison follows from the monotone Bessel-ratio equation and its classical expansion. `verify.py` independently checks finite-radius values and constants, but those checks are not the proof.

## Originality — PASS (best-knowledge)

Lewis (2021), arXiv:2105.13199, studies Stein/Wasserstein bounds for related circular families, not deterministic optimal \(L^2\) fitting. Ameijeiras-Alonso (2024), DOI:10.1007/s11222-024-10384-x, studies sample-dependent bandwidth selection and AMISE of kernel density estimators, not this target-approximation problem. Hundrieser–Klatt–Munk (2021), arXiv:2103.15426, studies optimal-transport statistics. A closely related heat-to-Poisson result has a different variable family and scale-normalization; it does not imply the stated complementary-error-function equation or factor of 14.17. Database and literature comparisons were performed by claim implication rather than title similarity. Absolute historical priority is not independently established.

## Value — PASS

The theorem answers a natural width-calibration problem between two standard circular smoothing families and identifies a universal sharp boundary constant. Crucially, it shows that canonical first-moment calibration chooses concentration of order \((1-r)^{-1}\), whereas the globally least-squares-accurate approximation requires order \((1-r)^{-2}\). The resulting factor \(14.17\ldots\) squared-error penalty quantitatively demonstrates a meaningful breakdown of a commonly used calibration rule. This is a structural continuum limit and optimizer-location theorem, not a finite benchmark or a reparametrized textbook identity.

## Closest literature and limits

The primary texts were inspected at their relevant results and discussion sections. No directly dominating best \(L^2\) projection theorem was identified. Unindexed prior work and historical-priority uncertainty remain possible. Finite-radius concentration uniqueness and other divergence criteria remain outside the scope.

Self-review: passed. Independent audit: not yet performed.
