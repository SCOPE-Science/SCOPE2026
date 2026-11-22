# Scientific review: sharp finite-band positivity frontier for axially tilted spherical heat covariance

## Correctness — PASS

The statement concerns the double-compressed operator \(P_LT_{t,\varepsilon}P_L\), not a separately truncated kernel multiplied by the latitude factor. With normalized spherical harmonics, latitude multiplication has the exact adjacent coefficient \(a_{\ell m}=\sqrt{((\ell+1)^2-m^2)/((2\ell+1)(2\ell+3))}\), and heat diagonal ratios produce the exact multiplier \(2\cosh(t(\ell+1))\). Congruence by the positive heat-multiplier square root reduces the finite-band positive-semidefiniteness test to the self-adjoint Jacobi block spectrum. Perron comparison makes the zonal block strictly dominant and proves both the sharp cutoff and one-dimensional critical nullspace. Disjoint high-degree negative two-mode subspaces prove infinite negative inertia at each nonzero tilt. After edge reflection, the normalized Jacobi matrices converge in operator norm to a compact geometric Jacobi operator with \(O_t(L^{-3})\) error. The exact last-edge amplitude then yields the relative \(-1/(8L^2)\) term. The embedded numerical checker corroborates finite instances. The proof does not infer an infinite theorem from numerical checks.

## Originality — PASS, with stated historical uncertainty

The 2021 Buhmann–Jäger preprint (full article inspected) develops axially symmetric harmonic coefficient-matrix criteria but not the present explicit heat-band threshold or its compact geometric-Jacobi asymptotic. The published 2026 Poisson axial-tilt result (full result inspected) instead has degree-independent normalized adjacent weights, a nonzero full-kernel positivity interval, and finite-band Legendre-zero cutoffs. Its theorem does not imply the heat-band boundary constant or \(-1/8\) correction. The qualitative nonpositivity of the fully tilted heat kernel is already accessible through general neighboring-eigenvalue-ratio arguments and is not claimed alone as new. Other published positive-definiteness and geometric-Jacobi literature was searched using the exact object, aliases, and candidate reductions, without identifying equivalent or stronger coverage. A 2024 Emery–Jäger–Porcu covariance article was available by abstract only; it remains a concrete historical-priority uncertainty. These comparisons establish a best-knowledge assessment, not a proof of global priority.

## Mathematical value — PASS

Finite harmonic truncation is a natural construction in spherical covariance modeling, but finite-band positive-semidefiniteness can mask a genuine infinite-dimensional failure. The exact cutoff and its exponentially small asymptotics give a quantitative resolution requirement, while the compact geometric-Jacobi constant captures the nonuniform high-frequency coupling that the corresponding Poisson law misses. The universal relative \(-1/8\) correction distinguishes the precise boundary from a coarse exponential estimate. This is an exact nontrivial spectral frontier for a motivated family, not an arbitrary finite test or a routine derivative of the qualitative indefinite-kernel observation.

## Limits and risk

The spectral asymptotic holds at fixed \(t>0\) only; no uniform joint scaling is proved. Full historical priority, particularly around geometric weighted Jacobi matrices, has not been independently certified. The related 2024 space-time axial covariance article was inspected through bibliographic and abstract material but its complete text was unavailable. The bundled numerical checks do not replace the analytic proof.

Self-review: passed. Independent audit: not yet performed.
