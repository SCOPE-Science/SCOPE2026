# Two independently tunable periods with a frozen third clock in quartic three-circle flows

## Finding

Fix any three pairwise disjoint circles
\[
C_i=\{(x,y):x^2+y^2=r_i^2\}\quad(i=1,2),\qquad
C_3=\{(x,y):(x-1)^2+y^2=s^2\},
\]
where \(0<r_1<r_2\), \(s>0\), and neither concentric circle intersects or touches the off-centre circle. Fix any nonzero \(\lambda,\beta\in\mathbb R\). In the quartic polynomial family defined below, the period \(T_3\) of \(C_3\) is completely independent of the parameters \(\alpha,\gamma\). Nevertheless, for all sufficiently large positive \(\gamma\), at \(\alpha=0\) the map
\[
(\alpha,\gamma)\longmapsto(T_1,T_2)
\]
has a nonsingular Jacobian. Every prescribed circle is then a hyperbolic limit cycle; these properties persist under sufficiently small perturbations of \(\alpha,\gamma\). Thus an open neighborhood of the two original-time periods \((T_1,T_2)\) can be independently attained **with all three exact circles, the third original-time period, and the polynomial degree four fixed**.

The explicit leading Jacobian coefficient is
\[
\lim_{\gamma\to+\infty}\gamma^4
\det D_{(\alpha,\gamma)}(T_1,T_2)\big|_{\alpha=0}
=I(r_1)I(r_2)\big(\rho(r_1)-\rho(r_2)\big)\ne0,
\]
where, with \(a(r)=1+r^2-s^2\) and \(d(r)=\sqrt{a(r)^2-4r^2}\),
\[
I(r)=\frac{2\pi}{d(r)},\qquad
\rho(r)=\frac{a(r)-\operatorname{sgn}(a(r))d(r)}{2}.
\]

## Assumptions and scope

Set \(f_i=x^2+y^2-r_i^2\) for \(i=1,2\) and \(f_3=(x-1)^2+y^2-s^2\). The pairwise-disjoint hypothesis is equivalent to \(|1+r_i^2-s^2|>2r_i\) for each \(i=1,2\). In the degree-at-most-four normal form from Cao and Llibre [1], define
\[
B=\lambda(x^2+y^2)+\alpha x+\beta y+\gamma,\qquad
A=\lambda f_1f_2-f_3B,
\]
and the planar autonomous ODE
\[
\dot x=yA,\qquad \dot y=\lambda f_1f_2-xA.
\]
We fix \(\lambda\ne0\), \(\beta\ne0\), vary only real \(\alpha,\gamma\), and take \(\gamma\) sufficiently large and positive. Here every \(T_i\) is the least *positive physical-time* period of the flow restricted to \(C_i\), not a reparametrized angular period. No claim of absence of additional limit cycles elsewhere is made.

## Proof

**1. Circular angular speeds and the hyperbolic region.** Direct differentiation gives
\[
\dot f_1=\dot f_2=2\lambda yf_1f_2,\qquad \dot f_3=2yf_3B.
\]
On \(C_i\) for \(i=1,2\), polar angle satisfies \(\dot\theta=f_3B\); on \(C_3\), its angle about \((1,0)\) satisfies \(\dot\phi=-\lambda f_1f_2\). In particular, changing \(\alpha\) or \(\gamma\) cannot change the third angular speed or \(T_3\). The exact hyperbolicity and isolation criterion proved for this normal form in [1, Theorem B, Proposition 4.3] is
\[
\lambda\beta\ne0,\qquad
|\lambda r_i^2+\gamma|>r_i\sqrt{\alpha^2+\beta^2}\quad(i=1,2).
\]
With \(\lambda,\beta\) fixed and nonzero, these strict inequalities hold throughout a neighborhood of \((0,\gamma)\) for all sufficiently large positive \(\gamma\). The cited criterion also ensures that the vector field is coprime and has **exact degree four**.

**2. Period integrals and a frozen third period.** Write \(a_i=1+r_i^2-s^2\). Since \(f_3\) has constant nonzero sign on \(C_i\) and \(B>0\) there for our parameters,
\[
T_i(\alpha,\gamma)
=\int_0^{2\pi}\frac{d\theta}{|a_i-2r_i\cos\theta|\big[\gamma+\lambda r_i^2+r_i(\alpha\cos\theta+\beta\sin\theta)\big]}
\quad(i=1,2).
\]
This integral is smooth in both parameters on the admissible open neighborhood. The third period is explicitly
\[
T_3=\int_0^{2\pi}\frac{d\phi}{|\lambda f_1(1+s\cos\phi,s\sin\phi) f_2(1+s\cos\phi,s\sin\phi)|}.
\]
In fact, letting \(b_i=1+s^2-r_i^2\), \(h(b)=\operatorname{sgn}(b)/\sqrt{b^2-4s^2}\), and \(\Delta=r_2^2-r_1^2>0\), partial fractions and the standard cosine integral give
\[
T_3=\frac{2\pi}{|\lambda|\Delta}\,|h(b_2)-h(b_1)|,
\]
which is independent of \(\alpha,\beta,\gamma\). The square roots exist since the circles are disjoint.

**3. The two-parameter Jacobian.** For either \(r\in\{r_1,r_2\}\), write \(a=a(r)\) and \(w_r(\theta)=|a-2r\cos\theta|^{-1}\). At \(\alpha=0\), differentiation under the integral gives
\[
\partial_\gamma T(r)
=-\int_0^{2\pi}\frac{w_r(\theta)\,d\theta}
{[\gamma+\lambda r^2+\beta r\sin\theta]^2},
\]
\[
\partial_\alpha T(r)
=-r\int_0^{2\pi}\frac{\cos\theta\, w_r(\theta)\,d\theta}
{[\gamma+\lambda r^2+\beta r\sin\theta]^2}.
\]
For \(\gamma\to+\infty\), uniformly on the compact integration domain, the denominator inverse square is \(\gamma^{-2}(1+O(\gamma^{-1}))\). Consequently,
\[
\partial_\gamma T(r)=-\gamma^{-2}I(r)+O(\gamma^{-3}),\qquad
\partial_\alpha T(r)=-\gamma^{-2}I(r)\rho(r)+O(\gamma^{-3}),
\]
where \(I(r)=\int w_r\) and \(\rho(r)=r\int\cos\theta\,w_r/I(r)\). The standard full-circle integral yields
\[
\int_0^{2\pi}\frac{d\theta}{|a-2r\cos\theta|}
=\frac{2\pi}{\sqrt{a^2-4r^2}},
\]
while the identity \(2r\cos\theta=a-(a-2r\cos\theta)\) gives
\[
r\int_0^{2\pi}\frac{\cos\theta\,d\theta}{|a-2r\cos\theta|}
=\tfrac12\big(aI(r)-2\pi\operatorname{sgn}(a)\big).
\]
These establish the displayed formulas for \(I,\rho\). Taking the determinant of the two derivative rows proves
\[
\det D_{(\alpha,\gamma)}(T_1,T_2)
=\frac{I(r_1)I(r_2)(\rho(r_1)-\rho(r_2))}{\gamma^4}+O(\gamma^{-5}).
\]

**4. A global geometric separation lemma.** It remains to show \(\rho(r_1)\ne\rho(r_2)\) for every admissible geometry, not just for generic radii. The only possible radii disjoint from \(C_3\) lie in the following ranges: \(0<r<1-s\) if \(s<1\), \(0<r<s-1\) if \(s>1\), or \(r>1+s\) for every \(s>0\). On the first range, \(a>2r\), \(0<\rho<1\); on the second, \(a<-2r\), \(\rho<0\); on the last, \(a>2r\) and \(\rho>1\). The ranges of \(\rho\) for disconnected branches are thus disjoint. On each branch the quadratic identity
\[
\rho(r)^2-a(r)\rho(r)+r^2=0
\]
gives
\[
\rho'(r)=\frac{2r(\rho(r)-1)}{2\rho(r)-a(r)}.
\]
Here \(2\rho-a=-\operatorname{sgn}(a)d\ne0\); also \(\rho\ne1\), since substituting \(\rho=1\) in the quadratic would give \(s^2=0\), contrary to \(s>0\). Thus \(\rho'\) never vanishes on any branch, and \(\rho\) is strictly monotone there. Two distinct admissible radii cannot have equal \(\rho\).

The limiting Jacobian coefficient is therefore nonzero. For all sufficiently large positive \(\gamma\), its determinant is nonzero, and the inverse-function theorem gives a local diffeomorphism from \((\alpha,\gamma)\) to \((T_1,T_2)\). The strict hyperbolicity conditions persist in a small enough neighborhood, while \(T_3\) stays fixed. This proves the finding.

## Verification

The standalone `check.py` evaluates the three original-time period integrals, the two exact derivative integrals, the Jacobian, and the asymptotic Jacobian coefficient. It checks four geometries including exterior and nested configurations. With \(s=1/4\), \(r_1=1/4\), \(r_2=1/2\), \(\lambda=1\), \(\beta=1/10\), \(\alpha=0\), \(\gamma=10\), it obtains
\[
T_1\approx0.7210154773762412,\quad T_2\approx0.9571609163754547,\quad
T_3\approx13.6299740931427470,
\]
and
\[
\det D_{(\alpha,\gamma)}(T_1,T_2)\approx-0.00138203373860404.
\]
Execute `python check.py` with Python 3, `mpmath` and `sympy`. These finite-precision comparisons are auxiliary; the global nonvanishing statement is proved analytically above.

## Relationship to prior work

Cao and Llibre [1, Theorem B and Proposition 4.3] derive the complete quartic normal form and the hyperbolic limit-cycle criterion for these three fixed circles. In particular their angular equations are the starting point of this work. The additional assertion established here is **rank-two local period control with a frozen third physical period**, valid for every admissible two-concentric geometry, together with its explicit nonvanishing Jacobian limit and geometric injectivity argument.

Margalef-Bentabol and Peralta-Salas [2, Theorems 1.2 and 2.1] establish prescribed-period realization for arbitrary configurations using a polynomial construction with a degree upper bound depending on the number of cycles and primary components. Their statement does not establish this fixed degree-four submersion within the specific normalized Cao–Llibre family, nor its frozen third clock. The theorem is fully compatible with the general existence result, not a contradiction or a claim to arbitrary independent control of all three periods.

## Limitations

The attainable period pairs form only a neighborhood about the constructed pair, **not all** of \((0,\infty)^2\). The third period is held fixed; no simultaneous arbitrary prescription of three periods, Floquet multipliers, or stability types is asserted. The geometric disjointness is strict and fails at tangency. The proof uses \(\beta\ne0\) and sufficiently large positive \(\gamma\). It classifies neither other possible periodic orbits nor global period-map injectivity. The numerical checker is not a substitute for the analytic argument. Historical literature outside the inspected sources may contain related period-control statements.

## References

[1] Chen Cao and Jaume Llibre, *Quartic polynomial differential systems with three disjoint invariant circles*, arXiv:2611.05696v1 (first public November 3, 2026), especially Theorem B, §4, Proposition 4.3. https://arxiv.org/abs/2611.05696

[2] Juan Margalef-Bentabol and Daniel Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698, especially Theorems 1.2 and 2.1. https://arxiv.org/abs/1507.00698

[3] Colin Christopher, *Polynomial vector fields with prescribed algebraic limit cycles*, Geometriae Dedicata 88 (2001), 255–258; DOI:10.1023/A:1013171019668. https://doi.org/10.1023/A:1013171019668
