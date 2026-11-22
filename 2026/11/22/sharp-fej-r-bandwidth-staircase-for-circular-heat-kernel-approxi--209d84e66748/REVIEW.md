# Mathematical review

## Correctness — PASS

The claim and proof use normalized Haar measure and the heat multiplier \(e^{-tk^2}\). Parseval and the explicit Fejér triangle yield an exact adjacent-error difference; a strictly decreasing weighted average gives discrete convexity and excludes nonadjacent ties. Time-monotonicity establishes unique switch times; uniform Euler–Maclaurin and Riemann-sum estimates prove the sharp order and error laws. The first-moment comparison uses \(N\sim t^{-1}\) and a positive quadratic-norm term dominating the Gaussian cross term. All limiting assertions are analytic. `checker.py` returned 1124 finite diagnostics, which test formulas but do not certify infinite quantifiers.

## Originality — PASS (best-knowledge)

The closest literature inspected is Fu–Hou–Wu, arXiv:2210.14720 (2022), giving Fejér multipliers and heat solutions but not their best integer-order \(L^2\) match; Abdullayev–Savchuk, arXiv:2106.08675 (2021), on generalized Fejér positivity and convergence; and Colbrook–Townsend, arXiv:2111.14889 (2021), Section 3.2, on spectral recovery with hat filters. Their statements do not imply the new staircase or optimal heat bandwidth. Related indexed results on optimal positive circular kernels and heat-to-Poisson fits use different objectives and admissible kernels. OEIS A194567 already tabulates the equation's positive root, so that constant alone is not an originality claim. Residual risk: older applied bandwidth-selection literature may contain an equivalent special calculation; no exhaustive historical-priority certification is claimed.

## Value — PASS

This fully classifies the bandwidth choice for a canonical *positive* Fourier approximation family, not just its convergence as order grows. The infinitely many strictly ordered switch times, sharp \(t^{-1/2}\) bandwidth scale, exact limiting squared error, and divergence of the first-moment-based penalty give practical and structural distinctions between approximating a Gaussian smoothing profile and matching a single mode.

## Limitations and closest literature

No claim is made for other spectral tapers, arbitrary nonnegative trigonometric polynomials, other norms, or noisy data. The source comparison is based on identifiable public full texts and indexed findings; independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
