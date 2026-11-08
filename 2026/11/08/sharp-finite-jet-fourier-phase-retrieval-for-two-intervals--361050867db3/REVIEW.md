# Scientific review: finite-jet Fourier phase retrieval for two intervals

## Correctness — PASS

The proof expands the squared Fourier transform of two arbitrary separated intervals through order four. The exact coefficient identities give a positive invariant \(q=ab\,g(g+a+b)\) and reduce the unknown length product \(r=ab\) to a quadratic with exactly one positive root. The gap then follows from a positive square root, and the remaining exchange of the lengths is precisely reflection. The fourth-order attainable-jet inequality follows from strict monotonicity in \(r\). Varying \(r\) at fixed area and \(q\) supplies a continuum of order-two ambiguities, proving minimality. Exact rational double-moment integration and direct Fourier evaluations in `CHECK.py` independently corroborate the identities. A computer test alone cannot establish the all-real-parameter claim; the displayed algebra and monotonicity do.

## Originality — PASS relative to inspected sources

Xia and Xu, *Fourier Phase Retrieval for Finite Unions of Intervals* (arXiv:2606.19855, first submitted 2026-06-18), Theorems 1.2–1.3, prove full-magnitude uniqueness and stability for at most two intervals. Their Section 2 first infers the maximal endpoint from the entire trigonometric spectrum before equating further coefficients. Equality of three Taylor coefficients is much weaker than equality of the full magnitude. The inspected theorem and its proof do not present or imply the exact order-four finite-jet inversion, its minimality, or the sharp feasible-jet inequality. Grohs–Koppensteiner–Rathmair, *Phase Retrieval: Uniqueness and Stability* (SIAM Review, 2020), discusses general full-data ambiguities; it does not supply the finite-jet result in its inspected overview. Searches for alternate phrases involving spectral moments, covariograms and Taylor derivatives yielded no direct equivalent. This is a best-knowledge originality judgment, not a guarantee of publication priority. Residual risk: an equivalent low-order-moment formula could appear under another terminology in older inverse-moment literature.

## Mathematical value — PASS

Whole Fourier intensity is an infinite continuum of observations. Proving that precisely three natural local Taylor measurements suffice for every two-interval indicator gives an explicit minimal finite-data theorem, rather than simply rephrasing the known full-data uniqueness. The analytic inverse supplies both interval lengths and the gap; the exact feasible-jet boundary classifies all realizable measurements and detects the equal-length locus. The loss of identifiability at vanishing gap is also mathematically transparent. No assertion is made about numerical stability of estimating derivatives from noisy finite-band samples or about unions of three or more intervals.

Self-review: passed. Independent audit: not yet performed.
