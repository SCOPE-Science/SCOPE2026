# Two sharp symmetry switches in polar-cap cross-degree spherical harmonic leakage

## Finding
For every integer \(d\ge3\), let \(\mathcal H_j\subset L^2(S^{d-1},\sigma)\) be the complex, exact-degree-\(j\) spherical harmonics, where \(\sigma\) is probability surface measure. For \(0\le a<1\), let \(E_a=\{x\in S^{d-1}:x_d\ge a\}\) and define the cross-degree coupling operator
\[
B_a=P_{\mathcal H_2}\,M_{\mathbf1_{E_a}}\big|_{\mathcal H_3}:\mathcal H_3\longrightarrow\mathcal H_2.
\]
Put \(s=a^2\), \(r_d=\sqrt{2(d+2)/(d+1)}\), and \(h_d=\sqrt{6d/(d+1)}\). Set
\[
P_d(s)=d(d+2)s^2-6s+3,\qquad Q_d(s)=(1-s)(1+(d+2)s),
\]
\[
F_d(s)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}
\frac{(1-s)^{(d-1)/2}}{d-1}\,\frac{\sqrt{d(d+2)(d+4)}}{d+3}.
\]
The positive singular values of \(B_a\), including multiplicities, are exactly
\[
\begin{aligned}
\sigma_0(s)&=F_d(s)\frac{P_d(s)}{\sqrt{12}}&&\text{(multiplicity 1)},\\
\sigma_1(s)&=F_d(s)\sqrt{\frac{d}{2(d+1)}}Q_d(s)&&\text{(multiplicity \(d-1\))},\\
\sigma_2(s)&=F_d(s)\frac{\sqrt{d(d+2)}}{d+1}(1-s)^2
&&\text{(multiplicity \((d-2)(d+1)/2\))}.
\end{aligned}
\]
The remaining \((d-1)(d-2)(d+3)/6\) singular directions on the degree-three source are zero. Thus \(B_a\) is surjective for every \(0\le a<1\).

There are **exactly two** transitions in its largest singular value as the polar cap shrinks. Define
\[
\begin{aligned}
s_{21}&=\frac{r_d-1}{r_d+d+2},\\
s_{10}&=\frac{6+h_d(d+1)+\sqrt{[6+h_d(d+1)]^2-4(d+2)(d+h_d)(3-h_d)}}{2(d+2)(d+h_d)}.
\end{aligned}
\]
Then \(0<s_{21}<1/(d+2)<s_{10}<1\), and the sharp dominant symmetry sequence is
\[
\begin{array}{c|ccccc}
s&[0,s_{21})&\{s_{21}\}&(s_{21},s_{10})&\{s_{10}\}&(s_{10},1)\\\hline
\operatorname{argmax}\sigma_j&2&1,2&1&0,1&0.
\end{array}
\]
At the first transition the maximizing singular subspace in \(\mathcal H_2\) has dimension \((d-2)(d+1)/2+d-1\); at the second it has dimension \(d\). In the high-dimensional limit,
\[
d\,s_{21}\longrightarrow\sqrt2-1,\qquad
 d\,s_{10}\longrightarrow\frac{\sqrt6+\sqrt{4\sqrt6-6}}{2}.
\]
For fixed \(d\) and \(s\uparrow1\), the nonzero-singular-value condition number satisfies
\[
\frac{\sigma_{\max}(s)}{\sigma_{\min}^{+}(s)}\sim
\frac{(d-1)(d+3)(d+1)}{\sqrt{12d(d+2)}}(1-s)^{-2}.
\]

## Assumptions and scope
The pair of degrees \((2,3)\) is the first adjacent positive-degree pair with three matching transverse orders, allowing two distinct optimizer changes. The statement concerns **cross-degree regional leakage**, not the spectrum of the full two-degree Slepian concentration matrix and not concentration within a single harmonic degree. The cap is one northern polar cap, not an antipodal pair; for an antipodally symmetric mask, this coupling vanishes by parity. Complex and real harmonic spaces give the same singular values with the stated real or complex multiplicities. The parameter range is \(d\ge3\), \(0\le a<1\); the collapsed empty cap \(a=1\) is excluded from strict ranking and surjectivity. All surface integrals use normalized surface measure, so no area factors are suppressed.

## Proof
Write \(u=x_d\) and \(v=(x_1,\ldots,x_{d-1})\), with \(|v|^2=1-u^2\). Under the stabilizer \(O(d-1)\), the degree-two harmonic space splits orthogonally into inequivalent transverse harmonic orders \(j=0,1,2\), of dimensions \(1,d-1,(d-2)(d+1)/2\). The degree-three space contains matching orders and one additional order \(j=3\). The cap mask commutes with \(O(d-1)\). Orthogonality of transverse harmonics shows that each matching block of the cross-degree operator is a scalar multiple of the identity between corresponding irreducible sectors, and the unmatched degree-three sector is killed.

For representative vectors in the three matching sectors, use the following homogeneous harmonic polynomials restricted to the unit sphere (with \(v_1,v_2\) denoting two different transverse coordinates):
\[
\begin{array}{c|cc}
j&\mathcal H_2&\mathcal H_3\\\hline
0&u^2-1/d&u^3-3u/(d+2)\\
1&uv_1&((d+2)u^2-1)v_1\\
2&v_1^2-v_2^2&u(v_1^2-v_2^2).
\end{array}
\]
The squared full-sphere norms of each pair, in this order, are
\[
\begin{array}{c|cc}
j&\|f_{2,j}\|^2&\|f_{3,j}\|^2\\\hline
0&2(d-1)/[d^2(d+2)]&6(d-1)/[d(d+2)^2(d+4)]\\
1&1/[d(d+2)]&2(d+1)/[d(d+4)]\\
2&4/[d(d+2)]&4/[d(d+2)(d+4)].
\end{array}
\]
These norms follow from uniform-sphere polynomial moments, for example \(\mathbb E[x_i^2x_j^2]=1/[d(d+2)]\) for \(i\ne j\) and \(\mathbb E[x_i^2x_j^2x_k^2]=1/[d(d+2)(d+4)]\) for distinct indices.

The marginal density of \(u\) is \(c_d(1-u^2)^{(d-3)/2}\) with \(c_d=\Gamma(d/2)/(\sqrt\pi\Gamma((d-1)/2))\). Define \(J_{2k+1}=c_d\int_a^1u^{2k+1}(1-u^2)^{(d-3)/2}\,du\). Elementary integration by parts gives
\[
J_1=\frac{c_d}{d-1}(1-s)^{(d-1)/2},\quad
\frac{J_3}{J_1}=\frac{2+(d-1)s}{d+1},\quad
\frac{J_5}{J_1}=\frac{(d-1)(d+1)s^2+4(d-1)s+8}{(d+1)(d+3)}.
\]
Conditional transverse spherical moments reduce the three unnormalized cross integrals to
\[
\begin{aligned}
I_0&=J_5-\left(\frac1d+\frac3{d+2}\right)J_3+\frac3{d(d+2)}J_1
=J_1\frac{(d-1)P_d(s)}{d(d+2)(d+3)},\\
I_1&=\frac{(d+3)J_3-(d+2)J_5-J_1}{d-1}
=J_1\frac{Q_d(s)}{d+3},\\
I_2&=\frac{4(J_1-2J_3+J_5)}{(d-1)(d+1)}
=J_1\frac{4(1-s)^2}{(d+1)(d+3)}.
\end{aligned}
\]
Dividing each \(I_j\) by the square root of the corresponding norms proves the three singular-value formulas. They are strictly positive for \(s<1\): \(Q_d(s)>0\) and \(P_d(s)=d(d+2)s^2-6s+3>0\), since its discriminant is negative for \(d\ge3\). The dimensions add up to \(\dim\mathcal H_2\), proving surjectivity and the source-kernel dimension.

To prove the **global** mode transitions rather than infer them numerically, divide all three branches by the common positive \(F_d(s)\) and call the resulting values \(A(s),B(s),C(s)\), in sector order \(0,1,2\). Directly, \(C(0)>A(0)>B(0)\). The ratio
\[
\frac{C(s)}{B(s)}=r_d\frac{1-s}{1+(d+2)s}
\]
is strictly decreasing and crosses one exactly at \(s_{21}\). Also \(A(s)=B(s)\) is the quadratic equation
\[
(d+2)(d+h_d)s^2-[6+h_d(d+1)]s+(3-h_d)=0.
\]
Its left side is positive at \(s=0\) and \(s=1\) but negative at \(s=1/(d+2)\), hence has two distinct roots, one on either side of that point. The key separation identity at the crossing \(s_{21}\), after setting \(r=r_d\) and using \(d+1=2/(r^2-2)\), is
\[
12\big(C(s_{21})^2-A(s_{21})^2\big)
=\frac{64(r-1)(r+1)^2(3-r^2)}{r^2(r+2)^3}>0.
\]
Because \(\sqrt2<r\le\sqrt{5/2}<\sqrt3\), this is strict. Thus the first \(A=B\) crossing occurs **before** \(s_{21}\), while the second occurs after; on \((s_{21},s_{10})\), \(B\) dominates both competitors. For \(s>s_{10}\), \(A>B>C\) in the top comparison, completing the global classification and all equality cases. The asymptotic limits follow by substituting \(s=z/d\) into the two crossing equations. Finally near \(s=1\), \(A\) is nonzero while \(B\) and \(C\) vanish to first and second order respectively after removing the common factor; taking \(A/C\) gives the stated condition-number coefficient.

## Verification
The standalone Python/SciPy script `verify.py` verifies exact polynomial reduction identities and the decisive crossing-factor identity symbolically, checks the branch inequalities across nine dimensions, and independently evaluates all three normalized cross integrals by adaptive one-dimensional quadrature at several cap sizes. Execute `python verify.py` from the directory containing this file. The script reports 308 successful exact, inequality, and numerical assertions. Such finite tests support reproducibility but do not replace the dimension-uniform proof above.

## Relationship to prior work
Simons, Dahlen and Wieczorek (arXiv:math/0408424v1, Section 5.1, especially equation (81)) give the classical fixed-azimuth spherical-cap concentration matrix in dimension three for a conventional harmonic band; the off-diagonal integrals are the natural precursor of the present cross-degree operator. Michel, Plattner and Seibert (arXiv:2103.14650v1, Section 3.2) develop a broader scalar/vector/tensor cap localization framework and its commuting operators. A 2026 note *Sharp sectoral concentration and complete eigenvalue ordering for two adjacent spherical degrees* analyzes adjacent-degree coupling on a **hemisphere** and therefore fixes \(s=0\); it does not determine the two cap-radius transitions. The present theorem is an explicit all-dimensional, variable-aperture, singular-spectrum and **cross-degree** optimization statement; it does not claim invention of Slepian matrices, harmonic order decomposition, or hemispherical adjacent-degree coupling.

## Limitations
The theorem is confined to the adjacent-degree pair \((2,3)\), a single axisymmetric polar cap, and exact spherical harmonics. It makes no assertion about arbitrary-degree adjacent pairs or nonaxisymmetric masks, and the singular values do not by themselves determine the largest eigenvalue of the full combined Slepian concentration matrix (whose diagonal blocks also vary with aperture). Literature searches and inspected primary sources are not an exhaustive priority proof; equivalent specialized cap-coupling computations may exist.

## References
1. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1, first posted 26 March 2021, Sections 3.2 and 4; https://arxiv.org/abs/2103.14650.
2. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1, first posted 31 August 2004, Section 5.1; https://arxiv.org/html/math/0408424v1.
3. *Sharp sectoral concentration and complete eigenvalue ordering for two adjacent spherical degrees*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-sectoral-concentration-and-complete-eigenvalue-ordering-fo--47d69d7de672.
