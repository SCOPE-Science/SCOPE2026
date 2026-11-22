# Self-review

## Correctness — PASS

The normal-form eigenvalues and eigenvectors of the Dirichlet tridiagonal matrix are explicit. Strictly decreasing affine-exponent crossing times give unique modal dominance on each comparison interval. In the large-lag limit, the four successive normalized snapshots around each \(s_j\) converge to \(v_{j+1},v_{j+1},v_j,v_j\); the least-squares sine identity yields the claimed \(0,1,0\) residual pattern for all indices simultaneously at sufficiently large finite lag. Absolute-error monotonicity follows by applying the heat contraction to the preceding least-squares residual, with strictly positive defect for all finite times. The standard-library check passed 273 assertions. Numerical checks are not the infinite proof.

## Originality — PASS, with risks

Full text was examined for Han, Xiu and Zikatanov, arXiv:2611.19040v1, especially Theorem 7, eq. (34), and Corollary 9, eq. (39). They give *absolute* closure guarantees rather than the relative one-delay time-profile. Full published RESULTS for *Arbitrarily many Fourier-ratio peaks under periodic heat flow* were compared: its \(\ell^1/\ell^2\) ratio differs from the consecutive-time projection angle and does not logically yield the latter. Standard spectral angle bounds at a single burn-in cannot produce the separated extremal sequence. The shared exponential crossing method is not claimed to be new. Some semigroup-angle literature may be unindexed, so exhaustive priority is unproved.

## Value — PASS, with limits

The result supplies a concrete boundary to interpreting contractive absolute error after burn-in as reliable normalized forecasting: arbitrarily many near-total relative failures arise despite strictly decreasing absolute defect. This directly informs how one-delay prediction quality should be assessed. The construction requires nonlocal, lag-dependent, highly imbalanced modal weights, and does not demonstrate common sensor behavior, noisy stability, or higher-memory failure.

Self-review: passed. Independent audit: not yet performed.
