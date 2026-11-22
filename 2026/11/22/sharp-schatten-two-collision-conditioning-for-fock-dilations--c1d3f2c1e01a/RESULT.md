# Sharp Schatten-two collision conditioning for Fock dilations

## Finding

Consider the classical complex Gaussian Fock Hilbert space \(\mathcal F^2_\alpha(\mathbb C)\) for any \(\alpha>0\). For \(|b|<1\), write \(C_bf(z)=f(bz)\). For distinct slopes \(b_1,\ldots,b_N\) in the open unit disk, define their *optimal squared Hilbert–Schmidt comparison coefficient*
\[
\kappa(b_1,\ldots,b_N)=\inf_{c\in\mathbb C^N\setminus\{0\}}
\frac{\|\sum_{j=1}^N c_j C_{b_j}\|_{\mathcal S_2}^2}
{\sum_{j=1}^N |c_j|^2\|C_{b_j}\|_{\mathcal S_2}^2}.
\]

**Collision theorem.** Fix any integer \(N\ge2\), any center \(a\in\mathbb C\) with \(0<|a|<1\), and any pairwise distinct directions \(\zeta_1,\ldots,\zeta_N\in\mathbb C\). For real \(\varepsilon>0\) sufficiently small, put \(b_j(\varepsilon)=a+\varepsilon\zeta_j\) and
\[
w_j=\prod_{k\ne j}(\zeta_j-\zeta_k)^{-1}.
\]
Then all slopes are distinct, nonzero, and strictly inside the unit disk, and
\[
\boxed{\lim_{\varepsilon\downarrow0}
\frac{\kappa(b_1(\varepsilon),\ldots,b_N(\varepsilon))}{\varepsilon^{2N-2}}
=\frac{1}{(1-|a|^2)^{2N-2}\sum_{j=1}^N|w_j|^2}.}
\]
This leading coefficient is strictly positive. Every choice of unit minimizing coefficient vectors converges, after suitable phase corrections, to \((w_1,\ldots,w_N)/(\sum_j|w_j|^2)^{1/2}\); more precisely, their distance from this complex line tends to zero.

The exponent cannot be improved, even at a fixed interior center. For an additional exact formula, let \(b_j=\varepsilon\exp(2\pi i j/N)\), \(0\le j<N\), with \(0<\varepsilon<1\). Then
\[
\boxed{\kappa(b_0,\ldots,b_{N-1})
=\frac{N(1-\varepsilon^2)\varepsilon^{2N-2}}{1-\varepsilon^{2N}}.}
\]
This last expression holds at center zero, where all the displayed slopes remain nonconstant.

## Assumptions and scope

All spaces and coefficients are complex; \(\mathcal S_2\) denotes the Hilbert–Schmidt ideal. The parameter \(\alpha\) is an arbitrary fixed positive real number. The collision is at fixed \(a\) in the open disk, not a simultaneous approach to the unit circle. Directions are fixed, pairwise distinct complex numbers, and \(\varepsilon\downarrow0\) along positive real values. The result concerns unweighted composition dilations and arbitrary complex *scalar* linear-combination coefficients, not general analytic weights or general Schatten exponents.

## Proof

**1. Reduction to a normalized Hardy Gram matrix.** The Fock monomials
\(e_n(z)=\alpha^{n/2}z^n/\sqrt{n!}\), \(n\ge0\), form an orthonormal basis and satisfy \(C_b e_n=b^n e_n\). Therefore, for any \(|b_j|<1\),
\[
\left\|\sum_j c_j C_{b_j}\right\|_{\mathcal S_2}^2
=\sum_{n=0}^\infty\left|\sum_jc_jb_j^n\right|^2
=\sum_{i,j}\overline{c_i}K_{ij}c_j,
\qquad K_{ij}=\frac1{1-\overline{b_i}b_j}.
\]
In particular \(\|C_{b_j}\|_{\mathcal S_2}^2=(1-|b_j|^2)^{-1}\). Set \(D=\operatorname{diag}((1-|b_j|^2)^{-1})\) and \(G=D^{-1/2}KD^{-1/2}\). This Hermitian matrix is positive definite because distinct Vandermonde columns \((1,b_j,\ldots,b_j^{N-1})\) are independent, and the optimal comparison coefficient is exactly \(\kappa=\lambda_{\min}(G)>0\).

**2. Exact dual interpolants.** In the classical Hardy space \(H^2(\mathbb D)\), let \(k_b(z)=(1-\overline b z)^{-1}\). The vectors \(k_{b_j}\) have a Gram matrix equal to the transpose of \(K\), hence their Gram matrix has the same positive eigenvalues. For each \(j\), define
\[
L_j(z)=\left(\prod_{k\ne j}\frac{z-b_k}{b_j-b_k}\right)
\left(\prod_{k=1}^N\frac{1-\overline{b_k}b_j}{1-\overline{b_k}z}\right).
\]
Its denominator is the product of \(N\) distinct linear Hardy-kernel denominators and its numerator has degree at most \(N-1\). Partial fractions therefore show \(L_j\in\operatorname{span}\{k_{b_1},\ldots,k_{b_N}\}\). The interpolation equations \(L_j(b_i)=\delta_{ij}\) make these functions the unique biorthogonal family. The matrix \((\langle L_i,L_j\rangle_{H^2})_{i,j}\) is consequently the inverse of the transposed kernel Gram matrix. In particular, it has exactly the eigenvalues of \(K^{-1}\); the difference in transpose convention does not affect eigenvalues.

**3. A rank-one limit of the inverse.** Put \(r=|a|\) and let \(B_a(z)=(z-a)/(1-\overline a z)\), an inner Blaschke factor. Inserting \(b_j=a+\varepsilon\zeta_j\) into the exact interpolant gives, in Hardy norm,
\[
\varepsilon^{N-1}L_j(z)\longrightarrow
(1-r^2)^Nw_j\frac{(z-a)^{N-1}}{(1-\overline a z)^N}
=(1-r^2)^Nw_j\frac{B_a(z)^{N-1}}{1-\overline a z}.
\]
This convergence is in \(H^2\), not merely pointwise: for all sufficiently small \(\varepsilon\), the rational denominators have poles outside a fixed disk of radius strictly greater than one, and converge uniformly on that larger closed disk. Multiplication by the inner function \(B_a^{N-1}\) preserves Hardy norm, so
\[
\left\|\frac{B_a^{N-1}}{1-\overline a z}\right\|_{H^2}^2
=\frac1{1-r^2}.
\]
Thus \(\varepsilon^{2N-2}K^{-1}\) converges in finite-matrix operator norm to a rank-one Hermitian matrix whose nonzero eigenvalue is
\((1-r^2)^{2N-1}\sum_j|w_j|^2\). Conjugation by \(D^{1/2}\), whose entries approach \((1-r^2)^{-1/2}\), gives
\[
\varepsilon^{2N-2}G^{-1}\longrightarrow
(1-r^2)^{2N-2}\,ww^*,
\]
where \(w=(w_1,\ldots,w_N)^{\mathsf T}\). Taking the largest eigenvalue of the inverse and then reciprocals yields the stated limit. Because the rank-one limit has a simple positive eigenvalue, its top unit eigenvector converges up to phase to \(w/\|w\|_2\); these are exactly the minimizers for \(G\), transformed back to scalar coefficients by \(D^{-1/2}\), which approaches a common multiple of the identity. This proves the coefficient-direction assertion.

**4. Exact symmetric family.** For \(b_j=\varepsilon\omega^j\), \(\omega=e^{2\pi i/N}\), all diagonal entries of \(D\) equal \((1-\varepsilon^2)^{-1}\), and
\[
G_{ij}=\frac{1-\varepsilon^2}{1-\varepsilon^2\omega^{j-i}}.
\]
Expanding each denominator as a geometric series and diagonalizing this circulant matrix by the \(N\)-point Fourier transform gives its entire eigenvalue multiset
\[
\left\{\frac{N(1-\varepsilon^2)\varepsilon^{2s}}
{1-\varepsilon^{2N}}:s=0,\ldots,N-1\right\}.
\]
For \(0<\varepsilon<1\), the smallest corresponds to \(s=N-1\), proving the claimed exact identity and the optimal exponent.

## Verification

The standalone `CHECK.py` computes the normalized Hardy Gram eigenvalues with 85-digit working precision and verifies the exact Fourier eigenvalue formula for regular root configurations, the general collision-limit trend for nonsymmetric complex directions, positivity of the smallest eigenvalue, and alignment of the weak eigendirection with barycentric weights. It reports `FOCK_DILATION_SZego_COLLISION_CHECK_OK 88` when its 88 finite assertions pass. Run using `python CHECK.py` with the independently available `mpmath` package. These checks are supplementary; the proof above establishes the assertions for all permitted integer dimensions and parameters.

## Relationship to prior work

Lin, Lu, Yang and Zu (2026, Theorem 1.3) establish Schatten-class inheritance and two-sided Schatten comparisons for any fixed family of pairwise distinct nonconstant Fock composition symbols. Their constants are allowed to depend on the fixed symbols; their theorem and proof do not calculate the optimally sharp *coalescence* rate as those symbols approach each other. The present theorem specializes to constant multipliers and Hilbert–Schmidt norm to determine that degenerating sharp coefficient, its asymptotically extremal scalar combination, and an exact symmetric benchmark.

Choe, Izuchi and Koo (2010) establish qualitative Schatten non-cancellation for sums of two Fock composition operators; the readily accessible abstract does not identify an equivalent sharp multi-symbol collision coefficient. Earlier general Fock–Sobolev linear-combination results also address different quantitative questions. Standard Hardy-kernel interpolation and Blaschke inner-factor identities are used explicitly rather than claimed as new.

## Limitations

This does not extend the displayed constant to nonlinear composition symbols, analytic coefficient multipliers, or Schatten exponents other than two. No uniform statement is made as the collision center itself approaches the unit circle or as the number of summands varies. The rank-one limit specifies the leading asymptotic but no full higher-order expansion. A full-text priority comparison with some older journal articles on linear sums of Fock composition operators remains outstanding; bibliographic uniqueness is not asserted as a theorem.

## References

1. Z. Lin, Y. Lu, R. Yang and C. Zu, *Finite sums of weighted composition operators on the Fock space*, arXiv:2611.19948 (first posted 2026-11-15), especially Theorem 1.3 and Section 5. https://arxiv.org/abs/2611.19948
2. B. R. Choe, K. H. Izuchi and H. Koo, *Linear sums of two composition operators on the Fock space*, Journal of Mathematical Analysis and Applications 369 (2010), 112–119. https://doi.org/10.1016/j.jmaa.2010.02.029
3. H. R. Cho, B. R. Choe and H. Koo, *Linear combinations of composition operators on the Fock-Sobolev spaces*, Potential Analysis 41 (2014), 1223–1246. https://doi.org/10.1007/s11118-014-9417-6
