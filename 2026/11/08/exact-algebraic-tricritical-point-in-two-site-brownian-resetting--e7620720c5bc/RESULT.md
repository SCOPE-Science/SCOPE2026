# Exact algebraic tricritical point in two-site Brownian resetting on a circle

## Finding

Consider Brownian motion on a circle of radius \(R>0\), diffusivity \(D>0\), and a point absorber at angle \(\pi/2\). At each event of a Poisson clock of rate \(r\geq0\), restart at the antipode \(3\pi/2\) with probability \(1-p\), or at an angle \(\varphi\in(0,\pi/2)\) with probability \(p\in(0,1)\). The initial angle is sampled from the same distribution. Call a *zero-rate tricritical coordinate* a pair \((p,\varphi)\) where the first and second derivatives at \(r=0\) of the averaged mean first-passage time both vanish.

**Theorem.** There is exactly one such coordinate in the specified physical rectangle. Put \(b=(1/2+\varphi/\pi)^2\). Then \(b=b_*\) is the unique root in \((2/5,9/20)\) of

\[
Q(b)=b^3+15b^2-16b+4=0,
\]

and

\[
p_*=\frac{5b_*-2}{3b_*^3},\qquad m_*:=\frac{p_*}{1-p_*}.
\]

Numerically, \(b_*=0.4200306588002687368\ldots\), \(p_*=0.4505064449928159102\ldots\), \(m_*=0.8198575595430340942\ldots\), and \(\varphi_*/\pi=0.1480977231870737\ldots\). Reflection about the target produces the companion angle \(\pi-\varphi_*\), not an additional parameter value.

At this point the dimensionless first-passage objective is flat through quadratic order in the dimensionless resetting rate \(y=\pi^2R^2r/D\) but has a **strictly positive cubic coefficient** \(C_*=0.0000056571326959670658\ldots\). The two local control coefficients provide smooth coordinates near this point. Along their physically realizable curve \(A_2=0\), \(A_1=-\varepsilon<0\), a positive local minimizer emerges with

\[
y_{\rm loc}(\varepsilon)=\sqrt{\frac{\varepsilon}{3C_*}}+O(\varepsilon)
\quad (\varepsilon\downarrow0).
\]

This last statement is about a **local** small-rate minimum; no global uniqueness of the optimal rate near the tricritical point is asserted.

## Assumptions and scope

The Brownian generator along arclength is \(D\partial_{ss}\); the target absorbs immediately, reset times are independent exponential waiting times, resets are instantaneous, and the initial/reset angle law coincides. The strictly physical parameter domain is \(0<p<1\) and \(0<\varphi<\pi/2\), with \(D,R>0\). Angles are in radians. The first reset location is fixed diametrically opposite the target; this is not a classification of all two-site configurations. MSC2020: 82C31.

Set

\[
b=(1/2+\varphi/\pi)^2,\qquad y=\pi^2R^2r/D,
\qquad \mathcal F(y;p,b)=\frac{\cosh\sqrt y/(1-p+p\cosh\sqrt{by})-1}{y}.
\]

The physical averaged mean first-passage time is \((\pi^2R^2/D)\mathcal F(y;p,b)\). The removable value at \(y=0\) is defined by continuity. In the parameter domain here, \(1/4<b<1\).

## Proof

**1. Renewal objective and Taylor coefficients.** For free Brownian motion on the circle, the Laplace transform of the hitting time from an angle at shortest angular separation \(d\) from the absorber is \(\cosh((\pi-d)\sqrt{rR^2/D})/\cosh(\pi\sqrt{rR^2/D})\). Averaging this transform over the two reset/initial sites and applying the standard restart renewal equation gives the stated \(\mathcal F\). The antipodal site has \(d=\pi\), whereas the second site has \(d=\pi/2-\varphi\). Thus its hyperbolic-cosine numerator is \(\cosh(\sqrt{by})\).

The function extends analytically through \(y=0\):

\[
\mathcal F(y;p,b)=A_0+A_1y+A_2y^2+A_3y^3+O(y^4),
\]

where, writing \(P_1,P_2\) for the displayed integer polynomials,

\[
A_0=\frac{1-bp}{2},\qquad A_1=\frac{P_1}{24},\qquad
A_2=-\frac{P_2}{720},
\]

\[
P_1=6b^2p^2-(b^2+6b)p+1,
\]

\[
P_2=90b^3p^3-30b^3p^2+b^3p-90b^2p^2+15b^2p+15bp-1.
\]

These identities follow by formal division of the two hyperbolic-cosine series; an explicit exact-arithmetic recurrence is in `verify.py`. Since \(r\) and \(y\) are positive multiples, the zero-rate tricritical equations are exactly \(P_1=P_2=0\).

**2. Elimination and uniqueness.** The following polynomial identity is exact:

\[
P_2=\frac{5b(6p-1)}2P_1-\frac{3b^3p-5b+2}{2}.
\]

For any solution with \(b>0\), therefore \(p=(5b-2)/(3b^3)\). Substitution yields

\[
P_1\left(b,\frac{5b-2}{3b^3}\right)
=-\frac{2(b-1)}{3b^4}Q(b).
\]

In the open physical range \(0<b<1\), one must have \(Q(b)=0\). The cubic decreases then increases for \(b>0\), because its derivative \(3b^2+30b-16\) has only one positive zero. Since \(Q(0)>0\), \(Q(1/2)<0\), and \(Q(1)>0\), it has exactly two zeros in \((0,1)\). The smaller lies in \((2/5,9/20)\), and gives \(0<p<1\). The larger is in \((1/2,3/5)\), where \(p>1\), because \(3b^3-5b+2=(b-1)(3b^2+3b-2)<0\). Hence exactly one physical solution exists. The same computation verifies \(P_2=0\) at the smaller root.

**3. Certified strict cubic sign.** At the simultaneous root, the exact cubic coefficient satisfies

\[
C_*=A_3(p_*,b_*)=
\frac{915202561b_*^2-928637484b_*+228590912}{5670b_*^8}.
\]

The identity follows by substituting \(p=(5b-2)/(3b^3)\) into the fourth coefficient of the quotient series and reducing modulo \(Q(b)\). Let

\[
\ell=420030658800268/10^{15},\qquad
u=420030658800270/10^{15}.
\]

Exact rational evaluation gives \(Q(\ell)>0>Q(u)\); the unique smaller zero satisfies \(\ell<b_*<u\). The quadratic numerator \(H(b)=915202561b^2-928637484b+228590912\) has \(H(u)>0\) and \(H'(b)<0\) throughout \([\ell,u]\), so \(H(b_*)>0\), proving \(C_*>0\). The exact sign checks and the coefficient reduction are reproduced by `verify.py`.

**4. Nondegenerate local onset.** The Jacobian determinant for the control map \((b,p)\mapsto(A_1,A_2)\) is

\[
\frac{\partial(A_1,A_2)}{\partial(b,p)}
=-\frac{b^2p}{17280}
\left(90b^2p^2+6b^2p+b^2-180bp+12b+75\right).
\]

At the tricritical coordinate \(2/5<b_*<9/20\) and \(0<p_*<1/2\), the bracket is greater than \(75-180(9/20)(1/2)>0\). Therefore the Jacobian is nonzero, and the implicit-function theorem provides a unique local physical path with \(A_2=0\), \(A_1=-\varepsilon\). Uniform analyticity on a neighborhood gives, on this path,

\[
\partial_y\mathcal F=-\varepsilon+3C_*y^2+O(\varepsilon y^2+y^3).
\]

Putting \(y=\sqrt\varepsilon\,v\), the implicit-function theorem at \(v=(3C_*)^{-1/2}\) gives a unique small positive stationary point and the asserted asymptotic. Its second derivative is \(6C_*y+o(y)>0\), so it is a strict local minimum. This proves the claimed local square-root onset without assuming anything about other, distant extrema.

## Verification

Run `python verify.py` with Python 3 and SymPy 1.11 or later. The checker reconstructs all four Taylor coefficients, verifies the elimination and algebraic reduction identities, isolates the physical root with exact rational endpoints, proves the sign of the cubic coefficient, checks the nonzero control Jacobian, and reports illustrative high-precision evaluations. All symbolic identities and rational sign tests passed in SymPy 1.14.0. Numerical tests are supplemental and are not used as an infinite-domain proof.

## Relationship to prior work

Julián-Salgado, Castro-Villarreal, Dagdug and Boyer (arXiv:2605.08414, first public May 8, 2026) derived the Brownian-ring two-site reset formula and identified its tricritical points by numerically solving the first-two-derivative equations, reporting \(m_{tc}\simeq0.81985\), \(\varphi_{tc}\simeq0.1481\pi\). That existence and approximate location are prior work. The present claim replaces the numerical coordinate with a unique algebraically specified physical solution, proves the positive third-order nondegeneracy, and gives a rigorously parametrized local square-root onset. Their related accepted article (DOI:10.1103/2fsc-jkq8) is the same scientific work, not independent evidence. Their earlier arXiv:2311.11897 analyzes two-point resetting on a half-line and its discontinuous optimum; its geometry and equations do not imply this specific circle's algebraic tricritical coordinate. Standard Landau expansions motivate, but do not supply, the polynomial elimination or exact physical-root isolation.

## Limitations

The proof classifies only zero-rate simultaneous derivative zeros for the stated diametric first reset site and a second site between angle zero and the target, plus the direct mirror image. It does not classify additional extrema away from zero, assert global optimizer uniqueness, or derive universal behavior for arbitrary reset distributions. Numerical root values are given for orientation, with the defining polynomials and exact rational brackets providing the proof. A revised or unindexed prior treatment could preempt publication priority; no independent audit has yet been performed.

## References

1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1 (first submitted 2026-05-08), https://arxiv.org/abs/2605.08414, especially equations (28)–(31), (38), and Table 1.
2. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer, *Critical and tricritical transitions in diffusion with stochastic resetting on a ring*, accepted 2026-09-29, https://doi.org/10.1103/2fsc-jkq8. Same work as reference 1.
3. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (first submitted 2023-11-20), https://arxiv.org/abs/2311.11897.
