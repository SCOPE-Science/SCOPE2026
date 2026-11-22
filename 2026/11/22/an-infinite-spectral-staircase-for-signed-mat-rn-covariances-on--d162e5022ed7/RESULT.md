# An infinite spectral staircase for signed Matérn covariances on \(SU(2)\)

## Finding
Let \(G=SU(2)\), with normalized Haar measure and irreducible characters \(\chi_\ell\), indexed by \(\ell=0,1,\ldots\), so \(\chi_0=1\), \(\chi_1(g)=\operatorname{tr}(g)\), and \(\dim\chi_\ell=\ell+1\). Fix \(\lambda>0\). The squared-resolvent (Matérn-type) central kernel and its signed fundamental-character modulation are
\[
H_\lambda(g)=\sum_{\ell=0}^{\infty}\frac{\ell+1}{[\lambda+\ell(\ell+2)]^2}\chi_\ell(g),\qquad
K_{\lambda,b}(x,y)=H_\lambda(x^{-1}y)[1+b\chi_1(x^{-1}y)],\quad b\in\mathbb R.
\]
Put \(q=\lambda-1>-1\), define \(a_0(q)=0\) and \(a_y(q)=y/(y^2+q)^2\) for integers \(y\ge1\), and let
\[
R_y(q)=\frac{a_{y-1}(q)+a_{y+1}(q)}{a_y(q)},\qquad R_*(q)=\max_{y\ge1}R_y(q).
\]
The maximum exists and satisfies \(R_*(q)>2\). **The sharp positivity criterion** is
\[
\boxed{K_{\lambda,b}\text{ is of positive type on }SU(2)\ \Longleftrightarrow\ b\ge b_*(\lambda):=-1/R_*(\lambda-1).}
\]
The active Fourier obstruction follows an *unbounded, no-skipping staircase*: for each integer \(y\ge2\) there is a **unique** \(q_y>0\) satisfying \(R_{y+1}(q_y)=R_y(q_y)\); the sequence \(q_2<q_3<\cdots\) is strictly increasing and tends to infinity. If \(-1<q<q_2\), the maximizer is exactly \(y=2\). If \(q_y<q<q_{y+1}\), it is exactly \(y+1\). At \(q=q_y\) precisely the two adjacent indices \(y,y+1\) maximize. No other ties occur. Each step is described by a unique positive root of an explicit degree-six polynomial displayed in the proof.

For example, \(q_2=1.380930003817\ldots\) and \(q_3=3.371698165069\ldots\), corresponding to sharp mass parameters \(\lambda=2.380930003817\ldots\) and \(\lambda=4.371698165069\ldots\). As \(\lambda\to\infty\), the active index and sharp boundary obey
\[
 y_*(\lambda)\sim\sqrt{3(\lambda-1)},\qquad
 b_*(\lambda)=-\frac12+\frac{3}{8(\lambda-1)}+o(\lambda^{-1}),
\]
where either active index can be used at a tie. Equivalently, \(q_y\sim y^2/3\).

For **every** \(b\ge b_*(\lambda)\), the kernel is strictly positive definite on finite sets of distinct group points. Its RKHS is uniformly dense in \(C(SU(2))\) if and only if \(b>b_*(\lambda)\). At \(b=b_*(\lambda)\), exactly one irreducible Fourier block vanishes off the transition parameters, or exactly two adjacent blocks at a transition; all remaining infinitely many blocks are positive.

## Assumptions and scope
The Laplace--Beltrami/Casimir eigenvalue of \(\chi_\ell\) is normalized to \(\ell(\ell+2)\). The kernel is a continuous central function on the full non-Abelian group, not merely on its maximal torus. Positive type means positive semidefiniteness of \((K_{\lambda,b}(x_i,x_j))\) for every finite collection and complex coefficient vector. Strict positive definiteness refers to pairwise distinct group points; universality means uniform density of the associated complex RKHS in continuous complex-valued functions. All parameters \(\lambda>0\) and real \(b\) are included. The series converges uniformly because \(|\chi_\ell(g)|\le\ell+1\) and each summand is \(O(\ell^{-2})\) uniformly.

## Proof
**1. Fourier reduction.** The elementary \(SU(2)\) Clebsch--Gordan identity is \(\chi_1\chi_\ell=\chi_{\ell-1}+\chi_{\ell+1}\), with \(\chi_{-1}=0\). Consequently the character coefficient of degree \(\ell=y-1\) in the modulated kernel is
\[
 c_{y-1}=a_y(q)+b[a_{y-1}(q)+a_{y+1}(q)]=a_y(q)[1+bR_y(q)].
\]
The Peter--Weyl positive-type criterion makes \(K\) positive semidefinite exactly when all these coefficients are nonnegative. As \(R_y>0\), every nonnegative \(b\) works; for negative \(b\), the sharp condition is \(b\ge-1/\sup_yR_y\). The tail expansion \(R_y=2+12/y^2+O(y^{-4})\) for fixed \(q\) shows \(\sup R_y>2\) and is attained at a finite integer. In particular \(b_*>-1/2\).

**2. The two low-index observations.** For all \(\lambda>0\), direct simplification gives
\[
 R_2(\lambda-1)-R_1(\lambda-1)=
 \frac{6(18\lambda^4+172\lambda^3+459\lambda^2+684\lambda+432)}{\lambda^2(\lambda+3)^2(\lambda+8)^2}>0.
\]
For real \(x>1\), extend \(R_x(q)=[a(x-1)+a(x+1)]/a(x)\), where \(a(x)=x/(x^2+q)^2\) whenever the denominators are positive. Differentiation and clearing denominators yield
\[
 R_x'(q)=-\frac{8x(q+x^2)P(x^2,q)}{[q+(x-1)^2]^3[q+(x+1)^2]^3},
\]
where
\[
 P(u,q)=3u^3-3(q+1)u^2-(15q^2+18q+3)u-9q^3+q^2+13q+3.
\]
If \(-1<q\le0\), this expression is valid for \(x\ge2\); for \(u\ge4\), \(P_u\ge9u^2-6u-3>0\) and \(P(4,q)=135-107q-59q^2-9q^3\ge76\). Hence \(R_x\) strictly decreases for \(x\ge2\), and \(y=2\) uniquely maximizes the integer ratios. For \(q>0\), \(P(1,q)=-q(9q^2+14q+8)<0\). Its derivative in \(u\) is a quadratic with positive leading and negative constant coefficient, hence has one positive zero, a strict minimum; therefore \(P\) has exactly one zero in \((1,\infty)\). The continuous \(R_x\) increases to a unique maximum and then decreases on \(x\ge1\). Together with \(R_2>R_1\), this gives strict discrete unimodality, except possibly one equality of adjacent indices.

**3. Every adjacent crossing is unique.** For integers \(y\ge2\), put
\[
 D_y(q)=(q+y^2)^2(q+(y-1)^2)^2(q+(y+1)^2)^2(q+(y+2)^2)^2.
\]
Algebraic subtraction gives the exact identity
\[
 R_{y+1}(q)-R_y(q)=\frac{2(2y+1)T_y(q)}{D_y(q)},\qquad
 T_y(q)=\sum_{j=0}^6t_j(y)q^j,
\]
with explicit integer coefficients:
\[
\begin{aligned}
 t_6&=18,\\
 t_5&=4(21y^2+21y+19),\\
 t_4&=3(50y^4+100y^3+120y^2+70y+21),\\
 t_3&=6(20y^6+60y^5+92y^4+84y^3+70y^2+38y+1),\\
 t_2&=30y^8+120y^7+256y^6+348y^5+354y^4+268y^3+242y^2+146y+1,\\
 t_1&=-2y(y-1)(y+1)(y+2)(6y^6+18y^5+12y^4-6y^3+18y^2+24y+13),\\
 t_0&=-y(y-1)(y+1)(y+2)(6y^8+24y^7+30y^6+6y^5-21y^4-24y^3+y^2+10y+4).
\end{aligned}
\]
For every integer \(y\ge2\), \(t_0,t_1<0\) and \(t_2,\ldots,t_6>0\). For \(t_0\), note that \(30y^6-21y^4>0\) and \(24y^7-24y^3>0\); the remaining terms in its parenthesis are positive. The parenthesis of \(t_1\) is positive because \(12y^4-6y^3>0\). Thus the coefficients of \(T_y\), in descending order, have **exactly one sign change**. Descartes' rule, \(T_y(0)<0\), and \(T_y(q)\to+\infty\) as \(q\to+\infty\) prove one and only one positive zero \(q_y\). It is a sign-changing zero, so \(R_y>R_{y+1}\) below it and \(R_y<R_{y+1}\) above it.

**4. Ordered, exhaustive staircase.** At a crossing \(q=q_y\), strict discrete unimodality says \(R_{y+2}(q_y)<R_{y+1}(q_y)=R_y(q_y)\). Since the difference for \(y+1\) changes sign only at its own zero, \(q_y<q_{y+1}\). Consequently the active index starts at \(2\), steps upward by exactly one across each \(q_y\), and has only the asserted ties. There are infinitely many steps: for any fixed \(y\), the sign of \(R_{y+1}-R_y\) is positive when \(q\) is sufficiently large; hence no bounded set of indices can remain optimal.

**5. Large-mass law.** For \(u=qt\), the rescaled derivative polynomial satisfies \(q^{-3}P(qt,q)\to3(t-3)(t+1)^2\). The unique positive turning point therefore has \(u/q\to3\), and the maximizing integer \(y\) lies within one of the continuous maximizer in the large-\(q\) regime. Consequently \(y/\sqrt q\to\sqrt3\). Expanding the exact expression for \(R_y(q)\) with \(y^2/q\to t\) gives
\[
 R_y(q)=2+\frac{12(t-1)}{q(1+t)^2}+o(q^{-1}).
\]
At \(t=3\), \(R_*=2+3/(2q)+o(q^{-1})\), yielding the claimed \(b_*\) expansion and \(q_y\sim y^2/3\).

**6. Strict positivity and density.** At the sharp boundary, positivity coefficients vanish only at the finite set of maximizing degrees. For any finitely supported complex measure \(\mu=\sum_jv_j\delta_{x_j}\) with pairwise distinct atoms, zero kernel energy forces its matrix-valued Peter--Weyl coefficients to vanish for every degree except those finitely many holes. Such a measure equals a finite Fourier polynomial times Haar measure; it is therefore absolutely continuous. Since Haar measure on \(SU(2)\) is nonatomic, the only finitely supported absolutely continuous measure is zero. Thus all distinct-point Gram matrices are strictly positive definite. Uniform RKHS density, on the other hand, requires positive Fourier scalar weight at every irreducible representation: the missing character at the boundary is orthogonal to the entire RKHS, while all weights are positive strictly above the boundary. This proves the distinction.

## Verification
A standalone Python-standard-library checker, `su2_resolvent_checker.py`, verifies the rational difference identity in Step 3 for \(63\) integer indices at six exact rational values of \(q\), verifies the coefficient-sign pattern across those indices, exercises the character-coefficient identity at multiple mass and multiplier values, verifies transition brackets, and checks complementary finite positivity and staircase examples. It passed **3748 exact-rational assertions**. Symbolic polynomial simplification of the displayed derivative and difference identities was also performed. None of the finite comparisons replaces the universal analytic argument, and no independent audit is asserted.

## Relationship to prior work
Borovitskiy, Terenin, Mostowsky and Deisenroth (arXiv:2006.10160, first public 2020-06-17) derive spectral Matérn constructions on compact Riemannian manifolds. Azangulov, Smolensky, Terenin and Borovitskiy (arXiv:2208.14960, first public 2022-08-31), especially Sections 3--4 and its character appendix, give a constructive compact-Lie-group kernel framework including \(SU(2)\) characters and Matérn spectral weights. These works supply the parent kernel and standard harmonic background; the inspected sections do not derive its signed fundamental-character positivity boundary or its unbounded mode-switching law. The published result “Finite positive-type and universality cones for character-polynomial Abel kernels on \(SU(2)\)” (2026) explicitly concerns **geometric Abel weights** \((\ell+1)r^\ell\), whose affine coefficient tails have finitely many positivity facets. The squared-resolvent weights here instead give infinitely many sharp, different active spectral indices and are not a specialization of that theorem. Related signed-geodesic circle positivity staircases concern the Abelian circle and different spectral weights; they do not imply this non-Abelian Matérn-resolvent law. Classical equivalences under resolvent or Chebyshev terminology remain a priority risk.

## Limitations
The theorem concerns the squared resolvent, one fundamental-character multiplier, and the indicated Casimir normalization. It does not give the full polycharacter admissibility region, cover all Matérn orders, or establish a new result about arbitrary compact groups. The algebraic switching parameters are specified uniquely, not in radicals; approximate decimals are informational only. Exhaustive external literature discovery and independent validation have not been established.

## References
1. V. Borovitskiy, A. Terenin, P. Mostowsky, M. P. Deisenroth, *Matérn Gaussian processes on Riemannian manifolds*, first preprint 2020-06-17, https://arxiv.org/abs/2006.10160.
2. I. Azangulov, A. Smolensky, A. Terenin, V. Borovitskiy, *Stationary Kernels and Gaussian Processes on Lie Groups and their Homogeneous Spaces I: the compact case*, first preprint 2022-08-31, https://arxiv.org/abs/2208.14960.
3. *Finite positive-type and universality cones for character-polynomial Abel kernels on \(SU(2)\)*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-finite-positive-type-and-universality-cones-for-character-polyno--5666d49c8fcc.
4. *The exact every-mode staircase for even-harmonic geodesic-exponential circle covariances*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-every-mode-staircase-for-even-harmonic-geodesic-exponentia--027cc81ac50f.
