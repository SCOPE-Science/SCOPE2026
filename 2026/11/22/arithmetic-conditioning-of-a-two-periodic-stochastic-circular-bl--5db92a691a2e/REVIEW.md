# Scientific review

## Correctness — PASS

The theorem fixes the cyclic operator, sample length, norm, and parameter ranges explicitly. Splitting even/odd sites by the unitary Fourier transform yields the stated \(2\times2\) matrices with determinant \((1-a)(1-b)-ab\cos^2(\pi k/q)\). Multiplication by the Chebyshev product yields the exact signed determinant, and rank-one resonant blocks give nullity exactly two. The norm is attained by the zero-frequency block because the nonnegative singular-value representation is monotone in the modulus of the off-diagonal coefficient. Near either simple zero, the small singular value is the determinant divided by the nonzero singular value, yielding the constant in \(q/\|q\alpha\|_{\mathbb Z}\). Standard continued-fraction and Liouville approximation facts give the arithmetic consequences. The standalone code performed 242 reproducibility assertions, including independently constructed dense matrices and exact-rational determinants and ranks; finite tests are not used as the infinite proof.

## Originality — PASS (qualified)

González del Cueto and Guevara Vasquez, *Fast circular convolution with periodic kernels* (arXiv:2611.16144v1), derive Fourier-block representation and inversion for general periodically varying convolution kernels; its accessible full text was examined in the relevant definitions, spectral/inversion results and applications. This supplies the starting machinery but not the exact sine-square determinant, rational-grid nullity census or sharp small-divisor conditioning constant for this stochastic three-tap family. Closest published records concern either Diophantine conditioning of Gaussian interference measurements, inversion by two full-resolution two-dimensional stencils, dihedral convolution, or two-periodic cubic spline collocation; none implies the present formula after matching objects and assumptions. Published circular-deconvolution stability papers by Linzer and Yalamov are relevant, but only accessible abstracts were reviewed and they discuss transform-algorithm stability. Neither historical uniqueness nor human priority has been certified.

## Value — PASS

This is a natural deconvolution inverse-stability question for a minimal positive, mass-preserving, spatially varying point-spread function. The theorem resolves finite-grid identifiability and sharp condition-number growth in the same family; rational, badly approximable and Liouville phases exhibit qualitatively distinct behavior even though their row-stochastic stencils have the same local support. The exact leading constant quantifies worst-case noise amplification and can benchmark regularization or discretization choices. It is not an average-case image-recovery prediction and does not claim that the recent general FFT algorithm is inaccurate.

## Closest literature and limitations

Primary source: F. González del Cueto and F. Guevara Vasquez, arXiv:2611.16144v1, first public 2026-11-12. Earlier circular deconvolution stability papers: E. Linzer, SIAM J. Numer. Anal. (1992), DOI 10.1137/0729085; P. Y. Yalamov, SIAM J. Matrix Anal. Appl. (2000), DOI 10.1137/S0895479899351052 (abstract comparisons only). Related periodic tridiagonal work: A. Dyachenko and M. Tyaglov, arXiv:2109.10771 (abstract comparison). Earlier equivalent spectral or small-divisor derivations could exist in unpublished or unindexed sources; the displayed result is not an externally certified priority claim.

Self-review: passed. Independent audit: not yet performed.
