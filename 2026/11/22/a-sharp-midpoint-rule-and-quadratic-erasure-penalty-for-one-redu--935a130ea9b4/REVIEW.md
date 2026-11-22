# Scientific review

## Correctness

PASS. The original sample rows form an orthonormal basis, giving a two-outlier Gram spectrum after any original-row erasure. A geometric-series identity reduces the worst row overlap to one elementary trigonometric expression for each parity. Strict derivative signs yield the unique midpoint optimum for every integer \(N\ge2\), and a direct Gram calculation proves the comparison with free regridding. The standalone checker independently confirms 6,930 finite matrix/eigenvalue/optimizer assertions; the analytic proof, not those computations, handles the unbounded dimension.

## Originality

PASS, best-knowledge. Exact row-swap formulas are elementary linear algebra, but the complete minimax location, parity-dependent sharp values, and quadratic-versus-linear erasure penalty under a frozen critical Fourier grid are not statements of the inspected results. Yu–Townsend's full treatment of unevenly spaced samples provides nonuniform Fourier bounds and oversampling theory, while Kunis–Nagel–Strotmann and Kunis–Nagel treat different Vandermonde separation problems. Published erasure-robust frame theory is broader in its goals but was not found to imply this particular geometric optimum. Historical priority remains uncertain without a fully exhaustive search of obscure frame-design literature.

## Value

PASS. Exactly one extra sample is the minimal redundancy enabling recovery from any single known erasure. The placement and sharp worst-noise amplification are therefore a natural exact interpolation-design invariant, not an arbitrary slice. The result proves a substantial \(N\)-factor stability penalty from freezing the original sampling grid, quantifying a practical mathematical tradeoff between adding one measurement and redistributing all measurements.

## Closest literature and limitations

Yu and Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature* (2022), arXiv:2202.04722; Kunis, Nagel and Strotmann, *Multivariate Vandermonde matrices with separated nodes on the unit circle are stable* (2021), arXiv:2103.08167; Kunis and Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes* (2020), DOI:10.1007/s11075-020-00974-x. Only consecutive Fourier frequencies, equal-weight samples, one extra sample and one erasure are included. A possible unindexed equivalent result remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
