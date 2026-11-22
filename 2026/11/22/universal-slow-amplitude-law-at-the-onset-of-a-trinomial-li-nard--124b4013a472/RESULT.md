# Universal slow-amplitude law at the onset of a trinomial Liénard limit cycle

## Finding

Let the coefficients and exponents be as in the next section. For a small negative odd coefficient \(a_2=-\delta^{2(n-m)}\), the once-around Poincaré return map on the upward section \(x=0,\ y>0\), expressed in the scaled coordinate \(y=\delta u\), has a universal slow-time limit: on each compact positive \(u\)-interval,
\[
\frac{\mathcal P_\delta(\delta u)/\delta-u}{\delta^{2n}}
\longrightarrow G(u)=I_m u^{2m+1}-I_n u^{2n+1}
\]
with convergence also of its first \(u\)-derivative, where \(I_j=\int_0^{2\pi}\sin^{2j+2}t\,dt=2\pi\binom{2j+2}{j+1}4^{-(j+1)}\). Thus if \(u_0>0\) and \(u_k^\delta=\mathcal P_\delta^k(\delta u_0)/\delta\), the piecewise-linear interpolation at \(s=k\delta^{2n}\) converges uniformly on any bounded \(s\)-interval to the solution of
\[
\frac{du}{ds}=I_m u^{2m+1}-I_n u^{2n+1},\qquad u(0)=u_0.
\]
This limit is independent of the even-term coefficient and exponent.

The unique attracting limit cycle (whose existence and uniqueness are established in Chen–Lu–Wang–Zhang, 2026) crosses the section at \(y=r_\delta>0\), where
\[
\frac{r_\delta}{\delta}\longrightarrow
u_*:=\left(\frac{I_m}{I_n}\right)^{1/[2(n-m)]}.
\]
Its transverse return multiplier \(\lambda_\delta\), which is positive for sufficiently small \(\delta\), satisfies the sharp weak-attraction law
\[
\frac{1-\lambda_\delta}{\delta^{2n}}
\longrightarrow 2(n-m)I_nu_*^{2n}>0,
\qquad T_\delta\longrightarrow2\pi.
\]
At the critical parameter \(a_2=0\), every sufficiently small positive section orbit decreases to the origin and has the exact algebraic decay
\[
\lim_{k\to\infty}k\,r_k^{2n}=\frac{1}{2n I_n},
\]
where \(r_k\) is the height at the \(k\)-th positive upward crossing.

For example, with \(N=m=2\), \(n=3\), \(a_1=1\), one obtains \(u_*=\sqrt{8/7}\), \((1-\lambda_\delta)/\delta^6\to80\pi/49\), and at criticality \(k r_k^6\to32/(105\pi)\).

## Assumptions and scope

Fix integers \(2\le N\le m<n\) and a finite nonzero real \(a_1\). Consider the real polynomial Liénard flow
\[
\dot x=y-a_1x^{2N}-a_2x^{2m+1}-x^{2n+1},\qquad \dot y=-x.
\]
Set \(a_2=-\delta^{2(n-m)}\) with \(\delta>0\). The local section is \(\Sigma=\{(0,r):r>0\}\), and \(\mathcal P_\delta(r)\) denotes the height at the next crossing of this same half-axis after one complete positive turn; it is defined for all sufficiently small \(r,\delta\). The orientation of rotation is clockwise and does not affect the formulas. Multipliers and periods refer to physical time, not reparameterized time. The slow-time assertion concerns every fixed finite range of \(s\) and every fixed \(u_0>0\), not uniformity over initial data tending to zero or infinity.

## Proof

**1. Exact reversible-center cancellation.** Introduce three auxiliary coefficients \(A,B,C\) and the normalized system
\[
\dot X=Y-A X^{2N}-B X^{2m+1}-C X^{2n+1},\qquad \dot Y=-X,
\]
with initial state \((X,Y)=(0,1)\). Let \(Q(A,B,C)\) be the positive height of its first full return to \(X=0\) after one clockwise circuit. Standard analytic dependence of polynomial ODE solutions and the implicit-function theorem at the transverse crossing near \(2\pi\) show that \(Q\) is real analytic near \((0,0,0)\). When \(B=C=0\), the system is reversible under \(\mathscr R(X,Y)=(-X,Y)\): its vector field \(V\) obeys \(V(\mathscr R z)=-D\mathscr R\,V(z)\). An orbit near the harmonic circle starting on the fixed axis crosses that axis again transversally near time \(\pi\). Reversing the latter half via \(\mathscr R\) closes the orbit, so \(Q(A,0,0)\equiv1\) for all sufficiently small \(A\). This exact cancellation eliminates all pure powers of the even coefficient, not merely their first-order average.

**2. Independent first-variation coefficients.** Put \(E=(X^2+Y^2)/2\). Along solutions,
\[
\dot E=-A X^{2N+1}-B X^{2m+2}-C X^{2n+2}.
\]
At \(A=B=C=0\), the orbit is \((X,Y)=(\sin t,\cos t)\). Differentiating the net energy change with respect to \(B\) or \(C\) at zero gives respectively \(-I_m\) and \(-I_n\). Since the initial and final normalized energies are \(1/2\) and \(Q^2/2\), these are also \(\partial_B Q(0,0,0)=-I_m\) and \(\partial_C Q(0,0,0)=-I_n\). From analytic dependence and \(Q(A,0,0)=1\), uniformly near the origin and with the corresponding first-derivative estimates,
\[
Q(A,B,C)=1-I_mB-I_nC+
O\big((|B|+|C|)(|A|+|B|+|C|)\big).
\]
The same factorization follows by integrating \(\partial_B Q\) and \(\partial_C Q\) along a line segment from \((B,C)=(0,0)\); analyticity controls all derivatives of the remainder.

**3. Rescale the return map.** For a solution with initial height \(r>0\), set \((x,y)=r(X,Y)\). The normalized coefficients are \(A=a_1r^{2N-1}\), \(B=a_2r^{2m}\), \(C=r^{2n}\), and
\[
\mathcal P_{a_2}(r)=r\,Q(a_1r^{2N-1},a_2r^{2m},r^{2n}).
\]
For \(a_2=-\delta^{2(n-m)}\) and \(r=\delta u\), the coefficients become \(A=a_1\delta^{2N-1}u^{2N-1}\), \(B=-\delta^{2n}u^{2m}\), \(C=\delta^{2n}u^{2n}\). Substitution into the preceding analytic expansion yields, in \(C^1\) on every compact interval \(0<u_-\le u\le u_+<\infty\),
\[
\mathcal P_\delta(\delta u)/\delta
=u+\delta^{2n}\big(I_m u^{2m+1}-I_n u^{2n+1}\big)+o(\delta^{2n}).
\]
The scaled map is a consistent Euler discretization of \(u'=G(u)\). The ODE has a unique positive stable equilibrium \(u_*\), and a positive solution stays between its initial point and \(u_*\). On each finite slow-time interval it therefore remains in a compact subset of \((0,\infty)\). The usual discrete Grönwall estimate, using the uniform \(C^1\) remainder, proves convergence of interpolated iterates.

**4. Attracting cycle and multiplier.** The function \(G\) is positive below \(u_*\), negative above, and \(G'(u_*)=-2(n-m)I_nu_*^{2n}<0\). Uniform \(C^1\) convergence gives a fixed point \(u_\delta\tou_*\) for the scaled return map (choose two fixed positive endpoints on opposite sides and use the intermediate-value theorem). Differentiation yields
\[
\mathcal P_\delta'(\delta u_\delta)
=1+\delta^{2n}G'(u_*)+o(\delta^{2n}).
\]
The small fixed point is hyperbolically attracting. The global theorem of Chen–Lu–Wang–Zhang states that this family with \(a_2<0\) has exactly one limit cycle, so the locally constructed cycle is the unique one. Analytic passage times tend to \(2\pi\) under the small-amplitude scaling, proving the physical period limit.

**5. Critical relaxation.** Set \(a_2=0\). The same exact reversible-center argument gives
\[
\mathcal P_0(r)=r-I_n r^{2n+1}+o(r^{2n+1})
\]
as \(r\downarrow0\), even though \(a_1\ne0\). Therefore \(0<\mathcal P_0(r)<r\) for all sufficiently small positive \(r\), and successive positive section heights decrease to zero. For \(z_k=r_k^{-2n}\), Taylor's formula yields \(z_{k+1}-z_k=2nI_n+o(1)\). Cesàro averaging implies \(z_k/k\to2nI_n\), giving the claimed exact asymptotic.

## Verification

The standalone \(verify.py\) recomputes the rational sine-moment coefficients, independently integrates return crossings for the representative family \((N,m,n,a_1)=(2,2,3,1)\), and checks convergence of the scaled orbit amplitude and multiplier toward the exact constants as \(\delta\) decreases. It also tests critical return-map decay at several small radii and compares a full slow-time orbit with the limiting scalar ODE. These numerical checks are consistency tests; analytic dependence, reversibility, the energy first variations and the discrete Grönwall argument are the infinite-dimensional/time proof.

## Relationship to prior work

Chen, Lu, Wang and Zhang (2026) prove exact uniqueness and hyperbolic attraction for the negative-coefficient trinomial Liénard family. Those qualitative results supply the global identification of our locally obtained cycle, but their proof does not compute the small-coefficient amplitude, the sharp multiplier loss or the full scaled slow-time transient. Oliveira, Sánchez-Sánchez and Torregrosa (2022) derive general focal and period constants for polynomial Liénard systems, including leading odd-power coefficients. Their focal-constant framework is compatible with our linearized return coefficients; it does not state the present joint, parameter-uniform amplitude-flow limit and its critical matching law. The methods of center and weak-focus normal forms are standard, so the substantive claim is the explicit matched transition for this family, not the underlying normal-form machinery.

## Limitations

The result is local in orbit amplitude and concerns the singular regime \(a_2\to0^-\) with fixed nonzero \(a_1\) and fixed integer exponents. It does not produce a global basin description, an exact period correction, or universal error bounds on unbounded slow-time intervals. The local proof is self-contained; the assertion that the constructed cycle is the globally unique cycle uses the cited 2026 theorem. Earlier general normal-form results might imply some asymptotic subclaims after further specialization; a historical equivalent of the full matched transition remains possible. No independent validation has been performed.

## References

1. H. Chen, Y. Lu, Q. Wang and R. Zhang, *Uniqueness of limit cycles in a class of classical trinomial Liénard systems*, arXiv:2611.19873v1 (first posted 2026-11-15), https://arxiv.org/html/2611.19873v1.
2. R. D. S. Oliveira, I. Sánchez-Sánchez and J. Torregrosa, *Simultaneous Bifurcation of Limit Cycles and Critical Periods*, Qualitative Theory of Dynamical Systems 21, 20 (2022), https://doi.org/10.1007/s12346-021-00546-x.
3. N. Turner, P. V. E. McClintock and A. Stefanovska, *Maximum amplitude of limit cycles in Liénard systems*, Physical Review E 91, 012927 (2015), https://doi.org/10.1103/PhysRevE.91.012927.
