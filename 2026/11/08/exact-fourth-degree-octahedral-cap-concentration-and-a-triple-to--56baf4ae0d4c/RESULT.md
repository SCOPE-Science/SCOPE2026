# Exact fourth-degree octahedral-cap concentration and a triple-to-simple optimal-mode transition

## Finding
Let \(\sigma\) be probability surface measure on the unit sphere \(S^2\subset\mathbb R^3\). For \(2^{-1/2}\le c<1\), let
\[
\Omega_c=\{(x,y,z)\in S^2:\max(|x|,|y|,|z|)\ge c\}.
\]
These are the six congruent (interior-disjoint) spherical caps centered at the coordinate-axis endpoints. On the nine-dimensional complex space \(\mathcal H_4\) of **pure degree-four spherical harmonics**, the spatial concentration quotient
\[
\mathcal Q_c(f)=\frac{\int_{\Omega_c}|f|^2\,d\sigma}{\int_{S^2}|f|^2\,d\sigma},\qquad 0\ne f\in\mathcal H_4,
\]
has exactly four eigenvalue branches, with multiplicities \(1,2,3,3\), respectively:
\[
\begin{aligned}
\lambda_A(c)&=\frac{3(1-c)}{512}(5775c^8+5775c^7-7125c^6-7125c^5+2829c^4+2829c^3-391c^2-391c+512),\\
\lambda_E(c)&=\frac{3(1-c)}{1024}(8085c^8+8085c^7-12855c^6-12855c^5+5919c^4+5919c^3-701c^2-701c+1024),\\
\lambda_T(c)&=-\frac{3(1-c)^2}{32}(15c^5+30c^4-18c^3-66c^2-49c-32),\\
\lambda_U(c)&=\frac{3(1-c)^2}{128}(1155c^7+2310c^6+705c^5-900c^4-363c^3+174c^2+151c+128).
\end{aligned}
\]
The four branch values need not be pairwise distinct at isolated radii; the displayed multiplicities describe the **invariant subspaces**, and coincident branches contribute their dimensions to the eigenspace multiplicity.

Let \(u_*\) be the **unique** root in \([1/2,1]\) of
\[
495u^3-645u^2+237u-23=0,
\]
and put \(c_*=\sqrt{u_*}=0.861650652371478\ldots\). Then the sharp spatial concentration is
\[
\sup_{0\ne f\in\mathcal H_4}\mathcal Q_c(f)
=\begin{cases}\lambda_U(c),&2^{-1/2}\le c<c_*,\\
\lambda_A(c)=\lambda_U(c),&c=c_*,\\
\lambda_A(c),&c_*<c<1.
\end{cases}
\]
The maximizing complex linear subspace has dimension \(3\) below the threshold, dimension \(4\) exactly at the threshold, and dimension \(1\) above it. The two other representation sectors are **never** maximizing.

## Assumptions and scope
Coordinates \((x,y,z)\) always refer to points on \(S^2\). The spherical harmonic space consists only of restrictions of homogeneous harmonic polynomials of degree four in three variables; it does **not** include lower degrees. Boundaries of adjacent caps touch only on a null set at \(c=2^{-1/2}\). The case \(c=1\), where all concentration eigenvalues vanish, and \(c<2^{-1/2}\), where caps overlap, are excluded.

The four invariant spaces, whose direct sum is \(\mathcal H_4\), are
\[
\begin{aligned}
A&=\operatorname{span}\{x^4+y^4+z^4-3/5\},\\
E&=\operatorname{span}\{x^4-y^4-\tfrac67(x^2-y^2),\ x^4+y^4-2z^4-\tfrac67(x^2+y^2-2z^2)\},\\
T&=\operatorname{span}\{xy(7z^2-1),\ yz(7x^2-1),\ zx(7y^2-1)\},\\
U&=\operatorname{span}\{xy(x^2-y^2),\ yz(y^2-z^2),\ zx(z^2-x^2)\}.
\end{aligned}
\]
The corresponding maximizing spaces are \(U\), \(A\oplus U\), and \(A\), in the three parameter regimes above. All spans are taken over \(\mathbb C\).

## Proof
**Harmonic decomposition and diagonalization.** Restore homogeneous degree four by replacing constants with \(r^2=x^2+y^2+z^2\), or their squares where appropriate. Direct application of the Euclidean Laplacian annihilates every displayed basis polynomial. Their dimensions are \(1+2+3+3=9=\dim\mathcal H_4\). Under coordinate sign changes and permutations, off-block inner products vanish on both the full sphere and \(\Omega_c\). Inside each of \(A,E,T,U\), the concentration form is a scalar multiple of the full-sphere form: the explicit orthogonal basis above gives this directly by the same sign and permutation symmetries. Thus the four scalar quotients are the complete eigenvalue spectrum, with their stated subspace dimensions.

**Exact moment evaluation.** For a cap about the positive third coordinate axis, set \(z=t\), \(x=\sqrt{1-t^2}\cos\phi\), \(y=\sqrt{1-t^2}\sin\phi\). Probability surface integration is \(dt\,d\phi/(4\pi)\). Because each squared harmonic is even under the antipodal map, the six caps contribute the sum of three polar-axis integrals:
\[
\int_{\Omega_c}|f|^2\,d\sigma
=\int_c^1\big(M_x(f^2;t)+M_y(f^2;t)+M_z(f^2;t)\big)\,dt,
\]
where \(M_j\) is the uniform circular mean at coordinate \(j=t\). The elementary moments used in every entry are
\[
\frac1{2\pi}\int_0^{2\pi}\cos^{2a}\phi\sin^{2b}\phi\,d\phi
=\frac{(2a)!(2b)!}{4^{a+b}a!b!(a+b)!},
\]
with odd exponents averaging to zero. Dividing the resulting polynomial cap integrals by their full-sphere norms gives the four displayed branches. The representative full-sphere squared norms for the first polynomial in \(A,E,T,U\) are, respectively, \(16/525,16/2205,4/45,4/315\). As an additional normalization check,
\[
\lambda_A+2\lambda_E+3\lambda_T+3\lambda_U=27(1-c)
=9\,\sigma(\Omega_c).
\]

**The sharp optimal-mode switch.** Set \(u=c^2\). Direct subtraction and factorization give
\[
\lambda_A-\lambda_U
=-\frac{63c(c-1)(c+1)}{512}(495u^3-645u^2+237u-23).
\]
The prefactor is positive for \(0<c<1\). The cubic is strictly convex throughout \(u\in[1/2,1]\), negative at \(u=1/2\) and \(u=7/10\), and positive at \(u=3/4\). Hence it has precisely one zero \(u_*\in(7/10,3/4)\), with negative and positive signs on the two sides. Therefore \(U\) beats \(A\) below \(c_*\), and \(A\) beats \(U\) above it.

The remaining sectors are strictly dominated. First,
\[
\lambda_T-\lambda_U
=-\frac{45c(1-c)^2(1+c)^2}{128}(7u-3)(11u+1)<0
\]
for \(u\ge1/2\). Second,
\[
\lambda_E-\lambda_U
=-\frac{45c(c-1)(c+1)}{1024}(1155u^3-1713u^2+681u-59).
\]
The prefactor is positive; the cubic is strictly negative on \([1/2,3/4]\). An exact certificate is provided by its cubic Bernstein coefficients on that interval, which are \(-19/8,-259/16,-947/32,-1571/64\), all strictly negative. Thus \(E\) is below \(U\) for \(u\le u_*\). Finally,
\[
\lambda_A-\lambda_E
=-\frac{27c(c-1)(c+1)}{1024}(385u^3-155u^2-29u-9)>0
\]
for \(u\ge u_*>7/10\), since the last cubic and its derivative are positive already at \(7/10\), and the derivative is increasing thereafter. These strict comparisons prove the claimed complete maximizer classification, including multiplicity four at \(c_*\).

## Verification
The companion `check_octa_degree4.py` uses exact rational symbolic algebra to verify the harmonic basis, all \(45\) full-sphere and cap pairings, each branch against its corresponding normalized Rayleigh quotient, the trace identity, and the difference-factorization and root-sign certificates. It also performs an independent direct two-dimensional Gauss–Legendre/trapezoid quadrature of the normalized nine-by-nine concentration matrix at four specified cap thresholds (if NumPy is installed). Run `python check_octa_degree4.py` in an environment with SymPy and NumPy. The reported exact checks are algebraic identities; the finite quadratures are corroborative and not substitutes for the proof. The exact domain is all real \(2^{-1/2}\le c<1\), not merely sampled radii.

## Relationship to prior work
Jaming and Speckbacher (arXiv:2004.02474v1; first public 2020-04-06) develop general large-sieve concentration inequalities for finite spherical-harmonic expansions on two-point homogeneous spaces; their inequalities do not identify the four exact octahedral-sector eigenvalues or the sharp switching radius. Simons, Dahlen, and Wieczorek (arXiv:math/0408424) formulate spherical Slepian concentration for arbitrary regions through a finite matrix, and Michel, Plattner, and Seibert (arXiv:2103.14650v1) develop scalar/vector/tensor spherical-cap commuting operators for a single cap. Those general constructions motivate the problem but do not furnish the exact six-cap, pure-degree-four classification established here.

An earlier exact treatment of **the same six-axis-cap geometry** for pure degrees one and two identifies linear isotropy and two quadratic sectors, with one quadratic sector always dominant; its degree-two formulas do not determine any degree-four concentration eigenvalue. The present degree-four calculation exhibits a qualitatively new sharp **mode switch** and an additional two-dimensional representation sector, requiring cap moments of squared quartic rather than squared quadratic harmonics. Related exact computations for two antipodal caps at degree four or four tetrahedrally placed caps at degree three concern different operators. No direct substitution into any of these spectra yields the four octahedral quartic branches. Earlier specialist octahedral harmonic calculations may exist and remain a bibliographic priority risk.

## Limitations
This result is restricted to fixed pure spherical-harmonic degree four and equal, disjoint octahedral caps. It does not resolve overlapping-cap radii, a bandlimit containing several degrees, unequally weighted caps, or numerical stability at large bandwidth. It provides an exact self-review and independent numerical cross-check, not an independently performed mathematical audit. Novelty is assessed against the inspected accessible sources, not asserted as exhaustively certified.

## References
1. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474v1 (2020-04-06), https://arxiv.org/html/2004.02474v1.
2. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (2004-08-31), https://arxiv.org/abs/math/0408424.
3. V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1 (2021-03-26), https://arxiv.org/abs/2103.14650.
