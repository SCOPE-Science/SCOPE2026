# Two transverse stability reversals under a common predator-conversion sweep in a three-species Lotka–Volterra flow

## Finding

For the positive-parameter, two-prey–one-predator Lotka–Volterra equations
\[
\begin{aligned}
\dot x&=x\left(1-x-\frac32y-\frac32z\right),\\
\dot y&=y\left(1-\frac{99}{100}x-y-5z\right),\\
\dot z&=z\left(t\left(\frac14x+4y\right)-1\right),\qquad t>0,
\end{aligned}
\]
the unique coexistence equilibrium is strictly positive exactly for \(3/7<t<703/175\). Within that entire interval, there are precisely two spectral stability transitions \(t_1\in(6/5,5/4)\) and \(t_2\in(3,13/4)\), determined by distinct roots of the exact quartic
\[
Q(t)=2353225t^4+217031234t^3-1013526060t^2+985375470t-101672781.
\]
The coexistence equilibrium is locally exponentially asymptotically stable for \(3/7<t<t_1\) and \(t_2<t<703/175\), and linearly unstable for \(t_1<t<t_2\). At each transition it has one strictly negative eigenvalue and a simple conjugate imaginary pair that crosses the imaginary axis transversely, first to instability and then back to stability. Numerically, \(t_1=1.20245031065833\ldots\) and \(t_2=3.17827981795257\ldots\). The two transitions and both stability windows persist under sufficiently small perturbations of the fixed positive coefficients.

## Assumptions and scope

All rates are positive. Two self-limited prey species compete directly and are consumed by a shared predator. The scalar \(t\) multiplies both predator conversion efficiencies in the fixed ratio \(1:16\), with all prey growth, crowding, direct-competition, consumption and predator-mortality coefficients frozen. All stability claims concern the unique equilibrium with \(x,y,z>0\); they are local linear or local exponential conclusions for the autonomous ordinary differential equation, not global basin claims. At a transition, *spectral crossing* is proved; nonlinear Hopf nondegeneracy and a branch of periodic orbits are not asserted.

## Proof

**1. Unique feasible coexistence state.** Dividing the three stationary equations by their positive populations gives the nonsingular linear system
\[
\begin{pmatrix}1&3/2&3/2\\99/100&1&5\\1/4&4&0\end{pmatrix}
\begin{pmatrix}x\\y\\z\end{pmatrix}=
\begin{pmatrix}1\\1\\1/t\end{pmatrix}.
\]
Its determinant is \(-314/25\), and its unique solution is
\[
(x_*,y_*,z_*)=\left(\frac{25(7t-3)}{157t},\frac{703-175t}{2512t},\frac{97-17t}{2512t}\right).
\]
All coordinates are positive if and only if \(3/7<t<703/175\); the third upper bound \(97/17\) is larger than \(703/175\).

**2. Exact characteristic coefficients.** The Jacobian at that state is
\[
J=\begin{pmatrix}-x_*&-3x_*/2&-3x_*/2\\ -99y_*/100&-y_*&-5y_*\\ tz_*/4&4tz_*&0\end{pmatrix}.
\]
Direct expansion gives \(\det(\lambda I-J)=\lambda^3+A(t)\lambda^2+B(t)\lambda+C(t)\), where
\[
\begin{aligned}
A(t)&=\frac{7(375t-71)}{2512t},\\
B(t)&=\frac{20825t^3-115685t^2+131823t+204573}{3155072t^2},\\
C(t)&=\frac{(7t-3)(17t-97)(175t-703)}{3155072t^2}.
\end{aligned}
\]
Throughout the feasible interval \(A,C>0\). The cubic numerator of \(B\) has discriminant \(-350833582372132531200<0\); hence exactly one real root, and since its leading coefficient and value at zero are positive, that root is negative. Therefore \(B>0\) for all positive \(t\).

**3. Exactly two feasible stability boundaries.** Routh–Hurwitz for a monic real cubic with positive \(A,B,C\) gives local asymptotic stability if and only if \(H=AB-C>0\). Here
\[
H(t)=\frac{Q(t)}{7925540864t^3}.
\]
Descartes' rule gives at most three positive real roots of \(Q\) (three sign changes) and at most one negative real root (one sign change in \(Q(-t)\)). Exact rational evaluations give \(Q(0)<0<Q(1/5)\), \(Q(6/5)>0>Q(5/4)\), and \(Q(3)<0<Q(13/4)\). Thus these three disjoint positive intervals contain distinct positive roots; there is exactly one in each and exactly one negative root. The first positive root lies below \(1/5<3/7\), leaving precisely \(t_1,t_2\) in the feasible interval. Their signs alternate, and \(H>0\) just after \(3/7\), proving the stated stable–unstable–stable partition.

**4. Oscillatory and transverse crossings.** At either simple zero \(t_i\), \(C=AB\), so the characteristic polynomial factors exactly as \((\lambda+A)(\lambda^2+B)\); its eigenvalues are \(-A,\pm i\sqrt B\) with \(A,B>0\). Along the eigenvalue branch with positive imaginary part, implicit differentiation gives
\[
\left.\frac{d}{dt}\operatorname{Re}\lambda(t)\right|_{t=t_i}
=-\frac{H'(t_i)}{2\bigl(A(t_i)^2+B(t_i)\bigr)}\ne0.
\]
The three positive roots of \(Q\) are distinct and separated by disjoint sign-changing intervals, hence simple (quartic with another distinct negative root). At \(t_1\), \(H'<0\); at \(t_2\), \(H'>0\). Therefore the first pair crosses from the left to the right half-plane and the second from right to left. Since \(A,B,C>0\), the polynomial has no nonnegative real root; in the intermediate unstable interval the unstable eigenvalues must be a nonreal conjugate pair. At all strict stability points, Hurwitz linearization yields local exponential attraction. At any compact choice of parameters inside the two stable windows and the unstable window, strict inequalities persist under small changes of fixed coefficients; the two simple spectral roots persist by the implicit-function theorem, proving robustness.

## Verification

The companion Python/SymPy script `check.py` recomputes the rational coexistence equilibrium, Jacobian characteristic polynomial, the quartic Routh–Hurwitz numerator, the cubic discriminant, exact rational root brackets, Descartes sign patterns and representative stability signs. It terminates with `PASS` on all assertions and prints approximate crossing locations. The exact algebra and sign-change/degree proof, rather than floating-point root searches, establish the universal parameter interval conclusions.

## Relationship to prior work

Huang and Yang (2026), equations (1.2) and (4.2)–(4.5), establish the underlying ecological model and general Routh–Hurwitz local-stability inequalities, and analyze large parameter classes. Those general inequalities are used and credited; the contribution here is the explicit **one-parameter moving-coexistence branch**, a quartic whose complete feasible root count is proved, **two opposite transverse oscillatory crossings**, and an open robust example under a common predator-conversion sweep. Prior examples of two Hopf points in Holling–Tanner (Braza, 2003) concern a different nonlinear functional-response ecology; published three-species antagonistic-link reentrance and delayed/spatial predator–prey reentrance involve different mechanisms, not a fixed immediate-response two-prey–one-predator Lotka–Volterra conversion sweep. This does not establish comprehensive historical priority for every closely related Lotka–Volterra family.

## Limitations

The fixed numerical rates are an exact rational witness and not an optimal/minimal parameter characterization. No nonlinear first Lyapunov coefficient, Hopf bifurcating periodic-orbit branch, global attractor classification, or ecological invariance beyond the standard positive orthant is claimed. Historical priority is subject to specialized older literature not fully accessible in this study. Stability at the two neutral thresholds is not classified nonlinearly.

## References

1. Mingchieh Huang and Tinghui Yang (2026), *Direct and Indirect Competition in a Two-Prey-One-Predator System: Global Dynamics, Chaos, and the Paine Conjecture*, arXiv:2611.02246v1, first posted 2026-11-01, https://arxiv.org/html/2611.02246v1 .
2. P. A. Braza (2003), *The Bifurcation Structure of the Holling–Tanner Model for Predator–Prey Interactions Using Two-Timing*, SIAM J. Applied Mathematics 63, 889–904, https://doi.org/10.1137/S0036139901393494 .
3. H. L. Smith (1982), *The Interaction of Steady State and Hopf Bifurcations in a Two-Predator–One-Prey Competition Model*, SIAM J. Applied Mathematics 42, 27–43, https://doi.org/10.1137/0142003 .
