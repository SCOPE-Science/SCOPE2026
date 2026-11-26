# A complete first-order angle-sign law for hemispherical random directions

## Finding
Fix an integer \(k\ge3\). Let \(X_1,\ldots,X_k\) be independent uniform-surface-area points in the closed hemisphere \(H_d=\{x\in\mathbb S^{d-1}:x_1\ge0\}\subset\mathbb R^d\), with \(d\to\infty\). For each pair \(i<j\), choose a sign \(s_{ij}\in\{-1,+1\}\), and write \(m=\binom{k}{2}\). Then, **simultaneously for every prescribed pattern of acute and obtuse origin angles**, 
\[
\Pr\bigl(s_{ij}\langle X_i,X_j\rangle>0\ \text{for all }i<j\bigr)
=2^{-m}\left[1+\frac{4}{\pi\sqrt{2\pi d}}\left(\sum_{i<j}s_{ij}+\sum_{i<j<\ell}s_{ij}s_{i\ell}s_{j\ell}\right)+O_k(d^{-1})\right].
\]
The error is uniform over the finite set of sign patterns for each fixed \(k\). The two order-\(d^{-1/2}\) contributions have **exactly the same coefficient**: one counts signed edges (the hemispherical bias), and the other signed triangles (the intrinsic dependence of spherical Gram entries). Other edge configurations do not enter this first correction.

In particular, the probability of an entirely pairwise-acute configuration is
\[
2^{-\binom{k}{2}}\left[1+\frac{4}{\pi\sqrt{2\pi d}}\left(\binom{k}{2}+\binom{k}{3}\right)+O_k(d^{-1})\right].
\]
For \(k=3\), the six patterns having at least one positive and at least one negative edge each have probability \(1/8+O(d^{-1})\), whereas all-acute and all-obtuse configurations have opposite explicit order-\(d^{-1/2}\) deviations from \(1/8\).

## Assumptions and scope
The cap is a **fixed exact hemisphere** for each dimension, with probability measure proportional to the standard surface area. Points are independent, and their number \(k\) is fixed while \(d\) tends to infinity. Inner products are measured in the ambient Euclidean space and are zero with probability zero; therefore strict and weak sign conditions have equal probabilities. The result holds for all sufficiently large \(d\) depending on \(k\); the asymptotic statement does not concern a growing number of sampled points or a cap of another radius.

## Proof
**1. Gaussian hemisphere representation.** For \(1\le i\le k\), let \(G_{i1},\ldots,G_{id}\) be independent standard normal variables, and set \(V_i=(|G_{i1}|,G_{i2},\ldots,G_{id})\). Then \(X_i=V_i/\|V_i\|\) is uniform on \(H_d\); normalization does not change any pairwise sign. Put \(n=d-1\), \(U_i=|G_{i1}|\), \(H_{ij}=U_iU_j\), and for \(2\le r\le d\) define \(Z_{r,ij}=G_{ir}G_{jr}\). The vector \(W_n=n^{-1/2}\sum_{r=2}^d (Z_{r,ij})_{i<j}\in\mathbb R^m\) is independent of \((H_{ij})_{i<j}\), and each sign event is exactly
\[
s_{ij}\left(W_{n,ij}+\frac{H_{ij}}{\sqrt n}\right)>0.
\]

**2. A joint density expansion for Gaussian Gram entries.** For a vector \(t=(t_{ij})_{i<j}\), define a real symmetric \(k\times k\) matrix \(T(t)\) by \(T_{ii}=0\) and \(T_{ij}=t_{ij}\) for \(i\ne j\). A Gaussian quadratic-form integral gives the **exact** characteristic function of one \(Z_r\):
\[
\mathbb E e^{\mathrm i\sum_{i<j}t_{ij}Z_{r,ij}}=\det(I-\mathrm i T(t))^{-1/2}.
\]
Since \(\operatorname{tr}T(t)^2=2\sum_{i<j}t_{ij}^2\) and \(\operatorname{tr}T(t)^3=6\sum_{i<j<\ell}t_{ij}t_{i\ell}t_{j\ell}\), its rescaled \(n\)-fold product has, near the origin,
\[
\log\mathbb E e^{\mathrm i t\cdot W_n}
=-\frac12\|t\|^2-\frac{\mathrm i}{\sqrt n}\sum_{i<j<\ell}t_{ij}t_{i\ell}t_{j\ell}+O_k(\|t\|^4/n).
\]
Writing \(\phi_m\) for the standard \(m\)-variate Gaussian density, this implies the weighted \(L^1\) Edgeworth expansion
\[
f_n(w)=\phi_m(w)\left(1+\frac1{\sqrt n}\sum_{i<j<\ell}w_{ij}w_{i\ell}w_{j\ell}\right)+R_n(w),\qquad
\int_{\mathbb R^m}|R_n(w)|\,dw\le C_k n^{-1}.
\]
For completeness, the Fourier remainder estimate has no implicit regularity assumption. The exact characteristic function of \(W_n\) has modulus
\[
\bigl|\mathbb E e^{\mathrm i t\cdot W_n}\bigr|=\det(I+T(t)^2/n)^{-n/4}
\le(1+2\|t\|^2/n)^{-n/4}.
\]
For sufficiently large \(n\), this and its derivatives through order \(m+2\) are integrable. Taylor expansion of the logarithm, with its differentiated remainder, on \(\|t\|\le n^{1/8}\) gives an \(O_k(n^{-1})\) Fourier remainder after multiplying by a fixed polynomial in \(\|t\|\) and a Gaussian envelope. On the complement, the determinant bound (with the same polynomial derivative bounds) yields a negligible Fourier integral: in the intermediate range it is exponentially small in a power of \(n\), and at large \(\|t\|\) it is bounded by a sufficiently high negative power. Fourier inversion after up to \(m+2\) differentiations therefore gives \(\sup_w(1+\|w\|)^{m+2}|R_n(w)|=O_k(n^{-1})\), which implies the displayed \(L^1\) estimate. The sign of the cubic density term follows because the Fourier transform of \(w_{ij}w_{i\ell}w_{j\ell}\phi_m(w)\) is \(-\mathrm i t_{ij}t_{i\ell}t_{j\ell}e^{-\|t\|^2/2}\).

**3. Orthant integration and the coincidence of coefficients.** Conditional on \(H\), the leading Gaussian density integrates over the shifted orthant to
\[
\prod_{i<j}\Phi\left(\frac{s_{ij}H_{ij}}{\sqrt n}\right)
=2^{-m}\left[1+\frac{\sqrt{2/\pi}}{\sqrt n}\sum_{i<j}s_{ij}H_{ij}
+O_k\left(n^{-1}(1+\sum_{i<j}H_{ij}^2)\right)\right].
\]
The cubic density term can be integrated over the unshifted orthant at an additional error \(O_k(n^{-1/2}(1+\sum H_{ij})/\sqrt n)\) after the prefactor. Each of the three involved one-dimensional signed half-Gaussian first moments is \(s_{ij}/\sqrt{2\pi}\), so its integral relative to \(2^{-m}\) equals \((2/\pi)^{3/2}s_{ij}s_{i\ell}s_{j\ell}\). For the linear term \(\mathbb E H_{ij}=(\mathbb E|G|)^2=2/\pi\). Thus the averaged edge coefficient is \(\sqrt{2/\pi}\cdot 2/\pi=(2/\pi)^{3/2}\), identical to the triangle coefficient. All half-normal moments required by these errors are finite. Combining the \(L^1\) remainder with these estimates proves
\[
2^{-m}\left[1+\frac{(2/\pi)^{3/2}}{\sqrt n}\left(\sum_{i<j}s_{ij}+\sum_{i<j<\ell}s_{ij}s_{i\ell}s_{j\ell}\right)+O_k(n^{-1})\right].
\]
Finally, \(n=d-1\) and \((2/\pi)^{3/2}=4/(\pi\sqrt{2\pi})\) give the theorem, uniformly in every fixed finite set of sign patterns.

## Verification
The standalone `verify.py` checks the covariance and third-cumulant combinatorics directly, checks that the proposed signed first-order corrections sum to zero over all patterns, and compares independent seeded hemisphere samples in selected dimensions with the stated formula. Its finite simulations are diagnostics only; the Fourier argument and integration prove the infinite-dimensional asymptotic. Run `python verify.py` in an environment with Python 3 and NumPy.

## Relationship to prior work
Cai, Fan and Jiang [1] study distributions and extremes of angles between random sphere points, primarily for point counts growing with dimension. Their results motivate angular probability laws but do not state the present joint hemisphere sign-pattern expansion.

Bubeck, Ding, Eldan and Rácz [2] analyze high-dimensional spherical geometric random graphs. They already give an exact finite-dimensional hemispherical **two-point** sign probability (Lemma 5), and study triangle effects in geometric graph statistics (including a leading-order lower bound). Accordingly the two-point marginal and the general observation of triangle dependence are **not** claimed to be new. The theorem here gives a specific, **signed full induced-configuration law for every fixed \(k\ge3\)** under hemispherical sampling, with both the one-edge hemisphere bias and the three-edge triangle dependence, an explicit common coefficient, and an error estimate uniform over all patterns. The inspected relevant arguments in [2] do not provide that full signed expansion.

Bárány, Hug, Reitzner and Schneider [3] investigate random spherical convex hulls in halfspheres, chiefly face numbers and fixed-dimension sample-size asymptotics. Their principal observables and asymptotic regime are different. Related published calculations of third-order moments for random correlation matrices [4] use a triangle graph motif, but concern moments rather than the present hemisphere-restricted sign orthants. The proof above independently establishes all probabilistic ingredients used for the stated result.

## Limitations
Only a fixed number \(k\) of independent points and an exact hemisphere are covered; there is no assertion for exponentially growing \(k\), other cap sizes, or arbitrary sampling densities. The expansion determines the first nonconstant term, not an all-orders law. The proof establishes a model-derived mathematical statement, not independent historical priority. Older work on induced subgraph probabilities or multivariate Gaussian-chaos orthants may contain equivalent special cases or further implications not found in the inspected sources.

## References
1. T. Cai, J. Fan, T. Jiang, *Distributions of Angles in Random Packing on Spheres*, arXiv:1306.0256v1 (first public 2013-06-02). https://arxiv.org/abs/1306.0256
2. S. Bubeck, J. Ding, R. Eldan, M. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713v1 (first public 2014-11-20), especially Lemmas 1 and 5. https://arxiv.org/abs/1411.5713
3. I. Bárány, D. Hug, M. Reitzner, R. Schneider, *Random points in halfspheres*, arXiv:1505.04672v1 (first public 2015-05-18). https://arxiv.org/abs/1505.04672
4. *Exact triangle cumulants reveal the first hidden dependence in LKJ correlation matrices*, publicly available mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-triangle-cumulants-reveal-the-first-hidden-dependence-in-l--955e3ffe3131
