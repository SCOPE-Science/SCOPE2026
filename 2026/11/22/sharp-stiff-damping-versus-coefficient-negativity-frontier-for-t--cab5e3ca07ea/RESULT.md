# Sharp stiff-damping versus coefficient-negativity frontier for two-stage algebraically stable third-order Runge–Kutta rules

## Finding
Let a real two-stage Runge–Kutta method have classical order at least three, positive weights, algebraic stability, and stage abscissas in \([0,1]\). Its scalar stability function is \(R(z)=1+zb^\mathsf T(I-zA)^{-1}\mathbf1\). Define its *stiff-decay residual* and *negative-entry size* by
\[
\sigma(A,b)=\lim_{x\to\infty}|R(-x)|,\qquad
\nu(A)=\max_{1\le i,j\le2}\max\{0,-a_{ij}\}.
\]
For each prescribed damping budget \(0\le\rho<1\), consider all such tableaux with \(\sigma(A,b)\le\rho\). The minimum \(\nu_\rho\) exists and its optimizer is unique up to simultaneous stage permutation.

Put \(t_\rho=(1-\rho)/(1+\rho)\). For \(0\le\rho\le1/2\), the unique minimizer has first weight \(3/4\), stage times \((1/3,1)\), and
\[
\boxed{\nu_\rho=\frac{1}{12(1+\rho)}.}
\]
For \(1/2<\rho<1\), let \(u_\rho\) be the **unique** solution in \((1/6,1/2)\) of
\[
(1+12u_\rho^2)^2=4(3-t_\rho)u_\rho.
\]
Then
\[
\boxed{\nu_\rho=u_\rho-\frac{2(3-t_\rho)u_\rho^2}{1+12u_\rho^2}.}
\]
In both regimes, the minimizer is the tableau specified in the proof below with \(u=u_\rho\) (or \(u=1/6\) for \(\rho\le1/2\)) and \(t=t_\rho\). Its actual stiff-decay residual equals \(\rho\). At \(\rho=0\), the unique minimizer is the L-stable two-stage Radau IIA tableau, with \(\nu_0=1/12\); at \(\rho=1/2\), the frontier changes from the boundary node to an interior pair of nodes. As \(\rho\uparrow1\), the frontier tends to the previously established unconstrained negative-entry minimum \(0.0356390699388833\ldots\); that unconstrained endpoint is **not** a new claim.

## Assumptions and scope
A real two-stage method consists of \(A=(a_{ij})\in\mathbb R^{2\times2}\) and \(b=(b_1,b_2)^\mathsf T\), where \(b_i>0\). Write \(\mathbf1=(1,1)^\mathsf T\), \(c=A\mathbf1\), and \(B=\operatorname{diag}(b)\). Classical order at least three means precisely
\[
b^\mathsf T\mathbf1=1,\quad b^\mathsf Tc=\tfrac12,\quad
b^\mathsf T(c\circ c)=\tfrac13,\quad b^\mathsf TAc=\tfrac16.
\]
Algebraic stability means \(M=BA+A^\mathsf TB-bb^\mathsf T\succeq0\). Require both entries of \(c\) to lie in \([0,1]\), with no assumption of collocation, symplecticity, diagonal implicitness, or stiff accuracy. The distinct abscissas can be sorted as \(c_1<c_2\), since their positive weighted variance is \(1/12\). Distinct tableaux differing only by a simultaneous stage permutation are identified. The theorem optimizes exactly \(\sigma\) and \(\nu\), not an SSP radius or a finite-stepsize error constant.

## Proof
**1. Exhaustive parametrization.** Sort the stages and write \(b=(p,q)^\mathsf T\) with \(q=1-p\). The first three order conditions give a two-point distribution with mean \(1/2\) and variance \(1/12\). Setting \(u=\sqrt{q/(12p)}\), their unique solution is
\[
p=\frac1{1+12u^2},\quad q=\frac{12u^2}{1+12u^2},\quad
c_1=\tfrac12-u,\quad c_2=\tfrac12+\frac1{12u}.
\]
The constraints \(c_1,c_2\in[0,1]\) are exactly \(1/6\le u\le1/2\).

Since \(\mathbf1^\mathsf TM\mathbf1=2b^\mathsf Tc-(b^\mathsf T\mathbf1)^2=0\), positive semidefiniteness forces \(M\mathbf1=0\). Thus \(M=m\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\) with \(m\ge0\). Set \(t=3m/(pq)\ge0\). The diagonal entries of \(M\) and the row sums \(c=A\mathbf1\) solve uniquely for
\[
A(u,t)=\begin{pmatrix}
\dfrac p2+\dfrac{tq}{6} & \dfrac{q(3-t)}6-u\\[4pt]
\dfrac{p(3-t)}6+\dfrac1{12u} & \dfrac q2+\dfrac{tp}{6}
\end{pmatrix},\qquad b(u)=\begin{pmatrix}p\\q\end{pmatrix}.
\]
Conversely, for every \(u\in[1/6,1/2]\) and \(t\ge0\), this tableau has the stated row sums and
\[
M=\frac{tpq}{3}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0.
\]
It also satisfies \(A^\mathsf Tb=b-Bc\), whence \(b^\mathsf TAc=b^\mathsf Tc-b^\mathsf T(c\circ c)=1/6\). Therefore this is an **exhaustive**, not merely a sufficient, parametrization of the permitted family.

**2. Stiff-decay parameter.** Direct expansion gives
\[
\operatorname{tr}A=\frac{3+t}{6},\qquad \det A=\frac{1+t}{12},
\]
and the scalar stability function depends only on \(t\):
\[
R_t(z)=\frac{1+(3-t)z/6+(1-t)z^2/12}
{1-(3+t)z/6+(1+t)z^2/12}.
\]
Its denominator has no roots in the closed left half-plane since both \((3+t)/6\) and \((1+t)/12\) are positive. Moreover the difference between squared numerator and denominator moduli on the imaginary axis, in the correct order, is \(|Q_t(iy)|^2-|P_t(iy)|^2=t y^4/36\ge0\). Combined with \(|R_t(-\infty)|\le1\), this also establishes scalar A-stability. In particular,
\[
\sigma(A,b)=\frac{|1-t|}{1+t}.
\]
For any \(0\le\rho<1\), the constraint \(\sigma\le\rho\) is equivalent to
\[
\frac{1-\rho}{1+\rho}\le t\le\frac{1+\rho}{1-\rho}.
\]

**3. Necessary negative coefficient and strict selection of damping.** The upper-right entry is
\[
a_{12}=\frac{q(3-t)}6-u=-d(u,t),\qquad
 d(u,t)=u-\frac{2(3-t)u^2}{1+12u^2}.
\]
For every permitted \(u\), \(d(u,0)>0\): indeed \(1+12u^2-6u=12(u-1/4)^2+1/4>0\). Also \(\partial d/\partial t=2u^2/(1+12u^2)>0\). Therefore every allowed tableau satisfies
\[
\nu(A)\ge d(u,t)\ge d(u,t_\rho).
\]
Equality at the minimizing \(t=t_\rho\in(0,1]\) is possible: the other three entries of \(A(u,t_\rho)\) are positive, so \(\nu(A(u,t_\rho))=d(u,t_\rho)\). Strict increase in \(t\) forces \(t=t_\rho\) at every optimizer.

**4. Sharp scalar minimization and transition.** For fixed \(t\in(0,1]\), write \(d_t(u)=d(u,t)\). Differentiation yields
\[
d_t'(u)=1-\frac{4(3-t)u}{(1+12u^2)^2}.
\]
The function \(u/(1+12u^2)^2\) is strictly decreasing for \(u>1/6\), since its derivative is \((1-36u^2)/(1+12u^2)^3\). Thus \(d_t'\) is strictly increasing on \((1/6,1/2)\), and
\[
d_t'(1/6)=\frac{3t-1}{8},\qquad d_t'(1/2)=\frac{5+t}{8}>0.
\]
If \(t\ge1/3\), the unique minimum lies at \(u=1/6\) and equals \((1+t)/24\). If \(0<t<1/3\), there is a unique interior stationary point, it is the strict global minimum, and it solves \((1+12u^2)^2=4(3-t)u\). Since \(t_\rho\ge1/3\) exactly when \(\rho\le1/2\), substitution produces both branches and the sharp phase transition. Exhaustiveness of the parametrization, strictness of the \(t\) selection, and uniqueness of the one-dimensional minimizer yield uniqueness up to relabeling.

**5. Boundary interpretation.** At \(\rho=0\), \(t=1\), \(u=1/6\), \(b=(3/4,1/4)^\mathsf T\) and
\[
A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},
\]
the two-stage third-order Radau IIA tableau. For \(\rho\uparrow1\), \(t_\rho\downarrow0\) and the minimizing equation recovers the published symplectic negative-entry optimization, furnishing a boundary consistency check without reclaiming its existing result.

## Verification
The attached standalone \(\texttt{verify.py}\), using only the Python standard library, reconstructs the tableaux for a range of rational \(u,t\), checks all four order-three conditions and the algebraic-stability matrix with exact fractions, and verifies the rational stability function by direct two-by-two inversion. It also checks rational samples of both damping regimes, the boundary formula, and the Radau IIA corner; a floating-point bisection is used only for supplementary interior samples. Run \(\texttt{python verify.py}\) from the extracted package directory. The exact proof above, not the finite tests, establishes the continuum of parameters and uniqueness.

Numerical boundary checks give \(\nu_0=1/12\), \(\nu_{1/2}=1/18\), \(\nu_{3/4}\approx0.0450346771246\), and \(\lim_{\rho\uparrow1}\nu_\rho\approx0.0356390699389\).

## Relationship to prior work
Gottlieb, Grant, Horesh, Lóczi, Shinnar and Trager (arXiv:2611.07981v1) establish a qualitative incompatibility between nonnegative Butcher entries and algebraic stability at order three; their third theorem does not quantify the damping-versus-negativity compromise here. Weng, Yu and Zhu (arXiv:2610.37425v1) optimize SSP radii through positive-coefficient phase-type representations, a different feasible class and objective. The published result *Sharp unavoidable negative Butcher coefficient for two-stage algebraically stable third-order Runge–Kutta rules* (2026-11-08) already determines the unrestricted minimum \(0.035639\ldots\), its optimizer, and uniqueness. That result is a **strong nearby predecessor**: its moment and positivity arguments overlap our unconstrained boundary, which is not claimed as new. The present conclusion instead treats every **strict stiff-decay budget** \(\rho<1\), obtains its uniquely optimal tableau, and identifies the exact \(\rho=1/2\) transition. Neither the unconstrained minimum nor the qualitative obstruction by themselves imply the complete damping-constrained profile.

## Limitations
This is a two-stage, order-at-least-three, positive-weight, algebraically stable result with both stage times in \([0,1]\). It does not establish analogous optima for more stages, nonpositive weights, or other stiffness/positivity measures. The damping budget is the limit along the negative real axis; transient stages or nonlinear strong-stability preservation are not quantified. Because the optimum always contains a negative coefficient, it has no positive classical SSP radius through the usual nonnegative-tableau criterion. Although a direct equivalent frontier was not found in inspected records, an earlier implicit RK parameter study may encode the same minimization. Independent external mathematical validation has not been performed.

## References
1. S. Gottlieb, Z. Grant, L. Horesh, L. Lóczi, A. Shinnar, B. Trager, *A stability order barrier and SSP bound for Runge–Kutta methods with non-negative coefficients*, arXiv:2611.07981v1, first public 2026-11-05, https://arxiv.org/abs/2611.07981 .
2. H. Yu, Q. Zhu, Z. Weng, *Phase-type representations for Strong Stability Preserving Runge–Kutta methods*, arXiv:2610.37425v1, first public 2026-10-27, https://arxiv.org/abs/2610.37425 .
3. *Sharp unavoidable negative Butcher coefficient for two-stage algebraically stable third-order Runge–Kutta rules*, public mathematical record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-unavoidable-negative-butcher-coefficient-for-two-stage-alg--f7feb4142d7a .
4. E. Hairer, G. Wanner, *Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems*, second edition, Springer, 1996; classical Runge–Kutta stability definitions and Radau IIA methods.
