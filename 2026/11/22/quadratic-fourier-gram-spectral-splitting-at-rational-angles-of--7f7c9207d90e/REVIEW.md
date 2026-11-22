# Scientific assessment

## Correctness — PASS

The finding uses a fixed positive geometric sampling measure and finite Fourier coefficient dimension. The moment formula is a direct geometric-series identity. At a primitive rational angle, the rank is exactly the denominator \(L\), since the limiting orbit has exactly \(L\) positive-mass support points and its first \(L\) monomials interpolate all residue values. The null polynomials are exactly \((z^L-1)R\) of degree less than \(L+K\); for \(K\le L\), their coefficient norm is twice that of \(R\). The nonstandard step is an explicit Schur-complement perturbation at this singular Gram matrix. Its effective form is the conditional variance of the orbit index given its residue class. Geometric conditional weights yield the factor \(L^4p^L/(1-p^L)^2\), and Fourier interpolation identifies the \(K\)-by-\(K\) positive moment matrix. This proves each eigenvalue expansion with positive leading coefficient. Orthogonality of the discrete Fourier matrix gives the fully explicit doubled-band spectrum and sharp sampling condition number. A separately replayed NumPy checker passed 768 assertions, but the analytic proof, not finite testing, establishes the theorem for all parameters.

## Originality — PASS (best-knowledge, with residual risk)

Zhedanov (2020, arXiv:2010.10321), Sections 2–4, contains the weighted circle measure, its moments, OPUC and norms, and finite support at root-of-unity rotation. Its explicit polynomial norm already controls determinant/product collapse but does not supply the individual eigenvalue splitting for every \(1\le K\le L\) or the matched soft/hard eigenvalue spectra and condition-number constant. Batenkov–Diederichs–Goldman–Yomdin (arXiv:1909.01927, especially Theorems 2.2–2.3) analyze finite clustered-node Fourier Vandermonde matrices with order estimates and bounds, rather than this infinite weighted orbit and exact spectral coefficients. Kunis–Nagel (DOI:10.1007/s11075-020-00974-x) likewise give condition bounds for finite near-collision node sets. Semantic database searches for rational rotations, geometric orbit moments, Toeplitz Gram spectra, and root-of-unity splitting returned no known statement directly covering the full claimed theorem. Classical analytic perturbation methods are credited as techniques, not new theorems. Historical priority remains provisional, especially relative to older OPUC or weighted Vandermonde analyses.

## Mathematical value — PASS

The denominator of a rational rotation is a natural and sharp sampling-rank boundary. Moving through that boundary creates as many weak directions as redundant polynomial degrees, but their strengths are not captured by the existing moment determinant. The theorem determines the *entire* leading spectrum, its positive coefficients and arithmetic parameter dependence, and a completely explicit paired spectrum at doubled bandwidth, with an exact condition-number divergence coefficient. This supplies quantitative stability information for the first over-resolved geometric orbit beyond what a rank test, norm product, or generic conditioning order provides.

## Limitations and closest literature

The statement is local in angle, fixed in dimension and weight, and restricted to \(1\le K\le L\). It is not a uniform or high-bandwidth theorem, and does not classify the higher-order weak modes beyond doubled bandwidth. The primary literature cited above is the closest inspected context. The numerical checker is finite and cannot establish the asymptotic theorem independently.

Self-review: passed. Independent audit: not yet performed.
