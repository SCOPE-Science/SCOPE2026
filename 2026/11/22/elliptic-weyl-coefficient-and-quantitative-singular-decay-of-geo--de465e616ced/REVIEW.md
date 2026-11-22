# Review of the quantitative singular-value law

## Correctness — PASS

On the exact Hilbert space with weights \(q^j\), conjugation turns the Cesàro matrix into \(D(I-rS)^{-1}\) with \(r=\sqrt q\). The proof gives a uniform finite-band counting estimate by cutting the row-weighted Toeplitz matrix into blocks, comparing each block with a circulant, and estimating grid counts using the at-most-\(2M\) crossings of the squared trigonometric symbol. Its error is \(O_r((M+1)t^{-1/2})\); choosing \(M\) logarithmically suppresses the geometric tail to \(O(t^2)\). The resulting counting remainder is inverted to the stated individual singular-value remainder. The argument controls the infinite tail and all block boundaries, including finite rank cross-cuts. The elliptic integral, Schatten cutoff, and weak-trace limit are derived, not inferred from finite experiments. The independent finite-section checker passes 80 assertions, but is not an infinite proof.

## Originality — PASS, with residual priority risk

Albanese, Bonet and Ricker (2015; DOI 10.1017/S1446788715000221; inspected author manuscript) establish geometric-weight compactness and spectral eigenvalues but not the individual singular-value asymptotic or its quantitative error. Zizler, Zuidwijk, Taylor and Arimoto (2002; DOI 10.1137/S089547989834915X; examined full-text method) treat finite band Toeplitz eigenvalue distributions; their theorem neither identifies the diagonally weighted infinite Cesàro singular coefficient nor supplies the logarithmically controlled singular-value remainder. Related research records for power-decaying Rhaly rows, finite Cesàro matrices, and Hardy-space point-mass averaging concern distinct operators or scaling regimes, so their claims do not imply the displayed formula. Standard general weighted-Toeplitz spectral theorems might yield an unquantified leading Weyl law; the priority risk of a stronger, unlocated quantitative theorem remains.

## Value — PASS

The 2015 work poses a natural boundary between compactness/spectrum and quantitative approximation numbers. The coefficient \(\kappa(\sqrt q)\) is a concrete, nonconstant elliptic spectral invariant, in contrast to the weight-independent eigenvalues \(1/j\). The sharp exponent-one Schatten cutoff, exact logarithmic singular-mass coefficient, and a rate for individual singular values provide useful quantitative stability information on a classical averaging operator, rather than a routine finite-table restatement.

## Scientific scope and limitations

The geometric parameter is fixed strictly below one. No claim is made about the noncompact \(q=1\) boundary, optimal higher-order asymptotics, or general weights. Novelty is based on inspected accessible primary sources and indexed comparisons, not a proof that no uncatalogued equivalent exists.

Self-review: passed. Independent audit: not yet performed.
