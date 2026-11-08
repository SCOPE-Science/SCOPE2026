# Mathematical assessment

## Correctness — PASS

The claim is for a trace-one incoherent mixture of normalized reciprocal squeezed Gaussians and the **squared** Hilbert–Schmidt norm of its localization operator over equal-area rectangles. The exact Gaussian cross-ambiguity kernel has coefficient \(\kappa_s=2/(s+s^{-1})\), with the same parameter in the isotropic exponent; this is critical because a missing coefficient changes the curvature. Direct Gaussian integration proves the formula, the logarithmic-differential Hessian follows exactly, and uniform local Taylor/error-function estimates establish its negative-small, positive-intermediate, negative-large sign pattern. Evenness and decay at extreme aspects supply the nonsquare global maximizers. All required quantifiers are asymptotic/existential, not numerical finite thresholds. The companion checker tests overlaps, convolution integrals, derivatives, and a concrete example; the proof, not the checker, justifies every infinite statement. Risk: the theorem does not determine exact transition points or optimizer uniqueness.

## Originality — PASS (best-knowledge, not an independence assertion)

Searches covered “mixed-state localization operator,” “Hilbert-Schmidt,” “rectangle,” “reciprocal squeezed Gaussian,” “aspect-ratio instability,” “bifurcation,” and equivalent Gaussian-overlap/rectangular-self-energy formulations in the cited primary literature and existing research records. Nicola–Riccardi (arXiv:2401.04659) assumes a *single isotropic Gaussian*, proving global ball optimality among domains, and does not imply a mixed-window square Hessian. Luef–Skrettingland (arXiv:1802.02435) develops the mixed-state framework and window-sum formula without this geometry. Nicola–Tilli (arXiv:2207.08624) optimizes operator norm under symbol constraints, a different norm, window and optimization class. The earlier paired squeezed-window ambiguity-denominator result concerns a pointwise disk minimum, not this integrated squared operator norm. No retrieved published-finding corpus hit established the same statement or a stronger covering theorem. Risk: semantic search cannot establish uniqueness in the complete literature; a specialist earlier analysis could exist.

## Value — PASS

Sharp localization geometry and Hilbert–Schmidt concentration are natural quantities in multiwindow time-frequency analysis. Symmetry of the balanced density operator might suggest a square should be locally preferred at every area; the theorem provides a rigorously motivated counterexample and proves an area-driven reentrant stability pattern, rather than selecting an arbitrary finite parameter instance. It gives a mechanism (competition between incompatible anisotropic kernels) and a reproducible exact energy/Hessian formula suitable for further study. It neither asserts exact bifurcation thresholds nor a general shape optimizer beyond rectangles.

## Closest literature and limits

- F. Nicola and F. Riccardi (2024), arXiv:2401.04659: primary source for the Hilbert–Schmidt geometric concentration problem, single Gaussian and ball rearrangement; not a mixed-state result.
- F. Luef and E. Skrettingland (2018), arXiv:1802.02435: general multiwindow/mixed-state operator theory; does not imply the aspect transition.
- F. Nicola and P. Tilli (2022), arXiv:2207.08624: sharp operator-norm but not mixed-state Schatten-two geometry.
- S. Halvdansson (2022), arXiv:2210.08314: general covariant quantization/mixed-state localization, no rectangle shape calculation.

Self-review: passed. Independent audit: not yet performed.
