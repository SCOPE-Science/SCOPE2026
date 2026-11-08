# Two-band quadratic Slepian spectrum for simplex-centred cap masks and an isolated tetrahedral isotropy

## Finding

For every integer \(d\ge3\), place \(d+1\) spherical caps at the vertices of a regular simplex on \(S^{d-1}\), and take their common threshold \(a\) in the disjoint-interiors range
\[
\sqrt{\frac{d-1}{2d}}\le a<1.
\]
The spatial concentration operator on the **pure complex degree-two spherical harmonic space** has two explicit eigenvalue branches, which can coincide, with specified multiplicities. Define
\[
\begin{aligned}
c_d&=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},\\
m_d(a)&=c_d\int_a^1(1-t^2)^{(d-3)/2}\,dt,\\
b_d(a)&=\frac{c_d(d+4)}{(d-1)(d+1)}\,a(1-a^2)^{(d-1)/2}
\left(a^2-\frac3{d+4}\right).
\end{aligned}
\]
Then the full eigenvalue multiset is
\[
\begin{aligned}
\lambda_{\mathrm{std}}&=(d+1)(m_d-b_d)+\frac{(d+2)(d^2-1)}{2d}\,b_d,
&\text{multiplicity }d,\\
\lambda_{\mathrm{orth}}&=(d+1)(m_d-b_d),
&\text{multiplicity }\frac{(d+1)(d-2)}2.
\end{aligned}
\]
All eigenvalues lie strictly between zero and one. The two bands coalesce at an admissible threshold exactly when \(d=3\), at the unique **interior** value
\[
a_\ast=\sqrt{3/7},\qquad
C_{3,a_\ast}=2(1-\sqrt{3/7})\,I_{\mathcal H_2}.
\]
For \(d=4\), the formal coalescence is only at the cap-touching endpoint \(a=\sqrt{3/8}\); for every \(d\ge5\) no coalescence occurs, even including that endpoint. In dimension three, the degree-three harmonic \(x_1x_2x_3\) has a nonzero integral over this isotropic tetrahedral mask, namely \(8/(147\sqrt3)\). Thus perfect localization isotropy on degree two does not mean the mask is spherical-harmonic balanced at all degrees.

## Assumptions and scope

Use probability surface measure \(\sigma\) on \(S^{d-1}\). Fix \(v_1,\ldots,v_{d+1}\in S^{d-1}\) with \(v_i\cdot v_j=-1/d\) for \(i\ne j\). Set
\[
E_{d,a}=\bigcup_{i=1}^{d+1}\{x\in S^{d-1}:x\cdot v_i\ge a\}.
\]
For the given threshold range the interiors of these caps are disjoint: the angular separation is \(\arccos(-1/d)\), and two caps of angular radius \(\arccos a\) cannot overlap in positive area when twice their radius is at most that separation. Boundary tangency makes no difference to area integrals. The vector space
\[
\mathcal H_2=\{q_A(x)=x^{\mathsf T}Ax:\ A=A^{\mathsf T}\in\mathbb C^{d\times d},\ \operatorname{tr} A=0\}
\]
is equipped with its full-sphere complex \(L^2\) inner product. Let \(P_2\) be the orthogonal projection onto this space and
\[
C_{d,a}=P_2 M_{\mathbf 1_{E_{d,a}}}P_2\big|_{\mathcal H_2}.
\]
In particular, the theorem concerns a fixed, pure degree-two subspace and not the usual low-pass sum of degrees zero through two. For \(d=3\), orient the simplex as \(v_i\in\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}/\sqrt3\) for the cubic-moment assertion.

## Proof

**1. Spherical quadratic normalization and cap decomposition.** For real trace-free symmetric \(A\), uniform spherical fourth moments yield
\[
\int_{S^{d-1}}q_A(x)^2\,d\sigma(x)=\frac{2}{d(d+2)}\operatorname{tr}(A^2).
\]
For a single cap with pole \(v\), write \(t=x\cdot v\), \(x=tv+\sqrt{1-t^2}\,y\), with uniform \(y\in S^{d-2}\subset v^\perp\). The density of \(t\) is \(c_d(1-t^2)^{(d-3)/2}\). Conditional moments of \(y\) and the trace-free condition give
\[
\int_{x\cdot v\ge a}q_A(x)^2\,d\sigma(x)
=\alpha\operatorname{tr}(A^2)+\gamma\lVert Av\rVert^2+b_d(a)(v^{\mathsf T}Av)^2,
\]
where, using \(J_j=c_d\int_a^1t^j(1-t^2)^{(d-3)/2}\,dt\),
\[
\alpha=\frac{2(J_0-2J_2+J_4)}{(d-1)(d+1)},\qquad
\gamma=\frac{4(J_2-J_4)}{d-1}-\frac{4(J_0-2J_2+J_4)}{(d-1)(d+1)},
\]
\[
b_d=J_4-\frac{6(J_2-J_4)}{d-1}
+\frac{3(J_0-2J_2+J_4)}{(d-1)(d+1)}.
\]
To evaluate the last integral exactly, simplify its integrand to
\[
\frac{(d+2)(d+4)}{(d-1)(d+1)}
\left(t^4-\frac{6t^2}{d+4}+\frac3{(d+2)(d+4)}\right).
\]
Differentiating \(t(1-t^2)^{(d-1)/2}(t^2-3/(d+4))\) proves the closed formula for \(b_d(a)\) in the finding; the primitive vanishes at \(t=1\). The derivation is polynomial and remains valid for \(d=3\).

**2. The simplex frame eliminates all but two sectors.** The tight-frame identity is
\[
\sum_{i=1}^{d+1}v_iv_i^{\mathsf T}=\frac{d+1}{d}I_d.
\]
Consequently, the \(\alpha\)- and \(\gamma\)-terms add to a scalar quadratic form. On the trace-free symmetric matrix space introduce
\[
B_i=v_iv_i^{\mathsf T}-I_d/d.
\]
Their Frobenius Gram matrix has diagonal \((d-1)/d\) and off-diagonal \(-(d-1)/d^2\). It has eigenvalue \((d^2-1)/d^2\) with multiplicity \(d\) and one zero eigenvalue. Hence the operator \(A\mapsto\sum_i\langle A,B_i\rangle B_i\) has that same nonzero eigenvalue with multiplicity \(d\), and eigenvalue zero with multiplicity
\[
\frac{(d-1)(d+2)}2-d=\frac{(d+1)(d-2)}2.
\]
After division by the full-sphere normalization \(2/[d(d+2)]\), the extra contribution of the \(b_d\)-term in the first sector equals \(b_d(d+2)(d^2-1)/(2d)\). To identify the common scalar, use the degree-two addition theorem: the concentration trace equals \(\dim(\mathcal H_2)\,\sigma(E_{d,a})\), and disjointness gives \(\sigma(E_{d,a})=(d+1)m_d(a)\). Comparing with the trace of the rank-\(d\) correction identifies the second eigenvalue as \((d+1)(m_d-b_d)\). Polarization of the real matrix calculation proves the same formulas for the stated complex space.

**3. The unique isotropy transition.** Since \(c_d>0\), \(a>0\), and \(a<1\), the spectral gap has the sign of \(a^2-3/(d+4)\), so coalescence occurs only at \(a^2=3/(d+4)\). The exact threshold comparison is
\[
\frac3{d+4}-\frac{d-1}{2d}=
-\frac{(d-4)(d+1)}{2d(d+4)}.
\]
It is positive exactly for \(d=3\), zero for \(d=4\), and negative for \(d\ge5\). For \(d=3\), \(c_3=1/2\), and the cap mass is \(m_3(a)=(1-a)/2\). Substituting \(b_3(a_\ast)=0\) yields the stated scalar. Each eigenvalue lies in \((0,1)\) because \(q_A\) is nonzero real-analytic on every nonempty open cap and on its open complement: its restricted-to-full energy ratio is strictly between zero and one.

**4. Why this isotropy is degree-selective.** On \(S^2\), \(H(x)=x_1x_2x_3\) is a spherical harmonic of degree three. The Funk--Hecke averaging identity implies
\[
\int_{x\cdot v\ge a}H(x)\,d\sigma(x)=H(v)\,
\frac{(1-a^2)(5a^2-1)}{16}.
\]
For the oriented tetrahedron in the assumptions, \(\sum_iH(v_i)=4/(3\sqrt3)\). At \(a^2=3/7\), this gives \(8/(147\sqrt3)\ne0\), completing the distinction.

## Verification

Run `python check.py` with Python 3, NumPy, SciPy and SymPy; the included standalone program requires no data downloads. The run produced `SIMPLEX_CAP_H2_CHECKS_PASS 260`. It checks the symbolic primitive, direct one-dimensional quadrature and trace identities for dimensions 3 through 20, simplex Gram eigenvalues, positivity and the crossing threshold, and direct spherical-cap quadrature of the full five-by-five concentration matrix in dimension three at four apertures including \(a_\ast\). The cubic moment is separately integrated. These finite checks corroborate the universal proof above and do not constitute an exhaustive proof in every dimension.

## Relationship to prior work

Simons, Dahlen and Wieczorek established the spherical Slepian concentration eigenproblem for arbitrary spatial regions and analyzed the special rotationally symmetric cap case. Roddy and McEwen developed Slepian wavelets for incomplete spherical regions. Those general frameworks are prerequisites, not new claims here. The distinguishing conclusion is the exact *pure degree-two* simplex-cap spectral decomposition in arbitrary dimension, and especially the isolated disjoint tetrahedral mask acting as a scalar on the complete degree-two harmonic space despite its nonzero cubic-harmonic moment. Pasqual’s 2014 analysis of spherical loudspeaker arrays examines the same tetrahedral four-cap geometry, but its linear harmonic radiation amplitudes are not the quadratic Slepian restriction Gram. Studies of overlap volumes of simplex-centred caps concern geometric coverage, not this spectral compression. An earlier equivalent closed formula in specialized harmonic-analysis or representation-theoretic literature remains a priority risk.

## Limitations

Only regular-simplex cap centres, common cap threshold in the pairwise-disjoint-interior range, the degree-two harmonic component, and probability surface measure are covered. The calculation does not provide spectra for overlapping cap families, full low-pass spherical harmonic spaces, arbitrary cap weights, finite noisy sampling, or higher-degree concentration. 

## References

- F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, first publicly posted August 31, 2004, https://arxiv.org/abs/math/0408424 (in particular Section 4, arbitrary-region eigenproblem, and Section 5, single axisymmetric cap).
- P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, first publicly posted June 3, 2021, https://arxiv.org/abs/2106.02023 (general arbitrary-region Slepian construction).
- A. M. Pasqual, *Spherical harmonic analysis of the sound radiation from omnidirectional loudspeaker arrays*, *Journal of Sound and Vibration* 333 (2014), 4930–4941, https://doi.org/10.1016/j.jsv.2014.05.006 (same tetrahedral cap geometry, different acoustic operator).
