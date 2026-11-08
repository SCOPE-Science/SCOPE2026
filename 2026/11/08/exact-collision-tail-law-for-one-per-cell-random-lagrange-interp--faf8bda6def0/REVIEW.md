# Self-review

## Correctness — PASS

The exact domain is fixed \(m\ge2\), fixed \(z\in[0,1]\), and independent uniform samples from their respective full-width equal cells. The Lagrange coefficients are well-defined almost surely. The proof identifies all singular faces, uses the exact triangular probability of a shared-boundary collision, derives the residue pair \((-C_i,+C_i)\), and justifies adding the face probabilities through a uniform inverse-minimum-gap bound and negligible intersections. The factor \(m^2\), the Euclidean \(\sqrt2\) residue, and the resulting product-integral tail constant were checked independently. Strict positivity, the two-node midpoint exception, and moment implications follow as written. The closed three-node coefficient was verified analytically and by independent quadrature; seeded numerical checks serve only as diagnostics, not proofs.

## Originality — PASS (with publication-precedence risk)

The closest inspected random interpolation theorem is Dell'Accio–Sommariva–Vianello (arXiv:2303.14074): its almost-sure unisolvency does not constrain inverse-weight moments. Xu–Narayan (arXiv:2101.04043) establish high-probability norming after oversampling, not exactly one sample per cell with a sharp fixed-degree tail. Shen–Serkh (arXiv:2212.10519) analyze deterministic-node numerical conditioning and backward error, whereas the present statement computes the probability of rare random collisions. Occorsio–Themistoclakis (arXiv:2008.00240) analyze filtered interpolation at fixed Chebyshev nodes. Related publicly indexed results for cubic Lagrange range violations and three-knot spline positivity are about bounded deterministic sampled data, rather than stochastic interpolation coefficient tails. No inspected statement implies the exact constant or the full moment classification. The strongest remaining uncertainty is specialist research on random perturbed grids or negative moments of inverse Vandermonde matrices; the checked evidence does not establish comprehensive publication uniqueness.

## Value — PASS

Random nodal interpolation is almost surely solvable but may have infinite expected noise amplification. The claim supplies a sharp *exact* tail constant at every fixed degree, identifies a precise two-node exception, proves failure of unconditional mean-square stability for all higher-degree full-cell designs, and evaluates a nontrivial logarithmic constant at the smallest higher-degree case. It is a motivated interpolation-design boundary, not a substitution into a convergence bound or an arbitrary numerical table. The theorem motivates keeping jittered nodes a positive distance from shared cell boundaries or regularizing the interpolation map. It does not address the approximation error of noiseless smooth functions or higher-dimensional interpolation.

Self-review: passed. Independent audit: not yet performed.
