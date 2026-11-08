# Quantified asymptotic positivity for higher-order periodized Korobov quadrature

## Finding
For every fixed integer \(\alpha\ge2\) and \(\gamma>0\), let \(N\ge2\) and let \(w_{N,j}\), \(0\le j<N\), be the *unmodified full-lattice kernel-product-integration weights* defined below. With
\[
\mu(t)=\frac{\pi}{2}|\sin(2\pi t)|,
\]
there is a constant \(C_{\alpha,\gamma}<\infty\), independent of \(N\), such that
\[
\max_{0\le j<N}\left|w_{N,j}-\frac{\mu(j/N)}{N}\right|\le\frac{C_{\alpha,\gamma}}{N^2},\qquad
\sum_{j=0}^{N-1}(-w_{N,j})_+\le\frac{C_{\alpha,\gamma}}{N^2}.
\]
The sum of the weights has the **exact leading defect**
\[
\lim_{N\to\infty}N^{2\alpha}\left(1-\sum_{j=0}^{N-1}w_{N,j}\right)=2\gamma\zeta(2\alpha).
\]
Consequently, \(\sum_j|w_{N,j}|=1+O_{\alpha,\gamma}(N^{-2})\) and \(\lim_{N\to\infty}\sum_j |w_{N,j}|=\lim_{N\to\infty}\sum_jw_{N,j}=1\). This proves quantitative **asymptotic positivity**, *not* positivity of each weight at every finite \(N\).

There is an opposing finite-grid obstruction: for **every fixed even** \(N\ge2\) and every integer \(\alpha\ge2\), the endpoint weight \(w_{N,0}\) is **negative for all sufficiently large** \(\gamma\). Thus no unconditional all-grid pointwise positivity claim is possible when the kernel weight can grow with \(N\).

The underlying Fourier lemma is more general: if \(\nu\) is a real continuous, nonnegative, one-periodic probability density with \(|\widehat\nu(h)|\le M(1+|h|)^{-2}\), then the same kernel weights obey \(\max_j|w_{N,j}-\nu(j/N)/N|=O_{\alpha,\gamma,M}(N^{-2})\). If \(\nu\) additionally has a fixed finite zero set and is bounded below by a positive constant times the circular distance to that set, its total negative weight is \(O(N^{-2})\). The explicit density \(\mu\) satisfies both conditions.

## Assumptions and scope
For integer \(\alpha\ge2\) and fixed \(\gamma>0\), define the real positive-definite periodic Korobov kernel
\[
K_{\alpha,\gamma}(s,t)=\sum_{h\in\mathbb Z}a_h e^{2\pi i h(s-t)},\qquad
a_0=1,\quad a_h=\gamma |h|^{-2\alpha}\quad(h\ne0).
\]
The series is absolutely convergent. Use the full equispaced cyclic lattice \(t_j=j/N\), the Gram matrix \(G_{jk}=K_{\alpha,\gamma}(t_j,t_k)\), and the kernel-mean vector \(\kappa_j=\int_0^1 K_{\alpha,\gamma}(t_j,t)\mu(t)\,dt\). Define \(w_N=G^{-1}\kappa\). Every Fourier coefficient \(a_h\) is strictly positive, making \(G\) invertible for each \(N\). The normalization has \(\int_0^1\mu=1\); **no post-hoc weight normalization or clipping** is used.

## Proof
**1. Exact Fourier alias formula.** Write \(m_h=\int_0^1\mu(t)e^{-2\pi i ht}\,dt\). For each residue \(\ell\) modulo \(N\), put
\[
A_{N,\ell}=\sum_{h\equiv\ell\ ({\rm mod}\ N)} a_h>0,\qquad
B_{N,\ell}=\sum_{h\equiv\ell\ ({\rm mod}\ N)}a_hm_h,\qquad
M_{N,\ell}=\sum_{h\equiv\ell\ ({\rm mod}\ N)}m_h.
\]
Discrete Fourier diagonalization of the circulant Gram matrix gives
\[
w_{N,j}=\frac1N\sum_{\ell=0}^{N-1}\frac{B_{N,\ell}}{A_{N,\ell}} e^{2\pi i\ell j/N},\qquad
\mu(j/N)=\sum_{\ell=0}^{N-1}M_{N,\ell}e^{2\pi i\ell j/N}.
\]
Both equalities hold absolutely, the second by the Fourier series of \(\mu\). Therefore
\[
\max_j|Nw_{N,j}-\mu(j/N)|\le\sum_{\ell=0}^{N-1}|B_{N,\ell}/A_{N,\ell}-M_{N,\ell}|.
\]

**2. Uniform Fourier error.** More generally suppose \(|m_h|\le M(1+|h|)^{-2}\). For a nonzero residue \(\ell\), select its representative \(h_0\) with \(1\le r=|h_0|\le N/2\); at the even-grid midpoint either representative suffices. All other representatives have absolute value at least \(N/2\). Since \(2\alpha>1\), uniformly in \(r,N\),
\[
\sum_{q\ne0}a_{h_0+qN}\le C_\alpha\gamma N^{-2\alpha},\qquad
1-\frac{a_{h_0}}{A_{N,\ell}}\le C_\alpha(r/N)^{2\alpha},\qquad
\sum_{q\ne0}|m_{h_0+qN}|\le CMN^{-2}.
\]
Here the first bound follows by comparison with \(\sum_{q\ne0}(|q|-1/2)^{-2\alpha}\), and the last by comparison with \(\sum_{q\ne0}(|q|-1/2)^{-2}\). Expanding the difference between the weighted and unweighted alias sums yields
\[
\left|\frac{B_{N,\ell}}{A_{N,\ell}}-M_{N,\ell}\right|
\le CM\left[\frac{1}{(1+r)^2}\left(\frac rN\right)^{2\alpha}+N^{-2}\right].
\]
Summing over the \(N-1\) nonzero residues gives \(O(N^{-1})\), because
\[
N^{-2\alpha}\sum_{r=1}^{\lfloor N/2\rfloor}r^{2\alpha-2}=O(N^{-1})\qquad(2\alpha>1).
\]
For residue zero, \(a_0=1\), \(A_{N,0}=1+O(\gamma N^{-2\alpha})\), and \(\sum_{q\ne0}|m_{qN}|=O(MN^{-2})\). Hence the zero-residue difference is \(O(N^{-2\alpha}+N^{-2})=O(N^{-1})\). The desired uniform bound follows after division by \(N\).

**3. Negative weights and zero neighborhoods.** The density has the absolutely convergent Fourier coefficients
\[
m_0=1,\qquad m_{\pm2k}=-\frac1{4k^2-1}\ (k\ge1),\qquad m_h=0\text{ for odd }h.
\]
It is nonnegative and its only zeros on the circle are \(Z=\{0,\frac12\}\). The elementary sine bound supplies
\[
\mu(t)\ge2\pi\operatorname{dist}_{\mathbb R/\mathbb Z}(t,Z).
\]
If \(w_{N,j}<0\), the uniform bound of Step 2 implies \(\mu(j/N)<C/N\), whence \(\operatorname{dist}(j/N,Z)<C/(2\pi N)\). Only \(O(1)\) grid indices can lie in these fixed-width, shrinking neighborhoods of the two zeros, and every negative weight is at most \(C/N^2\) in absolute value. This proves \(\sum_j(-w_{N,j})_+=O(N^{-2})\).

**4. Sharp total-mass deficit.** The exact discrete Fourier formula at frequency zero yields
\[
\sum_{j=0}^{N-1}w_{N,j}=\frac{B_{N,0}}{A_{N,0}},\qquad
A_{N,0}=1+2\gamma\zeta(2\alpha)N^{-2\alpha}.
\]
Since \(m_{qN}=O((|q|N)^{-2})\) for nonzero \(q\),
\[
B_{N,0}=1+O_{\alpha,\gamma}(N^{-2\alpha-2}),
\]
so \(N^{2\alpha}(1-B_{N,0}/A_{N,0})\to2\gamma\zeta(2\alpha)\). Finally, the identity \(\sum_j|w_{N,j}|=\sum_jw_{N,j}+2\sum_j(-w_{N,j})_+\) and \(2\alpha\ge4\) establish the asserted \(1+O(N^{-2})\) total-variation asymptotic. \(\square\)

**5. Finite-grid obstruction at large kernel weight.** Fix even \(N\) and \(\alpha\ge2\). In an odd residue \(\ell\), all indices \(h\equiv\ell\pmod N\) are odd, so \(m_h=0\) and \(B_{N,\ell}=0\). For nonzero even \(\ell\), all such indices are nonzero even integers with \(m_h<0\); hence \(B_{N,\ell}/A_{N,\ell}<0\) independently of \(\gamma\). For residue zero, as \(\gamma\to\infty\), the ratio \(B_{N,0}/A_{N,0}\) tends to the strictly negative weighted mean of \(m_{qN}\), \(q\ne0\), with weights \(|qN|^{-2\alpha}\). Therefore \(Nw_{N,0}=\sum_\ell B_{N,\ell}/A_{N,\ell}\) has a strictly negative limit, proving the claimed obstruction. \(\square\)

## Verification
The accompanying standard Python program `verify.py` computes weights by Fourier aliasing and independently by direct solution of the positive-definite Gram system, checks the density's Fourier coefficients against high-resolution quadrature, and samples several values of \(\alpha,\gamma,N\). It passed 283 finite checks. Numerical diagnostics only corroborate the explicit Fourier identities and scaling; Steps 1–5 establish the infinite-dimensional quantifiers analytically.

## Relationship to prior work
Bartel, Gilbert, Griebel, Kuo and Sloan (2026) define the transformed density, the full-lattice optimal kernel weights, and identify asymptotic positivity as an open property for their **multivariate** scheme (Section 7.2). Here the proof resolves that stability question only for the one-dimensional *full lattice* at higher smoothness \(\alpha\ge2\), and derives an explicit negative-mass bound and total-mass constant. The first-order one-dimensional kernel has previously been studied with an exact finite-grid positivity threshold; that result neither establishes the higher-order bounds here nor is claimed as new. Standard equispaced trigonometric integration and periodic interpolation estimates concern different estimators or weaker norms and do not directly determine the signed total variation of these unmodified weighted-kernel quadrature coefficients.

## Limitations
This theorem makes no claim about arbitrary rank-one lattice generating vectors in dimension \(s\ge2\), sparse or randomized subsampling, eventual *individual* positivity, or a dimension-uniform constant. Constants depend on the fixed smoothness and kernel weight. The \(O(N^{-2})\) upper bound on the negative mass is not asserted sharp; finite negative weights may disappear sooner for some parameters. Priority beyond the cited and inspected literature has not been independently certified.

## References
1. F. Bartel, A. D. Gilbert, M. Griebel, F. Y. Kuo and I. H. Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization*, arXiv:2610.01113v1 (first public release 2026-10-01), Sections 1.2, 3.2–3.3 and 7.2, https://arxiv.org/html/2610.01113v1.
2. T. Goda and D. Krieg, *A simple universal algorithm for high-dimensional integration*, Numerische Mathematik (2025), https://doi.org/10.1007/s00211-025-01517-z. Its median-of-equal-weight rules are distinct from the present optimally fitted unequal weights.
3. Kh. M. Shadimetov, A. R. Hayotov and N. H. Mamatova, *Optimal interpolation formulas in the periodic function space of S. L. Sobolev*, arXiv:1012.1953 (2010). Its full text, including interpolation formulas in Sections 3–6 and the equal-weight quadrature derivation in Section 8, was inspected; it does not analyze the nonconstant density or signed weight variation of the present kernel rule.
