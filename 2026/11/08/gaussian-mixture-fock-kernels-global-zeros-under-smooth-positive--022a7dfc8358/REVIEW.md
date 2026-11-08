# Scientific review: Gaussian-mixture Fock kernel zeros

## Correctness — PASS
Gaussian multiindex moments establish the exact one-variable kernel series in every complex dimension. The factorially scaled Taylor coefficients converge geometrically at rate \(a\), with a limiting prefactor that conflicts with the only possible finite-zero order-one Hadamard factorization. Thus all nontrivial mixtures have infinitely many zeros. For small admixture, an absolutely convergent exponential expansion allows a quantitative half-plane zero exclusion and a Rouché isolation of a simple negative real zero. The resulting lower and upper modulus bounds have the same leading logarithmic term. The complex Hessian of the explicitly normalized potential has eigenvalues computable from a single radial function, yielding uniform strict positivity and uniform smooth convergence.

Independent finite checks in `CHECK.py` compare both kernel representations, exact rational moments, localize the simple negative real zero and test the curvature inequality. These checks are ancillary and do not substitute for the infinite statements proved by the Hadamard, Rouché, and curvature arguments.

## Originality — PASS on inspected evidence
Liu–Wang–Zeng (2026, arXiv:2609.26810), Theorem 1.2 and Proposition 3.4, provide general pointwise upper and near-diagonal lower estimates; they do not imply global zero-freeness or the logarithmic escape law. The fully inspected earlier Marzo–Ortega-Cerdà (2008, arXiv:0810.0388) theorem concerns upper estimates for one-dimensional weighted Fock kernels. The fully inspected Zeytuncu (2010, arXiv:1009.2806) paper exhibits zeros for comparable radial weights on the bounded disk, not for smooth nearly quadratic entire Fock weights, and gives no escape constant for Gaussian mixtures. Nearby available published findings concern weighted-disk kernel zeros, Fock extremal radii or Fock Toeplitz operators rather than this two-Gaussian kernel family.

The 2026 Hu–Lv–Schuster paper on weighted-Fock kernel estimates is a relevant inaccessible comparison: its abstract was examined, but full text was not obtained through the available authorized access path. An older equivalent statement under alternate entire-function terminology cannot be ruled out. These are genuine publication-priority risks, not verified covering results.

## Value — PASS
The global Lu Qi-Keng property is a natural spectral geometry question distinct from positive diagonal and near-diagonal kernel estimates. The complete two-Gaussian mixture family shows that zero-freeness fails immediately away from either Gaussian endpoint; the first-zero distance has a sharp, parameter-dependent logarithmic scale. Uniform \(C^m\) and strict-curvature control demonstrate that the instability is not caused by a rough or degenerating weight. This gives a quantitative boundary to extending local weighted-Fock kernel estimates into global nonvanishing principles.

## Scope and limitations
No exact nearest-zero location beyond the leading logarithmic law, and no angular distribution or full real-zero classification, are claimed. The real zero's two-term expansion is only as the faster-decaying Gaussian weight tends to zero. The infinite-zero result holds for all mixing parameters. Full literature priority and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
