# Scientific assessment

## Correctness — PASS

The fixed diagonal Hermitian matrix, moving orthonormal plane and Gaussian square pencil are explicitly defined. A direct triangular factorization of the reduced pencil identifies the target eigenvalue branch and normalized eigenvector. Gaussian rotational invariance and uniformity of the null direction of a two-row, three-column standard complex Gaussian matrix yield the complex Gaussian-ratio representation. Orthogonality gives the exact identity \((1-d)^2+b^2=1\), reducing the refined angle to a ratio of independent exponentials. Its exact CDF, two moment integrals and asymptotics are elementary and mutually consistent. The supplied checker independently replays direct random pencils, deterministic moment quadrature and the leading small-angle coefficients. It does not substitute numerical sampling for the proof.

## Originality — PASS (qualified)

Shao's source Algorithm 1 and analysis provide high-probability rates for a selected branch, not this exact finite-angle distribution and unconditional mean/RMS coefficients. Nakatsukasa–Tropp Section 6 has an oversampled sketched least-squares eigenproblem rather than this square sketch. Earlier accessible work on another three-dimensional Hermitian plane showed a complex Gaussian-ratio limiting tail and failure of uniform mean-square quadratic rates but explicitly left finite-angle laws and sharp attainable moment rates open. Neither those tail thresholds nor the classical complex Cauchy ratio by themselves imply the present exact \(\varepsilon^2\log(1/\varepsilon)\) mean and \(\varepsilon\) RMS coefficients for this new positive-quotient geometry. Search coverage cannot prove uniqueness; the principal residual risk is an equivalent special-case computation in unindexed numerical linear algebra or complex-ratio literature.

## Value — PASS

High-probability accuracy and unconditional expected error serve different reliability and sample-averaging questions for randomized eigenvalue extraction. The example gives an exact, finite-angle, nonasymptotic risk law, identifies a logarithmic bias inflation, and quantifies a full-order loss in mean-square accuracy relative to deterministic Ritz on the *same* trial plane. The distinction is useful when selecting risk metrics and when interpreting simulations or batched use of square Gaussian projections. The result does not claim a general algorithmic no-go theorem or invalidate published high-probability guarantees.

## Closest literature and residual limitations

N. Shao, arXiv:2604.01037v4, especially the square-compression Algorithm 1, high-probability statements in Section 4, and the explicit pair-selection caveat. Y. Nakatsukasa and J. A. Tropp, SIAM J. Matrix Anal. Appl. 45 (2024), Section 6, uses least-squares embedding and oversampling. The Gaussian ratio step is classical. A separate accessible finite-angle asymptotic study for a different Hermitian plane remains a close prior statement but does not assert this finite-angle CDF or moment constants. Independent literature priority review could discover another formula; the calculations here are independently reconstructible.

Self-review: passed. Independent audit: not yet performed.
