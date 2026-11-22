# Cubic spherical harmonics on antipodal caps: two exact symmetry switches

## Finding
Let \(d\ge3\), let \(\mathcal H_3(S^{d-1};\mathbb C)\) be the complex pure degree-three spherical-harmonic space with probability-normalized surface measure, and let \(0<c<1\). Define the antipodal-cap region
\[
E_c=\{\omega\in S^{d-1}:|\omega_d|\ge c\}
\]
and the concentration operator \(C_c=P_3\mathbf1_{E_c}P_3\) on \(\mathcal H_3\), where \(P_3\) is the orthogonal projection. Set \(u=c^2\) and
\[
u_1=\frac1{d+2},\qquad u_2=\frac3{d+2}.
\]
There are exactly four symmetry-sector eigenvalues \(\lambda_0(u),\ldots,\lambda_3(u)\), listed below with their dimensions. Their complete strict order, including all ties, is
\[
\begin{array}{c|l}
0<u<u_1&\lambda_2>\lambda_0>\lambda_1>\lambda_3\\
u=u_1&\lambda_0=\lambda_1=\lambda_2>\lambda_3\\
u_1<u<u_2&\lambda_1>\lambda_0>\lambda_2>\lambda_3\\
u=u_2&\lambda_0=\lambda_1>\lambda_2>\lambda_3\\
u_2<u<1&\lambda_0>\lambda_1>\lambda_2>\lambda_3.
\end{array}
\]
Thus the **top** concentration eigenspace changes symmetry exactly twice. The first crossing has multiplicity \((d-1)(d+2)/2\), while the second has multiplicity \(d\). The least-concentrated sector is always the transverse cubic sector, with no transitions. All eigenvalues lie strictly in \((0,1)\).

In the thin-cap limit \(u\uparrow1\), the exact condition-number growth is
\[
\frac{\lambda_{\max}(C_c)}{\lambda_{\min}(C_c)}\sim
\frac{(d-1)(d+1)(d+3)(d+5)}{6(d+2)}(1-u)^{-3}.
\]
Consequently the condition number of continuous restriction \(R_c:\mathcal H_3\to L^2(E_c)\) is asymptotic to the square root of the displayed constant times \((1-c^2)^{-3/2}\).

## Assumptions and scope
The ambient dimension \(d\) is an arbitrary fixed integer at least three. Both caps have the same angular radius \(\arccos c\) and opposite poles; their union is nonempty and does not cover the sphere. Scalars are complex; replacing them by real scalars does not alter the eigenvalues. The operator uses the *global*, rather than cap-renormalized, surface measure in its quadratic form, so its eigenvalues are fractions of global \(L^2\) energy.

With \(t=\omega_d^2\), the probability density of \(t\) on the sphere is
\[
\frac{t^{-1/2}(1-t)^{(d-3)/2}}{B(1/2,(d-1)/2)},\qquad 0<t<1.
\]
The complete eigenvalue formulas are
\[
\lambda_k(u)=\frac{1}{B(1/2,(d-1)/2)N_k}
\int_u^1 t^{-1/2}(1-t)^{(d-3)/2}p_k(t)\,dt,
\qquad k=0,1,2,3,
\]
where
\[
\begin{aligned}
p_0(t)&=t\left(t-\frac3{d+2}\right)^2,&N_0&=\frac{6(d-1)}{d(d+2)^2(d+4)},\\
p_1(t)&=(1-t)\left(t-\frac1{d+2}\right)^2,&N_1&=\frac{2(d-1)(d+1)}{d(d+2)^2(d+4)},\\
p_2(t)&=t(1-t)^2,&N_2&=\frac{(d-1)(d+1)}{d(d+2)(d+4)},\\
p_3(t)&=(1-t)^3,&N_3&=\frac{(d-1)(d+1)(d+3)}{d(d+2)(d+4)}.
\end{aligned}
\]
Their respective multiplicities are
\[
1,\qquad d-1,\qquad \binom d2-1,\qquad\binom{d+1}3-(d-1),
\]
which sum to \(\binom{d+2}3-d=\dim\mathcal H_3(S^{d-1})\).

## Proof
Write \(\omega=(w,z)\in\mathbb R^{d-1}\times\mathbb R\), with \(z=\omega_d\). The orthogonal \(O(d-1)\)-decomposition of homogeneous harmonic cubics consists of four pieces: (i) the zonal polynomial \(z^3-3z|\omega|^2/(d+2)\); (ii) the \((d-1)\) polynomials \(w_j(z^2-|\omega|^2/(d+2))\); (iii) the polynomials \(zQ_2(w)\), where \(Q_2\) ranges over harmonic quadratics on \(\mathbb R^{d-1}\); and (iv) harmonic cubics \(Q_3(w)\) on \(\mathbb R^{d-1}\). Each is harmonic in the ambient variables, and the dimensions sum to the full degree-three harmonic dimension. Orthogonality is from the angular degrees \(0,1,2,3\) in \(w/|w|\) at each fixed \(z\).

The cap indicator depends only on \(z^2\). Orthogonality at each latitude therefore survives restriction, and within each transverse harmonic-degree sector the restricted quadratic form is a scalar multiple of the global form. Taking squared norms at fixed \(t=z^2\) yields the four weights \(p_k(t)\) above; the direction-dependent constants cancel in the concentration ratios. The global \(t\)-moments satisfy
\[
\mathbb E(t^j)=\frac{(1/2)_j}{(d/2)_j},\qquad j=0,1,2,3,
\]
and directly give the stated normalizers \(N_k=\mathbb E(p_k(t))\). This proves the complete spectral formulas and multiplicities.

For the strict comparisons, define the strictly positive factor
\[
W_d(u)=\frac{u^{1/2}(1-u)^{(d-1)/2}}{B(1/2,(d-1)/2)},\qquad 0<u<1.
\]
Exact integration by parts, using the beta weight, gives
\[
\begin{aligned}
\lambda_0-\lambda_1
 &=W_d\frac{d(d+4)}{3(d-1)(d+1)}\big((d+2)u-3\big)\big((d+2)u-1\big),\\
\lambda_0-\lambda_2
 &=W_d\frac{d(d+4)}{3(d+1)}u\big((d+2)u-1\big),\\
\lambda_1-\lambda_2
 &=W_d\frac{d(d+4)}{(d-1)(d+1)}(1-u)\big((d+2)u-1\big),\\
\lambda_1-\lambda_3
 &=W_d\frac{d(d+4)}{(d-1)(d+3)}(1-u)\big((d+2)u+1\big),\\
\lambda_2-\lambda_3
 &=W_d\frac{2d(d+2)(d+4)}{(d-1)(d+1)(d+3)}(1-u)^2.
\end{aligned}
\]
For reproducibility, each equality can be checked without evaluating incomplete beta functions: for any pair \((i,j)\), express the normalized polynomial difference \(p_i/N_i-p_j/N_j\) as
\[
\frac{1-du}{2}S_{ij}(u)+u(1-u)S'_{ij}(u).
\]
The corresponding tail integral is \(-W_d(u)S_{ij}(u)\); the displayed factorizations give the necessary quadratic or lower-degree polynomials \(S_{ij}\). These five identities imply every strict ordering and the two equality sets. All four eigenvalue integrals lie strictly between zero and one because their nonnegative weights have positive mass on both \((0,u)\) and \((u,1)\).

At \(u=u_1\), the first three sectors coincide and their multiplicities sum to \((d-1)(d+2)/2\). At \(u=u_2\), exactly the first two sectors tie, with total dimension \(d\). Since \(0<u_1<u_2<1\), there are no other transitions.

For thin caps, the largest eigenvalue is \(\lambda_0\) and the smallest is \(\lambda_3\). As \(u\uparrow1\), their leading integrands give
\[
\lambda_0\sim \frac{(1-3/(d+2))^2}{B(1/2,(d-1)/2)N_0}\frac{2}{d-1}(1-u)^{(d-1)/2},
\]
\[
\lambda_3\sim \frac{1}{B(1/2,(d-1)/2)N_3}\frac{2}{d+5}(1-u)^{(d+5)/2}.
\]
Taking the ratio and simplifying the stated \(N_0,N_3\) yields the sharp constant. Restriction singular values are the square roots of the eigenvalues of \(C_c=R_c^*R_c\), proving the final assertion.

## Verification
The companion file `check_cubic_caps.py` uses exact symbolic rational algebra to verify the global moments, all five beta-weighted derivative identities, and the sector dimension identity for a range of dimensions. It also verifies ordering and crossing cases by independent numerical integration and compares the resulting \(d=3\) eigenvalues against direct quadrature of normalized spherical harmonics. Additional checks test the thin-cap constant. Run with `python check_cubic_caps.py` after installing the packages listed in `requirements.txt`. The run returned `CUBIC_DOUBLE_CAP_CHECKS_PASS 147`. Exact symbolic algebra establishes the asserted polynomial identities for formal \(d\); finite numerical tests are illustrative, not the proof of all-dimensional statements.

## Relationship to prior work
Simons and Dahlen (2006) analyze the double-cap/belt Slepian problem on the ordinary two-sphere and give general tridiagonal methods for low-pass spherical harmonic spaces; their general matrix formulas permit calculation of the individual \(d=3\) pure-degree-three entries. The \(d=3\) numerical eigenvalues and the availability of the problem formulation are therefore not asserted to be novel. The present statement instead classifies, across *every* ambient dimension, the exact pure-cubic branch crossings, their unusually large degeneracies, all four branches and their multiplicities, and a sharp thin-cap condition-number constant. Jaming and Speckbacher (2020) establish general large-sieve concentration bounds on two-point homogeneous spaces, but not these exact pure-degree spectra. Michel, Plattner and Seibert (2021) treat scalar/vector/tensor Slepian construction, commuting operators for single polar caps on \(S^2\), and general numerical localization, not this all-dimensional cubic double-cap classification. Simons, Dahlen and Wieczorek (2004) provide the foundational spherical concentration formulation and cap computations. The exact identities here are compatible with those general frameworks but the all-dimensional equality classifications are not stated in the inspected texts.

## Limitations
The result concerns the single *pure* harmonic degree three, not the entire harmonic low-pass space through degree three. It assumes a perfect antipodal two-cap geometry with equal radii and continuous measurements. It does not establish finite-sample noise bounds or universality under deformed caps. The asymptotic is for fixed dimension as \(c\uparrow1\), not uniform in the dimension. Literature checks support but do not prove historical priority: general representation-theoretic or associated-Legendre formulas could imply part of the all-dimensional equality result under another name. No independent mathematical validation has been performed.

## References
1. F. J. Simons and F. A. Dahlen, “Spherical Slepian functions and the polar gap in geodesy,” *Geophysical Journal International* 166 (2006), 1039–1061, DOI: 10.1111/j.1365-246X.2006.03065.x.
2. P. Jaming and M. Speckbacher, “Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle,” arXiv:2004.02474v1, first posted 2020-04-06.
3. V. Michel, A. Plattner and K. Seibert, “A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator,” arXiv:2103.14650v1, first posted 2021-03-26.
4. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, “Spatiospectral concentration on a sphere,” arXiv:math/0408424v1, first posted 2004-08-31.
