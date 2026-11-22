# Transverse extinction threshold and algebraic critical decay along an escaping quadratic-flow axis

## Finding
For the quadratic flow of Dong (2022),
\[
\dot x=a(y-x)+kxz,\qquad \dot y=-cy-xz,\qquad \dot z=-b+xy,
\]
fix arbitrary \(a,b,c,k>0\) and \(z_0\in\mathbb R\). The orbit \((0,0,z_0-bt)\) exists for every real time. Its transverse variational equation has a one-dimensional rapidly contracting subspace and one complementary slow mode. Put
\[
s(t)=bt-z_0,\quad \lambda=\frac ak-c,\quad
p=\frac1b\left(\frac{a(c-a)}{k^2}-\frac{a^2}{k^3}\right).
\]
For some nonzero solution \((u_s,v_s)\), as \(t\to\infty\),
\[
v_s(t)=C e^{\lambda t}s(t)^p(1+O(s(t)^{-1})),\qquad
u_s(t)=\left(\frac{a}{ks(t)}+O(s(t)^{-2})\right)v_s(t),
\]
where \(C\ne0\). There exists an independent solution \((u_f,v_f)\) with
\[
\lim_{t\to\infty}\frac{\log\|(u_f(t),v_f(t))\|}{t^2}=-\frac{kb}{2}.
\]
Every transverse solution outside the fast subspace has the slow asymptotics up to a nonzero scalar factor. Consequently generic transverse linear perturbations grow exponentially for \(0<k<a/c\), while every nonzero solution in the exceptional fast subspace decays; all transverse perturbations decay exponentially for \(k>a/c\), and at the exact boundary \(k=a/c\) all transverse perturbations decay; those outside the fast subspace obey
\[
v(t)=C\,(bt-z_0)^{-c^2/b}(1+O(t^{-1})),\qquad
u(t)=\frac{c}{bt-z_0}v(t)(1+O(t^{-1})).
\]
The same threshold is the precise loss-of-finite-equilibria boundary: the flow has exactly two equilibria for \(0<k<a/c\) and none for \(k\ge a/c\). This equilibrium fact is already algebraically available from Dong's equilibrium formulas; the transverse asymptotic splitting and critical power are the findings here.

## Assumptions and scope
All parameters \(a,b,c,k\) are strictly positive. The time variable is the original time in the printed polynomial system. The transverse perturbations are solutions of the linearization in \((x,y)\) along the exact escaping orbit, not nonlinear perturbations of finite amplitude; perturbation of \(z\) is a decoupled constant at linear order. The displayed \(O\)-terms hold at fixed parameters, fixed \(z_0\), and for each nonzero slow-mode normalization. The exceptional fast subspace is one-dimensional. For critical \(k=a/c\), the coefficient of the generic algebraic term is nonzero exactly when the initial transverse vector lies outside that fast subspace. All convergence assertions refer to \(t\to+\infty\).

## Proof
**1. Axis and transverse system.** Setting \(x=y=0\) leaves \(\dot z=-b\), producing the stated exact global trajectory. Along this orbit put \(s=bt-z_0\); then for sufficiently large time \(s>0\), and the transverse variational system is
\[
\dot u=-(a+ks)u+av,\qquad \dot v=su-cv.
\tag{1}
\]
The original polynomial coefficients are smooth for all finite time, so any solutions constructed for sufficiently large positive \(s\) extend uniquely backwards to the original initial time.

**2. Construct the slow fundamental solution.** Seek \(v>0\) and write \(r=u/v\). Equation (1) gives
\[
\dot r=a+(c-a-ks)r-sr^2,\qquad \dot v/v=sr-c.
\tag{2}
\]
Let \(A=a/k\) and \(B=a(c-a)/k^2-a^2/k^3\). Define \(R(s)=A/s+B/s^2\). Direct substitution into (2) gives
\[
\left[a+(c-a-ks)R-sR^2\right]-bR'(s)
=\frac{(c-a)B-2AB+bA}{s^2}-\frac{B^2}{s^3}.
\tag{3}
\]
For sufficiently large \(S>0\), choose \(L>0\) so large that \(R_-(s)=R(s)-L/s^3\) and \(R_+(s)=R(s)+L/s^3\) are positive and respectively a strict subsolution and supersolution of (2) on \([S,\infty)\). Indeed, their residuals \(a+(c-a-ks)R_\pm-sR_\pm^2-bR_\pm'\) have leading terms \(((c-a)B-2AB+bA\mp kL)s^{-2}\); their signs can be arranged opposite by increasing \(L\). Scalar comparison gives an actual global Riccati solution \(r\) trapped between \(R_-\) and \(R_+\). Hence
\[
r(s)=\frac{A}{s}+\frac{B}{s^2}+O(s^{-3}).
\tag{4}
\]
Solve \(\dot v=(sr-c)v\) from an initial positive value. Because \(\dot s=b\), equation (4) integrates to
\[
\log v(t)=(A-c)t+\frac{B}{b}\log s(t)+C_0+O(s(t)^{-1}),
\]
with finite \(C_0\), and therefore yields the slow solution and its asserted nonzero amplitude.

**3. Construct the exceptional fast solution.** Eliminate \(u=(\dot v+cv)/s\) from (1), obtaining the exact second-order equation
\[
\ddot v+\left(a+c+ks-\frac bs\right)\dot v+
\left(ac+(ck-a)s-\frac{bc}{s}\right)v=0.
\tag{5}
\]
The Wronskian of two solutions of (5) is a nonzero constant times
\[
W(t)=s(t)\exp\left(-(a+c)t-\frac{k s(t)^2}{2b}\right).
\]
Let \(v_s\) denote the positive slow solution from Step 2. The standard reduction-of-order formula
\[
v_f(t)=v_s(t)\int_t^\infty\frac{W(\tau)}{v_s(\tau)^2}\,d\tau
\tag{6}
\]
defines a second, linearly independent scalar solution, since the integral converges and the Wronskian is nonzero. From \(v_s=e^{\lambda t}s^p(C+O(1/s))\) and a one-sided Gaussian tail estimate in (6),
\[
\log|v_f(t)|=-\frac{k s(t)^2}{2b}+O(t+\log t),\qquad
\frac{\dot v_f(t)}{v_f(t)}=-ks(t)+O(1).
\]
Thus \(u_f=(\dot v_f+cv_f)/s\) obeys \(u_f/v_f=-k+O(1/s)\), and the claimed \(t^{-2}\log\)-norm limit follows because \(s(t)=bt-z_0\). These two independent solutions span the entire transverse plane, proving the claimed alternatives for every initial perturbation.

**4. Critical boundary and finite equilibria.** The slow exponent changes sign at \(k=a/c\). At equality \(A=c\) and \(B=-c^2\), so the slow mode is algebraically decaying with exponent \(-c^2/b\), while the fast one continues to decay with a negative quadratic logarithmic exponent. Equilibria require \(xy=b\), so \(x,y\ne0\). The first two stationary equations imply \(y=ax/(a-ck)\); if \(a-ck=0\) they have no solution, and if nonzero they give
\[
x^2=\frac{b(a-ck)}a,\quad y=\frac bx,\quad z=-\frac{ac}{a-ck}.
\]
The two real sign-related equilibria exist exactly when \(a-ck>0\), and both escape every bounded region as \(k\uparrow a/c\). The source already supplies their formula; the new content is that their loss coincides with the sharp transverse linear-stability transition and the algebraic critical rate.

## Verification
The standalone file `verify.py` checks the axial identity, Jacobian, algebraic equilibria, scalar reduction, exact Riccati residual and both critical simplifications symbolically with SymPy; it independently matches coefficients using \(s^{-1}\) as a formal series parameter and evaluates rational test instances. Execute `python verify.py` with Python 3 and SymPy available. Its successful output reports the checked identities; the global asymptotic assertion follows from Steps 2–3, not from finite computations.

## Relationship to prior work
Dong (2022) introduced this vector field and calculated equilibria and finite-parameter attractors. Its displayed equilibrium formula already contains the threshold \(a-ck=0\), but its analysis does not establish the transverse fundamental-solution splitting along the unbounded axis, the sharp rate \(a/k-c\), or critical decay power \(-c^2/b\). Yang, Wei and Chen (2010) studied the preceding \(k=0\) generalized quadratic system; removing the \(kxz\) term changes the transverse coefficient matrix and does not supply the positive-\(k\) asymptotics. Other axial-escape results for systems with additional coupling in the **third** differential equation have a different transverse variational matrix and cannot imply this theorem by parameter substitution. The proof uses standard Riccati comparison and reduction of order, not a new general asymptotic theorem.

## Limitations
No claim is made about nonlinear attraction of the escaping orbit, global existence for arbitrary off-axis initial data, basin geometry, global chaotic attractors, or behavior at \(k\le0\). Linear transverse decay is not by itself a proof of nonlinear orbital stability along a noncompact orbit. The slowly decaying critical mode is generic only within the transverse two-dimensional variational plane and excludes the explicitly constructed fast line. Completeness of publication-priority searches is not mathematically provable; an unindexed equivalent asymptotic analysis could precede this observation.

## References
- C. Dong, “Dynamics, Periodic Orbit Analysis, and Circuit Implementation of a New Chaotic System with Hidden Attractor,” *Fractal and Fractional* 6 (2022), 190, first publicly posted 2022-03-30. https://doi.org/10.3390/fractalfract6040190
- Q. Yang, Z. Wei and G. Chen, “An Unusual 3D Autonomous Quadratic Chaotic System with Two Stable Node-Foci,” *International Journal of Bifurcation and Chaos* 20 (2010), 1061–1083. https://doi.org/10.1142/S0218127410026320
