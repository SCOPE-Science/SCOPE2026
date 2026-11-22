# Reentrant Dirichlet concentration of cubic spherical harmonics on antipodal caps

## Finding

Let \(d\ge3\) be an integer, and let \(\mathcal H_3(S^{d-1})\) be the real or complex exact-degree-three spherical-harmonic space. Given \(0<a<1\), restrict tangential-gradient energy to the two antipodal caps \(\Omega_a=\{x\in S^{d-1}:|x_d|\ge a\}\):
\[
\mathcal R_a(f)=\frac{\int_{\Omega_a}|\nabla_S f|^2\,d\sigma}{\int_{S^{d-1}}|\nabla_S f|^2\,d\sigma},\qquad 0\ne f\in\mathcal H_3(S^{d-1}).
\]
Put \(s=a^2\), \(t_1=1/(d+2)\), and \(t_2=(2d+5)/(3(d+2))\). There is a **reentrant optimal symmetry**: the maximizing harmonic subspace is precisely the transverse-order-one space \(V_1\) for \(0<s<t_1\), the zonal space \(V_0\) for \(t_1<s<t_2\), and \(V_1\) again for \(t_2<s<1\). At either interior transition, exactly \(V_0\oplus V_1\) maximizes, of dimension \(d\). Both transitions are strict off their thresholds.

There is one additional, nonmaximal spectral exchange at \(s_0=1/[3(d+2)]\). In decreasing order, the four full Dirichlet concentration eigenbranches are
\[
\begin{array}{c|c}
0<s<s_0&1>2>0>3\\
s_0<s<t_1&1>0>2>3\\
t_1<s<t_2&0>1>2>3\\
t_2<s<1&1>0>2>3.
\end{array}
\]
The branch \(3\) is always uniquely lowest. For the ratio of largest to smallest eigenvalues, as \(s\uparrow1\),
\[
\frac{\lambda_{\max}}{\lambda_{\min}}\sim\frac{(d+1)^2(d+3)}{6(d+2)}(1-s)^{-2}.
\]
All listed statements concern the gradient (Dirichlet) observable, **not** the scalar harmonic value-energy concentration problem.

## Assumptions and scope

The sphere has its round metric and any rotation-invariant surface-measure normalization. The operator is the unique positive self-adjoint operator with Rayleigh quotient \(\mathcal R_a\), using the Dirichlet inner product on \(\mathcal H_3\); since \(-\Delta_S f=3(d+1)f\), that inner product is \(3(d+1)\) times the full-sphere \(L^2\) inner product. We assume \(d\ge3\) and strictly interior \(0<a<1\); at \(a=0\) and \(a=1\), all branches tie. The complex case is obtained by complexification.

Writing \(x=(\sqrt{1-z^2}\,u,z)\) with \(u\in S^{d-2}\), let \(V_k\) be the restricted homogeneous cubic harmonic polynomials of transverse harmonic order \(k\in\{0,1,2,3\}\). Up to positive factors depending only on \(d\) and angular normalization, their latitude profiles are
\[
F_0=z^3-\frac{3z}{d+2},\quad F_1=\sqrt{1-z^2}\left(z^2-\frac1{d+2}\right),\quad F_2=z(1-z^2),\quad F_3=(1-z^2)^{3/2}.
\]
These profiles multiply transverse degree-\(k\) harmonics. The sector multiplicities are \(1\), \(d-1\), \(d(d-1)/2-1\), and \((d-1)(d-2)(d+3)/6\), respectively. Their sum equals \(d(d-1)(d+4)/6=\dim\mathcal H_3(S^{d-1})\).

## Proof

**Sector reduction.** The ambient homogeneous cubics generating the sectors are, with \(y\in\mathbb R^{d-1}\) and \(z=x_d\), the spaces generated respectively by \(z^3-3z|y|^2/(d-1)\) (equivalently \(z^3-3z/(d+2)\) on the sphere after scaling), \((z^2-|y|^2/(d+1))H_1(y)\), \(zH_2(y)\), and \(H_3(y)\), for transverse homogeneous harmonics \(H_k\). More explicitly, the zonal ambient harmonic is \(z^3-3z|y|^2/(d-1)\); on the sphere this equals \((d+2)/(d-1)\,[z^3-3z/(d+2)]\). For the transverse-order-one sector, the ambient harmonic \((z^2-|y|^2/(d+1))H_1(y)\) is proportional on the sphere to \((z^2-1/(d+2))H_1(y)\). Orthogonality follows from transverse harmonic degrees, and the dimension identity proves completeness. Invariance of the caps under \(O(d-1)\) makes each sector a scalar eigenspace.

**Exact energy densities.** Put \(c=1/(d+2)\) and \(u=z^2\) (the symbol \(u\) in this paragraph denotes the squared latitude). For a normalized transverse harmonic of order \(k\), the pointwise transverse-sphere-averaged tangential energy is \((1-z^2)|F_k'(z)|^2+k(k+d-3)|F_k(z)|^2/(1-z^2)\). Hence the four nonnegative polynomial densities in \(u\) are
\[
\begin{aligned}
g_0(u)&=9(1-u)(u-c)^2,\\
g_1(u)&=u(2+c-3u)^2+(d-2)(u-c)^2,\\
g_2(u)&=(1-u)[1+2(d-4)u+9u^2],\\
g_3(u)&=3(d+3u)(1-u)^2.
\end{aligned}
\]
Let \(Z_d=\int_0^1(1-z^2)^{(d-3)/2}dz\), let \(D_k=Z_d^{-1}\int_0^1g_k(z^2)(1-z^2)^{(d-3)/2}dz\), and set
\[
\lambda_k(a)=\frac{1}{D_kZ_d}\int_a^1 g_k(z^2)(1-z^2)^{(d-3)/2}\,dz.
\]
The beta-moment identity \(\mathbb E[z^{2j}]=(1/2)_j/(d/2)_j\) yields exactly
\[
\begin{aligned}
D_0&=\frac{18(d-1)(d+1)}{d(d+2)^2(d+4)},&
D_1&=\frac{6(d-1)(d+1)^2}{d(d+2)^2(d+4)},\\
D_2&=\frac{3(d-1)(d+1)^2}{d(d+2)(d+4)},&
D_3&=\frac{3(d-1)(d+1)^2(d+3)}{d(d+2)(d+4)}.
\end{aligned}
\]
These are positive for all admissible dimensions.

**Polynomial gap certificates.** Define \(B_d(a)=a(1-a^2)^{(d-1)/2}/Z_d>0\) for \(0<a<1\). Writing \(s=a^2\), direct integration or differentiation of the following right sides gives \(\lambda_i-\lambda_j=B_d(a)Q_{ij}(s)\):
\[
\begin{aligned}
Q_{01}(s)&=-\frac{d(d+4)}{6(d-1)(d+1)^2}[(d+2)s-1][3(d+2)s-(2d+5)],\\
Q_{02}(s)&=\frac{d(d+4)}{6(d+1)^2}(1-s)[3(d+2)s-1],\\
Q_{03}(s)&=\frac{d(d+4)}{2(d-1)(d+1)^2(d+3)}(1-s)[(d^3+4d^2+7d+6)s+d^2-3],\\
Q_{12}(s)&=\frac{d(d+4)}{6(d-1)(d+1)^2}[9(d+2)s^2+(d^2-8d-23)s+d+6],\\
Q_{23}(s)&=\frac{d(d+2)(d+4)}{3(d-1)(d+1)^2(d+3)}(1-s)(2d+9s-3).
\end{aligned}
\]
The common integrating-factor identity, valid separately for each difference, is
\[
(1-ds)Q_{ij}(s)+2s(1-s)Q_{ij}'(s)
=-\left[\frac{g_i(s)}{D_i}-\frac{g_j(s)}{D_j}\right].
\]
It proves each gap formula: differentiate \(B_d(a)Q_{ij}(a^2)\) in \(a\), compare it with the negative cap-integral derivative, and use vanishing of both sides at \(a=1\). This is a polynomial identity for unrestricted real \(d\ge3\), not a finite enumeration.

**Signs and equality cases.** The first gap changes sign precisely at \(s=t_1,t_2\); the second gap changes precisely at \(s=s_0\). The third and fifth gaps in the display are always positive. The fourth gap is positive: for \(d\ge11\) all three polynomial coefficients are positive; for integer \(3\le d\le10\) its discriminant \((d^2-8d-23)^2-36(d+2)(d+6)\) is strictly negative and its quadratic leading coefficient is positive. Thus \(\lambda_1>\lambda_2>\lambda_3\) everywhere, and \(\lambda_0>\lambda_3\) everywhere. The sign changes of \(Q_{01}\) and \(Q_{02}\) give exactly the four strict ranking intervals in the finding, with precisely the stated eigenspace sums at each boundary.

**Thin-cap condition number.** At \(s\uparrow1\), \(\lambda_1\) is largest and \(\lambda_3\) smallest. Since \(g_1(1)=(d-1)(d+1)^2/(d+2)^2\) while \(g_3(s)=3(d+3s)(1-s)^2\), integration at the endpoint gives \(\lambda_1\sim g_1(1)(1-s)^{(d-1)/2}/[(d-1)D_1Z_d]\) and \(\lambda_3\sim 3(1-s)^{(d+3)/2}/(D_3Z_d)\). Dividing yields the stated sharp coefficient.

## Verification

The standalone `checker.py` checks all four beta-moment normalizations, all six polynomial difference differential identities, the positivity discriminants for integers \(3\le d\le10\), and independent numerical quadrature at 36 dimension/aperture combinations across six dimensions, giving **234 passed checks**. The finite tests are supplementary; the polynomial identities and analytic sign argument establish the all-dimensional result. Reproduction: `python checker.py` with SymPy and SciPy installed.

## Relationship to prior work

Plattner and Simons (2013, arXiv:1306.3201) develop tangential vector Slepian concentration and polar-cap block matrices on the two-sphere, including tangential vector harmonics generated by scalar gradients, but do not state the present pure cubic all-dimensional double-cap phase diagram. Michel, Plattner, and Seibert (2021, arXiv:2103.14650) provide a general scalar/vector/tensor Slepian framework and commuting operators, mainly for single spherical caps, without the present explicit gradient-cap ordering. These are substantive frameworks within which the present problem can be posed, but their general matrix representations alone do not imply the closed transition formulas without additional calculations.

The published scalar pure-cubic antipodal-cap concentration theorem (published-finding corpus, 2026/10/26, finding `45d96c049f3f`) has cutoffs \(1/(d+2)\) and \(3/(d+2)\) for **value energy**, with top symmetry \(2\to1\to0\), in contrast to the present **gradient energy** with thresholds \(1/(d+2)\) and \((2d+5)/(3(d+2))\), and top symmetry \(1\to0\to1\). The shared first cutoff does not make the distinct observable or second cutoff a corollary. The earlier pure-degree-two gradient theorem has a different harmonic space. These comparisons identify overlap and differences; they do not establish global priority.

## Limitations

The theorem concerns only the pure cubic degree, a pair of equal antipodal caps, the intrinsic tangential gradient, and dimensions \(d\ge3\). It does not claim ordinary scalar \(L^2\) concentration, optimality among varying regions, mixed bandwidths, or extension to arbitrary vector fields. A more specialized unindexed result might cover this exact statement. Independent external mathematical auditing has not occurred.

## References

1. A. Plattner and F. J. Simons, *Spatiospectral concentration of vector fields on a sphere*, arXiv:1306.3201 (first posted 2013-06-13), Applied and Computational Harmonic Analysis **36** (2014), 1–22. https://arxiv.org/abs/1306.3201
2. V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first posted 2021-03-26). https://arxiv.org/abs/2103.14650
3. *Two sharp concentration transitions for cubic spherical harmonics on antipodal caps*, published research result (2026-10-26). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-sharp-concentration-transitions-for-cubic-spherical-harmonic--45d96c049f3f
