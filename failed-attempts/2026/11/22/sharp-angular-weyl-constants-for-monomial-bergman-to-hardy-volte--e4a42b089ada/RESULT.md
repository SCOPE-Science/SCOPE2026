# Sharp angular Weyl constants for monomial Bergman-to-Hardy Volterra maps

## Finding
Let \(d\ge1\) be an integer, \(\alpha>-1\), and \(\mathbf a=(a_1,\ldots,a_d)\in\mathbb N_0^d\) have positive total degree \(m=\sum_j a_j\). On the complex unit ball \(\mathbb B_d\), set \(b(z)=\prod_jz_j^{a_j}\) and define the radial Volterra integral
\[
(J_bf)(z)=\int_0^1 f(tz)(Rb)(tz)\,\frac{dt}{t},\qquad Rb(z)=\sum_{j=1}^d z_j\frac{\partial b}{\partial z_j}(z).
\]
It acts from normalized weighted analytic Bergman \(A^2_\alpha(\mathbb B_d)\) into normalized boundary Hardy \(H^2(\mathbb B_d)\). Its complete singular-value multiset is given by the explicit diagonal formula in the proof.

For \(-1<\alpha<1\), let
\[
\rho=\frac{2d}{1-\alpha},\qquad
C=m\sqrt{\frac{\Gamma(d)}{\Gamma(d+\alpha+1)}},\qquad
\mathcal W=\frac{C^\rho}{d}\frac{\prod_{j=1}^d\Gamma(1+\rho a_j/2)}{\Gamma(d+\rho m/2)}.
\]
Then \(\mathcal W\) is finite and strictly positive, and the **sharp Weyl law** is
\[
\boxed{\lim_{t\downarrow0}t^\rho\#\{n:s_n(J_b)>t\}=\mathcal W,\qquad
\lim_{n\to\infty}n^{1/\rho}s_n(J_b)=\mathcal W^{1/\rho}.}
\]
Thus \(J_b\in\mathcal S_p\) exactly for \(p>\rho\), belongs to weak \(\mathcal S_\rho\) but not \(\mathcal S_\rho\), and has the **exact logarithmic trace coefficient and zeta pole**
\[
\boxed{\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=1}^N s_n(J_b)^\rho=\mathcal W,
\quad\lim_{p\downarrow\rho}(p-\rho)\operatorname{Tr}|J_b|^p=\rho\mathcal W.}
\]
At the bounded noncompact boundary \(\alpha=1\), its exact essential norm is
\[
\boxed{\|J_b\|_{\mathrm{ess}}=m\sqrt{\frac{\Gamma(d)}{\Gamma(d+2)}}\prod_{j=1}^d\left(\frac{a_j}{m}\right)^{a_j/2}.}
\]
A factor with \(a_j=0\) is defined as one. For \(\alpha>1\), the polynomial-defined integral operator has no bounded extension between the indicated spaces.

In particular, for \(d=2\), \(\alpha=0\), and \(b(z)=z_1z_2\), the critical exponent is \(\rho=4\) and the precise Weyl constant is \(\mathcal W=1/15\). The full angular gamma-product records the monomial's distribution among coordinates; the critical exponent depends only on dimension and the Bergman weight.

## Assumptions and scope
The ball is \(\mathbb B_d=\{z\in\mathbb C^d:\|z\|_2<1\}\). The Bergman norm is integration against the probability measure \(c_{d,\alpha}(1-\|z\|_2^2)^\alpha dV(z)\); the Hardy norm is integration against normalized surface measure on \(\partial\mathbb B_d\). The integral is defined on analytic polynomials and extended where bounded. The multiindex components are nonnegative integers, at least one positive. Singular values are arranged in nonincreasing order with multiplicity. The result is about this homogeneous monomial-symbol family, not all analytic symbols.

## Proof
**1. Exact monomial singular values.** Write \(\mathbf k\in\mathbb N_0^d\), \(n=|\mathbf k|\), and \(\mathbf k!=\prod_j k_j!\). The normalized measures give
\[
\|z^{\mathbf k}\|_{A^2_\alpha}^2=\frac{\Gamma(d+\alpha+1)\mathbf k!}{\Gamma(d+\alpha+1+n)},\qquad
\|z^{\mathbf k}\|_{H^2}^2=\frac{\Gamma(d)\mathbf k!}{\Gamma(d+n)}.
\]
Since \(Rb=mb\), the radial integral yields \(J_b z^{\mathbf k}=m z^{\mathbf k+\mathbf a}/(n+m)\). Different input indices have different output indices, so their normalized images are orthogonal. The complete singular-value multiset, counting multiplicity, is therefore \(\{\sigma_{\mathbf k}:\mathbf k\in\mathbb N_0^d\}\), with
\[
\boxed{\sigma_{\mathbf k}=\frac{m}{n+m}\left[\frac{\Gamma(d)}{\Gamma(d+\alpha+1)}\frac{\Gamma(d+\alpha+1+n)}{\Gamma(d+n+m)}\prod_{j=1}^d\frac{(k_j+a_j)!}{k_j!}\right]^{1/2}.}
\]
All entries are positive. Orthogonality proves the formula without assuming the map is self-adjoint or normal.

**2. Uniform large-degree control and the phase boundary.** Put \(\beta=(1-\alpha)/2\) and \(\Phi(x)=\prod_jx_j^{a_j/2}\) on \(\Delta_{d-1}=\{x_j\ge0:\sum_jx_j=1\}\). For sequences \(n\to\infty\) with \(k_j/n\to x_j>0\) for every \(j\) with \(a_j>0\), finite gamma-ratio asymptotics give
\[
\sigma_{\mathbf k}=C n^{-\beta}(\Phi(x)+o(1)).
\]
The convergence is uniform on every closed angular subset away from relevant coordinate faces. The gamma-ratio bounds and \(\prod_{r=1}^{a_j}(k_j+r)\le(n+m)^m\) also give a constant \(M\), independent of \(\mathbf k\), such that \(\sigma_{\mathbf k}\le M(n+1)^{-\beta}\) if \(\beta>0\); at \(\beta=0\) the singular values are uniformly bounded. If \(\beta<0\), choosing \(k_j/n\to a_j/m\) on positive coordinates gives \(\sigma_{\mathbf k}\to\infty\). Hence the operator is compact for \(\alpha<1\), bounded but noncompact for \(\alpha=1\), and unbounded for \(\alpha>1\).

At \(\alpha=1\), the norm of a diagonal map modulo compact operators is \(\lim_{N\to\infty}\sup_{|\mathbf k|\ge N}\sigma_{\mathbf k}\). By compactness of the simplex and the gamma-ratio bounds this is \(C\max_{x\in\Delta_{d-1}}\Phi(x)\). Weighted arithmetic-geometric mean (or Lagrange multipliers on the positive coordinates) gives \(\max\Phi=\prod_j(a_j/m)^{a_j/2}\), proving the exact essential norm.

**3. Lattice-point Weyl limit.** Suppose \(\beta>0\) and put \(R=(C/t)^{1/\beta}\). Rescale the lattice by writing \(y=\mathbf k/R\). For \(y\ne0\) away from relevant coordinate faces, the condition \(\sigma_{\mathbf k}>t\) tends to
\[
\left(\sum_j y_j\right)^{-\beta}\Phi\!\left(\frac{y}{\sum_j y_j}\right)>1.
\]
The limiting region \(E\subset\mathbb R_+^d\) is star-shaped, bounded, and has radial boundary \(0\le r<\Phi(x)^{1/\beta}\) in \(\ell_1\)-polar coordinates \(y=rx\), \(x\in\Delta_{d-1}\). Its boundary has Lebesgue measure zero. To justify the lattice limit globally, first restrict to \(\delta\le\sum y_j\le M^{1/\beta}/C^{1/\beta}+1\) and angular directions separated from relevant faces; there convergence is uniform. The excluded small ball contributes at most \(O(\delta^dR^d)\) lattice points, thin coordinate neighborhoods contribute arbitrarily small proportion of \(R^d\), and the uniform degree bound eliminates the far tail. Sending the neighborhood widths to zero proves \(R^{-d}\#\{\sigma_{\mathbf k}>t\}\to\operatorname{vol}(E)\).

The \(\ell_1\)-polar Jacobian is \(r^{d-1}\), with simplex surface-coordinate measure \(dx_1\cdots dx_{d-1}\), so
\[
\operatorname{vol}(E)=\frac1d\int_{\Delta_{d-1}}\Phi(x)^{d/\beta}\,dx
=\frac1d\frac{\prod_j\Gamma(1+a_jd/(2\beta))}{\Gamma(d+md/(2\beta))}.
\]
The same formula holds for \(d=1\), where the simplex is a point and its integral is one. Since \(d/\beta=\rho\) and \(R^d=(C/t)^\rho\), the claimed counting constant follows. Standard inversion of a positive monotone counting asymptotic yields the stated ordered singular values.

**4. Spectral ideals and residues.** The singular law implies \(s_n(J_b)^\rho\sim\mathcal W/n\), proving weak-\(\mathcal S_\rho\) membership, failure of \(\mathcal S_\rho\), and the logarithmic coefficient. Comparison with \(\sum n^{-p/\rho}\) gives membership for exactly \(p>\rho\) and, as \(p\downarrow\rho\), the pole coefficient \(\rho\mathcal W\). No spectral asymptotic for a general nonmonomial symbol is asserted.

## Verification
The accompanying `checker.py` evaluates the exact gamma formula and an independent integer-factorial formulation on finite monomial families in dimensions one through three. It also counts eigenvalues at several thresholds. For \(d=2,\alpha=0,b=z_1z_2\), it confirms the exact constant \(1/15\) and exhibits normalized counts approaching one; in a coordinate-square example it confirms \(2/5\). A three-dimensional mixed-monomial example provides an additional diagnostic. These finite tests do not certify the infinite Weyl law; that conclusion follows from Steps 1–4. Run `python checker.py` with Python 3 and no external dependencies.

## Relationship to prior work
Miihkinen, Pau, Perälä and Wang (2019/2020) classify boundedness for general Volterra integration operators from weighted Bergman spaces to Hardy spaces; their Theorem 1 supplies the qualitative parameter regime but no ordered singular-value coefficient. Chen, Pau and Wang (2021) establish general compactness and Schatten(-Herz) criteria. Their Theorem 1.3 already implies the sharp **membership threshold** \(p>2d/(1-\alpha)\) for a nonconstant monomial, so that threshold is not claimed as an independently novel theorem. Their Theorem 5.4 gives rate criteria under a restrictive regularity assumption, not this gamma-product counting limit, logarithmic trace coefficient, or exact Calkin norm. Liu, Yuan and Zeng (2022) analyze Volterra operators from Bergman-type spaces back to Bergman-type spaces, not this Hardy codomain. Related spectral laws for generalized Volterra **companions** concern derivatives applied to the input function and/or damped self-maps, rather than \(f\,Rb\) from Bergman to Hardy. The quantitative claim is the explicit dimension- and multiindex-dependent Weyl coefficient and its critical residues, not qualitative compactness, boundedness, or Schatten membership. Historical priority relative to unindexed general Toeplitz eigenvalue asymptotics remains uncertain.

## Limitations
The exact diagonalization requires one monomial symbol and the standard radial Hilbert Bergman/Hardy norms. Arbitrary polynomial combinations are not diagonal in the same basis and are not covered. The result does not give a second Weyl term or a general-symbol spectral formula. General qualitative Schatten and boundedness results are prior work; only the exact coefficient and its consequences are assessed as new. Verification is self-review and finite computational checks, not independent validation.

## References
1. S. Miihkinen, J. Pau, A. Perälä, M. Wang, *Volterra type integration operators from Bergman spaces to Hardy spaces*, arXiv:1904.00359v1, first public 2019-03-31, Theorem 1; https://arxiv.org/abs/1904.00359.
2. J. Chen, J. Pau, M. Wang, *Essential Norms and Schatten(-Herz) Classes of Integration Operators from Bergman Spaces to Hardy Spaces*, Results in Mathematics 76 (2021), doi:10.1007/s00025-021-01403-8, particularly Theorems 1.3 and 5.4; https://doi.org/10.1007/s00025-021-01403-8.
3. J. Liu, C. Yuan, H. Zeng, *Schatten classes of Volterra operators on Bergman-type spaces in the unit ball*, CPAA 21 (2022), 3425–3439, doi:10.3934/cpaa.2022108; https://www.aimsciences.org/article/doi/10.3934/cpaa.2022108.
4. O. El-Fallah, H. Mahzouli, I. Marrhich, H. Naqos, *Asymptotic behavior of eigenvalues of Toeplitz operators on the weighted analytic spaces*, JFA 270 (2016), 4614–4630, doi:10.1016/j.jfa.2016.01.005 (general spectral-comparison risk; not used for the proof).
