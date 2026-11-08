# Exact quadratic spherical-orthant concentration and a sharp dimension-squared stability law

## Finding

Let \(d\ge3\), let \(S^{d-1}\) carry normalized rotation-invariant surface measure \(\sigma\), and let \(\Omega_d=\{x\in S^{d-1}:x_i>0\text{ for every }i\}\). On the space \(\mathcal H_2(S^{d-1})\) of complex-valued pure degree-two spherical harmonics, define the orthant concentration operator \(C_{2,d}\) by
\[
\langle C_{2,d}f,g\rangle_{L^2(S^{d-1})}=\int_{\Omega_d}f(x)\overline{g(x)}\,d\sigma(x).
\]
Put \(a=2/\pi\), \(\alpha=(1-a)^2\), \(\beta=a(1-a)\), \(\gamma=a^2\), and
\[
M_d=\begin{pmatrix}1&a\sqrt{(d-2)/2}\\a\sqrt{(d-2)/2}&\alpha+\beta(d-2)\end{pmatrix},
\qquad \mu_-(d)<\mu_+(d)\text{ its eigenvalues},
\]
\[
\tau_d=\alpha+2\beta(d-1)+\frac{\gamma d(d-1)}2.
\]
The **complete spectrum**, listing values \(2^{-d}\) times the displayed numbers, is
\[
\begin{array}{c|c}
\text{number}&\text{multiplicity}\\\hline
\tau_d&1\\
\mu_+(d)&d-1\\
\alpha&d(d-3)/2\\
\mu_-(d)&d-1
\end{array}
\]
(with the \(\alpha\) row absent for \(d=3\)). All eigenvalues lie strictly between \(0\) and \(1\); for \(d\ge4\) their strict ordering is
\[
0<\mu_-(d)<\alpha<\mu_+(d)<\tau_d.
\]
For \(d=3\), omit \(\alpha\) from this ordering. Thus the most concentrated harmonic is, uniquely up to scalar,
\[
\sum_{1\le i<j\le d}x_ix_j,
\]
and the least concentrated space has dimension \(d-1\). The quadratic concentration condition number obeys the **sharp dimension law**
\[
\boxed{\displaystyle\lim_{d\to\infty}\frac{\kappa(C_{2,d})}{d^2}=
\frac{2(\pi-2)}{\pi^2(\pi-3)}.}
\]
For contrast, on pure degree-one harmonics the exact orthant spectrum is \(2^{-d}(1+2(d-1)/\pi)\) once and \(2^{-d}(1-2/\pi)\) with multiplicity \(d-1\), so its concentration condition number is \((\pi+2(d-1))/(\pi-2)\), only linear in \(d\). The singular-value condition number of continuous degree-two restriction to the orthant is \(\sqrt{\kappa(C_{2,d})}\), asymptotic to \(d\sqrt{2(\pi-2)/(\pi^2(\pi-3))}\).

## Assumptions and scope

All dimensions \(d\) are fixed integers at least three; the final limit lets \(d\to\infty\). The harmonic space is **homogeneous degree exactly two**, not the full polynomial low-pass space of degrees zero through two. The input functions may be complex; the real symmetric calculation extends by complexification. Boundary hyperplanes have measure zero, so changing \(>\) to \(\ge\) does not affect the operator. The normalization uses the full-sphere probability measure, not unnormalized surface area. Conditioning is the ratio of largest to smallest positive eigenvalues for \(C_{2,d}\), or its square root for the restriction map.

## Proof

**1. Fourth moments.** Let \(X\) be uniformly distributed on the positive orthant, equivalently \(X=|Z|/\|Z\|\) for independent standard real Gaussian coordinates \(Z_i\). For nonnegative integer exponents of total degree four,
\[
\mathbb E_{\Omega_d}\prod_i X_i^{k_i}=
\frac{\Gamma(d/2)}{\Gamma((d+4)/2)}
\prod_i\frac{\Gamma((k_i+1)/2)}{\Gamma(1/2)}.
\]
For distinct indices this gives, after multiplication by \(d(d+2)\), the five moments \(3,1,4/\pi,2/\pi,4/\pi^2\) for patterns \((4),(2,2),(3,1),(2,1,1),(1,1,1,1)\), respectively. The orthant has full-sphere measure \(2^{-d}\).

**2. Euclidean-coordinate model.** Every homogeneous harmonic quadratic is \(q(x)=x^TAx\) with \(A=A^T\) and \(\operatorname{tr}A=0\). Write
\[
q(x)=\frac1{\sqrt2}\sum_{i=1}^d u_i x_i^2+\sum_{i<j}v_{ij}x_ix_j,
\qquad\sum_i u_i=0.
\]
Full-sphere fourth moments give
\[
d(d+2)\mathbb E_{S^{d-1}}|q(X)|^2=\sum_i|u_i|^2+\sum_{i<j}|v_{ij}|^2.
\]
Let \(B\) be the unsigned vertex-edge incidence matrix of the complete graph on \(d\) vertices, so \((Bv)_i=\sum_{j\ne i}v_{ij}\), and let \(S(v)=\sum_{i<j}v_{ij}\). Expanding the orthant moments and grouping edge pairs that are equal, adjacent, or disjoint yields the exact form
\[
\begin{aligned}
&d(d+2)\mathbb E_{\Omega_d}|q(X)|^2\\
&=\|u\|^2+\alpha\|v\|^2+\beta\|Bv\|^2+\gamma|S(v)|^2+
2\operatorname{Re}\left(\frac{a}{\sqrt2}\langle u,Bv\rangle\right).
\end{aligned}
\]
The cross coefficient follows directly from the \((3,1)\) and \((2,1,1)\) moments and \(\sum_i u_i=0\). Thus \(2^dC_{2,d}\) is represented by this Hermitian form on \(\mathbf1^\perp\oplus\mathbb C^{\binom d2}\).

**3. Complete spectral decomposition.** Since \(BB^T=(d-2)I+J\), where \(J\) is the all-ones matrix, edge space decomposes orthogonally into the constant edge vector (dimension one), the image \(B^T(\mathbf1^\perp)\) (dimension \(d-1\)), and \(\ker B\) (dimension \(\binom d2-d=d(d-3)/2\); zero when \(d=3\)). The constant vector has squared incidence norm \(2(d-1)\) and squared edge sum \(\binom d2\) per unit edge norm; hence its eigenvalue is \(\tau_d\). On \(\ker B\), the eigenvalue is \(\alpha\). For each unit \(w\in\mathbf1^\perp\), use the orthonormal pair consisting of vertex vector \(u=w\) and edge vector \(v=B^Tw/\sqrt{d-2}\). Their invariant form has matrix \(M_d\), because the cross entry is \(a\sqrt{(d-2)/2}\). This produces \(\mu_\pm(d)\), each \(d-1\) times, and accounts for all \((d-1)(d+2)/2\) harmonic dimensions.

**4. Strict ordering and eigenfunction identification.** The determinant of \(M_d\) is
\[
\det M_d=\alpha+(d-2)\left(\beta-\frac{a^2}{2}\right)
=\alpha+(d-2)a\left(1-\frac{3a}{2}\right)>0,
\]
because \(\pi>3\). Its trace is positive, so \(\mu_-(d)>0\). Moreover,
\[
\det(M_d-\alpha I)=(d-2)a^2\left((2-a)(1-a)-\frac12\right)<0.
\]
Indeed \(\pi<22/7\) implies \(a>7/11\), and the decreasing function \((2-a)(1-a)\) is then less than \(60/121<1/2\). Consequently \(\mu_-<\alpha<\mu_+\). Finally
\[
\tau_d-\operatorname{tr}M_d=d\beta+\gamma\binom d2-1>0
\]
for \(d\ge3\); this difference is increasing in \(d\), and at \(d=3\) it equals \(6/\pi-1>0\). Therefore \(\tau_d>\mu_+\). Every nonzero spherical harmonic has positive integral on both the orthant and its open complement, because a nonzero real-analytic function cannot vanish on an open subset; hence all the concentration eigenvalues are strictly below one. The unique top eigenvector is constant in edge space and zero in vertex space, giving the displayed harmonic. The minimum is the \(\mu_-\) standard sector, with the stated dimension.

**5. Sharp dimension law and linear comparison.** As \(d\to\infty\),
\[
\tau_d=\frac{a^2}{2}d^2+O(d),\qquad
\mu_-(d)=1-\frac{a^2/2}{\beta}+O(d^{-1})
=\frac{\pi-3}{\pi-2}+O(d^{-1}).
\]
The ratio of these numbers gives the stated constant; the common factor \(2^{-d}\) cancels. For degree one, the normalized quadratic form of a linear function is \(2^{-d}[(1-a)I+aJ]\), since \(d\mathbb E_{\Omega_d}(X_iX_j)=1\) for \(i=j\) and equals \(a\) otherwise. This gives the exact degree-one spectrum and condition number.

## Verification

The standalone `orthant_spectral_check.py` builds the full quadratic Gram matrix independently from monomial gamma-function integrals in dimensions \(3\) through \(12\), without using the incidence-block formula to construct it. It compares the entire eigenvalue multiset to the theorem, checks traces and strict inequalities, and checks the sharp large-dimensional constant. Execute `python orthant_spectral_check.py` with NumPy installed. The verified execution returned `ORTHANT_HARMONIC_SPECTRUM_CHECKS_PASS 399`. Finite matrix checks corroborate, but do not replace, the all-dimensional proof above.

## Relationship to prior work

General spherical Slepian concentration is classically an algebraic eigenvalue problem for arbitrary measurement regions. Simons, Dahlen and Wieczorek (2004) established that framework, including numerical concentration for arbitrary geographical regions and special polar-cap constructions. Michel, Plattner and Seibert (arXiv:2103.14650, first posted 2021-03-26), in their full preprint sections 3.1–3.3 and 5, derive the general kernel matrix and cap-specific commuting-operator methods. They do **not** explicitly calculate the present positive-orthant pure-quadratic spectrum or the dimension-squared conditioning constant. The generic kernel formula allows its computation in principle but does not imply the evaluated orthant-specific result without the moment and incidence decomposition here. Roddy and McEwen's later work treats wavelet construction on incomplete spherical regions and not an explicit positive-orthant second-degree spectral classification. Earlier hemisphere, lune, and union-of-caps concentration formulas concern other regions and are not used as novel components here.

## Limitations

The theorem is for one positive orthant and **pure** harmonic degrees one or two, with continuous noiseless measurements. It does not establish analogous formulas for higher degrees, arbitrary spherical simplices, or discretized/noisy sampling. A prior implicit derivation via symmetric-group harmonic tensors or orthant moments could remain undiscovered; novelty is provisional, not independently certified. The simple condition number compares energy-capture eigenvalues, not a noise-dependent reconstruction risk under a specified sampling scheme.

## References

1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (first posted 2004-08-31), https://arxiv.org/abs/math/0408424.
2. V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first posted 2021-03-26), https://arxiv.org/abs/2103.14650.
3. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02323 (first posted 2021-06-04), https://arxiv.org/abs/2106.02323.
