# Unconditional stability and a period-four spectral bottleneck in a delayed rational map

## Finding
Let \(u,v,a,b,r\) be arbitrary strictly positive real numbers. On the positive octant, define the smooth map
\[
T_r(x,y,z)=\left(\frac{u+a(x+z)}{v+b(x+z)+ry},\ x,\ y\right).
\]
It has exactly one positive fixed point \((t_r,t_r,t_r)\), and that point is a **hyperbolic sink for every finite** \(r>0\). Moreover \(T_r\) has no strictly positive primitive period-two orbit for any choice of the five positive parameters.

Fix \(u,v,a,b>0\) and increase the delayed-feedback coefficient \(r\) without bound. If \(\rho(r)\) denotes the spectral radius of \(DT_r(t_r,t_r,t_r)\), then
\[
\boxed{\lim_{r\to\infty}\sqrt r\,[1-\rho(r)]=\frac{v}{2\sqrt u}.}
\]
For sufficiently large \(r\), the spectral-radius modes form a complex-conjugate pair with arguments tending to \(\pm\pi/2\). The leading linear relaxation time \(1/[-\log\rho(r)]\) is asymptotic to \(2\sqrt{ur}/v\). The leading constant is independent of both same-parity feedback coefficients \(a,b\), although they influence finite-parameter behavior. The period-four feature is a **linear oscillatory bottleneck**, not an assertion that a genuine period-four orbit exists.

## Assumptions and scope
The phase space is \((0,\infty)^3\), and \(u,v,a,b,r>0\) with no other inequalities or monotonicity restrictions. All time indices are discrete. The fixed-point and period-two statements are global algebraic assertions about strictly positive points; the sink and relaxation statements are local assertions about the derivative at the unique positive fixed point. The limit holds with \(u,v,a,b\) fixed while \(r\to\infty\).

This smooth three-dimensional system is the equal-outer-lag positive rational recurrence
\[
x_{n+1}=\frac{u+a(x_n+x_{n-2})}{v+b(x_n+x_{n-2})+r x_{n-1}}.
\]
The normalized source example \(u=v=1\), \(a=3\), \(b=2\), \(r=4\) belongs to this family.

## Proof
**1. Unique positive fixed point.** A fixed coordinate \(t>0\) must satisfy
\[
(r+2b)t^2+(v-2a)t-u=0.
\]
The left-hand side is negative at zero, strictly convex, and tends to positive infinity; its two roots have negative product. Consequently it has exactly one positive root, explicitly
\[
t_r=\frac{2a-v+\sqrt{(v-2a)^2+4u(r+2b)}}{2(r+2b)}.
\]
Define \(D=v+(2b+r)t_r=u/t_r+2a>0\).

**2. Exact derivative and Schur stability.** Differentiating the first component at the fixed point yields equal outer derivatives \(\alpha=(a-bt_r)/D\) and a negative middle derivative \(-\omega=-rt_r/D\). Thus
\[
DT_r(t_r,t_r,t_r)=
\begin{pmatrix}\alpha&-\omega&\alpha\\1&0&0\\0&1&0\end{pmatrix},
\qquad P(\lambda)=\lambda^3-\alpha\lambda^2+\omega\lambda-\alpha.
\]
Positivity of \(u,v,a,b,r,t_r\) supplies the strict, parameter-uniform structural inequalities
\[
-\tfrac12<\alpha<\tfrac12,\qquad 0<\omega<1.
\]
Indeed \(D=u/t_r+2a>2a\) implies \(\alpha<a/D<1/2\), whereas \(D>2bt_r\) implies \(\alpha>-bt_r/D>-1/2\); also \(D>rt_r\). For a real monic cubic \(\lambda^3+c_1\lambda^2+c_2\lambda+c_3\), the strict Jury–Schur conditions are \(|c_3|<1\), \(1+c_1+c_2+c_3>0\), \(1-c_1+c_2-c_3>0\), and \(1-c_2+c_1c_3-c_3^2>0\). Here these become
\[
|\alpha|<1,\quad 1-2\alpha+\omega>0,\quad
1+2\alpha+\omega>0,\quad 1-\omega>0.
\]
All hold strictly. Every derivative eigenvalue therefore has modulus less than one and the fixed point is a hyperbolic attracting point. This does not invoke the global monotonicity assumptions of the source's embedding theorem.

**3. Two-cycle rigidity.** Suppose positive \(A,B\) alternate. The period-two equations are
\[
A(v+2bB+rA)=u+2aB,\qquad
B(v+2bA+rB)=u+2aA.
\]
Subtracting gives
\[
(A-B)[v+2a+r(A+B)]=0.
\]
The bracket is strictly positive, hence \(A=B\). Thus no positive primitive period-two orbit exists, even far from the local basin of the equilibrium.

**4. Singular, nearly period-four spectrum.** Put \(\varepsilon=r^{-1/2}\). The positive quadratic root satisfies the asymptotic expansion
\[
t_r=\sqrt u\,\varepsilon+(a-v/2)\varepsilon^2+O(\varepsilon^3).
\]
Therefore
\[
D=\frac{\sqrt u}{\varepsilon}+a+v/2+O(\varepsilon),\quad
\alpha=\frac a{\sqrt u}\varepsilon+O(\varepsilon^2),\quad
\omega=1-\frac v{\sqrt u}\varepsilon+O(\varepsilon^2).
\]
At \(\varepsilon=0\) the limiting characteristic polynomial is \(P_0(\lambda)=\lambda(\lambda^2+1)\), whose three roots \(0,i,-i\) are simple. The analytic implicit-function theorem gives analytic root branches. Substitution into \(P\), or differentiation at the limiting roots, gives
\[
\lambda_0=\frac a{\sqrt u}\varepsilon+O(\varepsilon^2),\qquad
\lambda_\pm=\pm i\left(1-\frac v{2\sqrt u}\varepsilon\right)+O(\varepsilon^2).
\]
The \(\alpha\)-dependent first-order perturbation vanishes at \(\pm i\), because it is proportional to \(\lambda^2+1\). The conjugate pair dominates the third root in modulus for small positive \(\varepsilon\), hence
\[
\rho(r)=1-\frac v{2\sqrt{ur}}+O(r^{-1}).
\]
This proves the spectral-gap limit and the relaxation-time asymptotic. Finally the arguments of \(\lambda_\pm\) approach \(\pm\pi/2\), explaining the four-step phase of the slow linearized oscillations.

## Verification
The accompanying `check.py` evaluates the fixed-point and Jacobian identities symbolically, verifies the strict Jury factors on exact-rational parameter samples, evaluates the cubic characteristic roots numerically, and checks the predicted scaled spectral gap for increasing \(r\). Numerical checks are diagnostic; the assertions for all positive parameters and the infinite \(r\)-limit follow from the algebraic proof above. Execute with `python check.py`; dependencies are Python 3, SymPy and NumPy. A reproducible package-level checker run is documented in `VERIFICATION.md`.

## Relationship to prior work
AlSharawi, Cánovas and Kallel, *Attractors in \(k\)-dimensional discrete systems of mixed monotonicity* (arXiv:2402.14127, first publicly posted February 21, 2024), introduce an extended-state order method and present the normalized equal-outer-lag rational recurrence as Example 4.3(v). Their Theorem 4.7 gives sufficient conditions for **global** attractivity in a broad rational family and covers some finite-parameter portions of the present family. Global attractivity necessarily implies local attractivity where its hypotheses apply, so **local stability in those covered portions is not claimed new**. The result here addresses every positive coefficient choice, including nonmonotone members and the strong delayed-feedback regime not covered by that sufficient condition, and derives a sharp spectral-gap law and a universal absence of primitive two-cycles.

Standard cubic Jury–Schur criteria and simple-root perturbation theory are used as established lemmas, not claimed as new methods. Earlier literature on third-order rational difference equations investigates positive fixed points, boundedness, and recurrence, but the inspected material did not provide this precise singular period-four spectral bottleneck with its coefficient independence.

## Limitations
No global convergence theorem is asserted for parameter ranges not covered by existing global-stability results. Higher-period orbits, coexisting attractors, or nonlinear dynamics far from the sink are not excluded. The \(\sqrt r\) scaling concerns the **local linearized** relaxation, not a uniform transient bound for all positive initial states. The complex pair is guaranteed in the large-\(r\) regime, not necessarily at every finite parameter. Prior-work checks do not guarantee publication priority; equivalent results may exist outside accessible/indexed sources. Independent validation has not been performed.

## References
1. Z. AlSharawi, J. S. Cánovas, S. Kallel, *Attractors in \(k\)-dimensional discrete systems of mixed monotonicity*, arXiv:2402.14127v1, February 21, 2024. https://arxiv.org/abs/2402.14127
2. H. L. Smith, *Global stability for mixed monotone systems*, Journal of Difference Equations and Applications 14 (2008), 1159–1164.
3. E. Camouzis and G. Ladas, *Dynamics of Third-Order Rational Difference Equations with Open Problems and Conjectures*, Chapman & Hall/CRC, 2008.
4. Classical Jury–Schur root-location criterion for real monic cubic polynomials (standard stability test).
