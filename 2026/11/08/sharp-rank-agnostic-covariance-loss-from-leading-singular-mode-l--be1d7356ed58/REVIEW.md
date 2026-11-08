# Scientific review: Landweber covariance rank truncation

## Correctness — PASS

The claim follows from (i) the exact noise-propagation covariance in the normal-operator eigenbasis, (ii) a strict single maximum for the scalar filter \(f_K\), (iii) a pairwise ordered-filter inequality, (iv) an eigenvalue counting argument proving the all-rank bound, and (v) a diagonal sharpness family with \(r\) unit modes and one critical mode. A compactness argument using \(f_K(t)/K\le\min\{Kt,(Kt)^{-1}\}\) establishes the asymptotic coefficient. Boundary values \(K=1\), zero normal eigenvalues, ties, and zero best approximation error are covered. Supplementary finite checker tests passed 24,486 assertions; finite tests do not substitute for the proof.

## Originality — PASS, with a priority qualification

The original Landweber spectral filter, propagated covariance formula, leading-normal-eigenmode approximation, and concerns about weak singular directions are present in Abhishek–Holman (2026). The result assessed here is instead the **sharp all-dimension/all-retained-rank competitive factor** for that particular low-rank covariance choice, including its unique critical spectrum and iteration-linear growth. Inspected sections 3.1–3.6, simulations and Appendix 5.1 of the motivating article did not identify this exact comparison. Ito–Jin (2019) analyzes randomized SVD of regularized inverse solutions rather than the same covariance comparison. Gazzola–Sabaté Landman (2020) reviews inverse-problem spectral filtering and regularized Krylov projection. Related published mathematical records were compared at claim and implication level, including a separate Rademacher covariance-diagonal probing analysis; no covering record was identified. This is **not** proof that no historical equivalent exists. Full text of Bardsley's 2018 spectral-filtering chapter was unavailable, leaving a specifically identified residual risk.

## Mathematical value — PASS

The motivating numerical UQ approach needs low-rank approximations to the propagated covariance, yet the normal-operator singular-value order need not be the covariance-eigenvalue order. The result provides a sharp universal bound on the loss from this particular rank-choice mismatch, pinpoints worst-case spectra, and shows the cost can increase linearly in the stopping iteration even though the approximation rank is fixed. This is a complete, natural algorithm-design quantity over all finite dimensions and ranks, rather than a selected numerical instance. It does not suggest that overall uncertainty coverage or reconstruction error deteriorates by the same factor, and it does not compare work or time complexity.

## Limitations and closest sources

Abhishek–Holman, arXiv:2610.00882v1 (2026): original covariance formula, top-normal-mode approximation, stochastic residual correction. Ito–Jin, arXiv:1909.01947v1 (2019): randomized SVD for regularized inverse solutions. Gazzola–Sabaté Landman, DOI:10.1002/gamm.202000017 (2020): spectral regularization background. Bardsley, DOI:10.1137/1.9781611975383.ch2 (2018): relevant chapter not accessible in full. No independent mathematical audit was conducted.

Self-review: passed. Independent audit: not yet performed.
